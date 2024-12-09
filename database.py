from logging_config import get_logger
import sqlite3
import pyexcel as p
import pandas as pd
import os

logger = get_logger()


# Caminho do banco de dados
DB_FOLDER = "database"
DB_PATH = os.path.join(DB_FOLDER, "estados.db")

# Garantir que a pasta existe
if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)

def armazenar_dados_no_banco(df, db_path="database/estados.db"):
    """Armazena os dados do DataFrame no banco de dados SQLite."""
    logger.info("Iniciando armazenamento no banco de dados.")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Criar tabela, se necessário
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS estados (
                sigla TEXT PRIMARY KEY,
                estado TEXT,
                capital TEXT,
                regiao TEXT,
                populacao INTEGER
            )
        """)
        logger.info("Tabela 'estados' verificada/criada com sucesso.")

        # Inserir/atualizar dados
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT OR REPLACE INTO estados (sigla, estado, capital, regiao, populacao)
                VALUES (?, ?, ?, ?, ?)
            """, (row['sigla'], row['estado'], row['capital'], row['regiao'], row['populacao']))

        conn.commit()
        logger.info(f"Armazenamento concluído. Total de registros: {len(df)}.")
    except Exception as e:
        logger.error(f"Erro ao armazenar dados no banco: {e}")
    finally:
        conn.close()




def realizar_consultas_e_exportar(db_path="database/estados.db"):
    """Realiza as consultas SQL e exporta os resultados para arquivos no formato XLS."""
    logger.info("Iniciando consultas e exportações.")

    try:
        # Verificar se o caminho do banco existe
        if not os.path.exists(db_path):
            raise FileNotFoundError(f"O banco de dados não foi encontrado no caminho: {db_path}")

        # Conexão com o banco de dados
        conn = sqlite3.connect(db_path)

        # Pasta para salvar os arquivos de saída
        OUTPUT_FOLDER = "outputs"
        if not os.path.exists(OUTPUT_FOLDER):
            os.makedirs(OUTPUT_FOLDER)

        # Consulta 1
        logger.info("Executando consulta para as 3 regiões mais populosas.")
        df_top3_regioes = pd.read_sql_query("""
            SELECT regiao, SUM(populacao) AS total_populacao
            FROM estados
            GROUP BY regiao
            ORDER BY total_populacao DESC
            LIMIT 3
        """, conn)
        df_top3_regioes.to_csv("outputs/top3_regioes_populosas.csv", index=False)
        logger.info("Consulta 1 exportada com sucesso para 'top3_regioes_populosas.csv'.")

        # Consulta 2
        logger.info("Executando consulta para regiões e quantidade de capitais.")
        df_regioes_n_capitais = pd.read_sql_query("""
            SELECT regiao, COUNT(capital) AS numero_capitais
            FROM estados
            GROUP BY regiao
        """, conn)
        p.save_as(
            records=df_regioes_n_capitais.to_dict(orient="records"),
            dest_file_name="outputs/regioes_n_capitais.xls"
        )
        logger.info("Consulta 2 exportada com sucesso para 'regioes_n_capitais.xls'.")

        # Consulta 3
        logger.info("Executando consulta para os 2 estados com as capitais mais populosas.")
        df_estados_mais_populosos = pd.read_sql_query("""
            SELECT estado, capital, populacao
            FROM estados
            ORDER BY populacao DESC
            LIMIT 2
        """, conn)
        p.save_as(
            records=df_estados_mais_populosos.to_dict(orient="records"),
            dest_file_name="outputs/estados_mais_populosos.xls"
        )
        logger.info("Consulta 3 exportada com sucesso para 'estados_mais_populosos.xls'.")

    except Exception as e:
        logger.error(f"Erro ao realizar consultas/exportações: {e}")
    finally:
        conn.close()
        logger.info("Conexão com o banco encerrada.")
        print("Consultas realizadas e arquivos exportados com sucesso!")



    

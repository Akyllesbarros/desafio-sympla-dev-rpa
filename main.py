from database import armazenar_dados_no_banco, realizar_consultas_e_exportar, DB_PATH
from scraping import coletar_dados_estados
from data_processing import combinar_dados
from logging_config import get_logger 
import os

logger = get_logger()

if __name__ == "__main__":
    # Dados extraídos do Selenium
    siglas, estados, capitais, regioes = coletar_dados_estados()
    print("Siglas:", siglas)
    print("Estados:", estados)
    print("Capitais:", capitais)
    print("Regiões:", regioes)

    # Arquivo de exemplo
    arquivo_excel = "resources/PopulaçãoxCapital.xlsx"

    # Combinar dados
    df_resultado = combinar_dados(siglas, estados, capitais, regioes, arquivo_excel)
    print("\n\n")
    print(df_resultado.head())  # Visualizar as primeiras linhas

    # Usar o DataFrame df_resultado do passo anterior
    armazenar_dados_no_banco(df_resultado, db_path=DB_PATH)
    print("Dados armazenados no banco com sucesso!")

    # Realizar consultas e exportar resultados
    realizar_consultas_e_exportar(db_path=DB_PATH)

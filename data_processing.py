from logging_config import get_logger
import pandas as pd
import unicodedata

logger = get_logger()

def processar_arquivo_excel(arquivo_excel):
    # Carregar os dados do Excel
    df_excel = pd.read_excel(arquivo_excel, header=None, names=["Capital/populacao"])

    # Ignorar o cabeçalho "Capital/populacao"
    df_excel = df_excel.iloc[1:]  

    # Separar as colunas com base no delimitador ":"
    df_excel[['capital', 'populacao']] = df_excel['Capital/populacao'].str.split(':', expand=True)

    # Remover espaços extras
    df_excel['capital'] = df_excel['capital'].str.strip()
    df_excel['populacao'] = df_excel['populacao'].str.strip()

    # Converter valores para string antes de remover pontos
    df_excel['populacao'] = df_excel['populacao'].str.replace('.', '', regex=False)

    # Converter população para inteiro
    print("\n\nAntes da conversão para inteiro:")
    print(df_excel['populacao'])
    df_excel['populacao'] = df_excel['populacao'].astype(int)

    # Retornar o DataFrame resultante
    return df_excel[['capital', 'populacao']]


def normalizar_texto(texto):
    """Remove acentuação e espaços extras, e converte para maiúsculas."""
    if isinstance(texto, str):
        texto = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')
        return texto.strip().upper()
    return texto


def combinar_dados(siglas, estados, capitais, regioes, arquivo_excel):
    """Combina dados extraídos do Selenium com os dados de população do Excel."""
    logger.info("Iniciando combinação de dados.")
    try:
        # Processar dados do Excel
        df_populacao = processar_arquivo_excel(arquivo_excel)
        logger.info("Dados do Excel processados com sucesso.")
        
        # Normalizar os nomes das capitais no DataFrame do Excel
        df_populacao['capital'] = df_populacao['capital'].apply(normalizar_texto)
        
        # Criar DataFrame com dados extraídos do Selenium
        df_estados = pd.DataFrame({
            'sigla': siglas,
            'estado': estados,
            'capital': capitais,
            'regiao': regioes
        })
        logger.info("Dados extraídos do Selenium organizados com sucesso.")

        # Normalizar os nomes das capitais no DataFrame do Selenium
        df_estados['capital'] = df_estados['capital'].apply(normalizar_texto)

        # Combinar os DataFrames (baseado na coluna 'capital')
        df_combinado = pd.merge(df_estados, df_populacao, on='capital', how='left')
        
        logger.info("Combinação de dados concluída.")
        return df_combinado
    
    except Exception as e:
        logger.error(f"Erro ao combinar dados: {e}")
        raise

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from logging_config import get_logger

# Inicializar o logger
logger = get_logger()

def coletar_dados_estados():
    """Coleta dados de estados, capitais e regiões usando web scraping."""
    
    logger.info("Iniciando o processo de coleta de dados dos estados.")

    # Configuração automática do driver
    try:
        driver = webdriver.Chrome()
        logger.info("Driver configurado com sucesso.")

        # URL do site
        url = "https://inanyplace.blogspot.com/2017/01/lista-de-estados-brasileiros-sigla-estado-capital-e-regiao.html"
        logger.info(f"Acessando a URL: {url}")
        driver.get(url)
        logger.info(f"Título da página carregada: {driver.title}")

        # Localizar a tabela
        logger.info("Localizando a tabela na página.")
        tabela = driver.find_element(By.TAG_NAME, "table")
        linhas = tabela.find_elements(By.TAG_NAME, "tr")  # Todas as linhas

        # Listas para armazenar os dados
        siglas = []
        estados = []
        capitais = []
        regioes = []

        # Percorrer as linhas, ignorando o cabeçalho
        logger.info("Iniciando extração dos dados da tabela.")
        for linha in linhas[1:]:
            colunas = linha.find_elements(By.TAG_NAME, "td")  # Todas as colunas da linha
            if len(colunas) >= 4:  # Garantir que a linha tem pelo menos 4 colunas
                siglas.append(colunas[0].text)
                estados.append(colunas[1].text)
                capitais.append(colunas[2].text)
                regioes.append(colunas[3].text)
        logger.info(f"Extração concluída com sucesso. Total de registros coletados: {len(siglas)}.")

    except Exception as e:
        logger.error(f"Erro durante o processo de coleta de dados: {e}")
    
    finally:
        # Fechar o navegador
        driver.quit()
        logger.info("Driver encerrado.")

    # Retornar os dados
    return siglas, estados, capitais, regioes

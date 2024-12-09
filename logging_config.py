import logging
import os

def get_logger():
    """Configura e retorna o logger."""
    # Diretório para armazenar os logs
    LOG_FOLDER = "logs"
    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)

    # Configuração do logger
    logging.basicConfig(
        filename=os.path.join(LOG_FOLDER, "processo.log"),
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger()

import logging

def setup_config():
    logging.basicConfig(
        filename="logs.log",
        format="%(asctime)s %(levelname)s %(message)s",
        level=logging.INFO
    )

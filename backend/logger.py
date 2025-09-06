import logging
import sys
import os

def logger_setup(DEBUG=True):
    logger = logging.getLogger("okko")
    
    logger.handlers.clear()
    
    log_level = logging.DEBUG if DEBUG == True else logging.INFO
    logger.setLevel(log_level)
    
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    
    if DEBUG == False:
        LOG_FILE = os.path.join("logging.log")
        file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    return logger
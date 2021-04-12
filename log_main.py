import logging, sys
from logging import FileHandler

def log_get():
    logger = logging.getLogger(__name__)
    level = logging.setLevel('INFO')
    FORMAT = '%(asctime)s %(processName)s\%(name)-8s %(levelname)s: %(message)s'
    logging.basicConfig(format = FORMAT, level='INFO', filename = 'log.txt' )
    handler = FileHandler(logfile)
    

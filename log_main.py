import logging, sys
from logging import FileHandler

class Logger_get(self):
    def __init__:
    self.logger = logger
    self.FORMAT= FORMAT
    logger = logging.getLogger(__name__)
    FORMAT = '%(asctime)s - %(message)s'
    logging.basicConfig(format = FORMAT, level=logging.INFO, filename = 'log.txt' )
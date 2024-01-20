import logging
import os
import sys
import logging.handlers
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)-15s %(levelname)s:%(message)s')
file_handler = logging.handlers.TimedRotatingFileHandler( 
        'log/{0}.log'.format(os.path.basename(sys.argv[0])), 'D', 1, backupCount=10)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
# Usage: from mylogger import logger
# logger.info("{}, {}".format(uuid, result))

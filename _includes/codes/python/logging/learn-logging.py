import logging
import sys

logger=logging.getLogger('learn-logging')
formatter=logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s)')

file_handler=logging.FileHandler("example.log")
file_handler.formatter=formatter

console_handler=logging.StreamHandler(sys.stdout)
console_handler.formatter=formatter

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.setLevel(logging.INFO)

logger.debug('this is debug info')
logger.info('this is information')
logger.warn('this is warning message')
logger.error('this is error message')
logger.fatal('this is fatal message, it is same as logger.critical')
logger.critical('this is critcal message')



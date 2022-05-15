import logging

logger_app = logging.getLogger()
logger_app.setLevel('DEBUG')
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('app.log')
logger_app.addHandler(console_handler)
logger_app.addHandler(file_handler)
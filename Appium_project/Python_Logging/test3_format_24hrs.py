import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%d/%m/%y %H:%M:%S %p %A' ,filename='test_log',level=logging.DEBUG,filemode='a')
#filename = 'a' means data will append

#logging.basicConfig(format='%(asctime)s: %(levelname)s : %(message)s',datefmt='%d/%m/%y %H:%M:%S %p %A',level=logging.DEBUG,filename='test_log1',filemode='w')
#filename = 'w' means updated data will be load only

logging.critical('This is critical message')
logging.error('This error message')
logging.warning('This is warning message')
logging.info('This is just info message')
logging.debug('This is debug message')

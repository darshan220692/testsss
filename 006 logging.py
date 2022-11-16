import logging

logging.basicConfig(filename="test6.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s ')

try:
    logging.info("I am trying to read a file")
    with open("test6.txt", "r"):
        logging.info("sucessfully it has read the file")
except Exception as e:
    logging.critical("This is a situation for us ")
    logging.error(e)
    logging.exception(e)
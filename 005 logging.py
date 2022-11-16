""" There are multiple levels in the logging
DEBUG - 10, INFO- 20, WARNING - 30, ERROR - 40, CRITICAL-50, If we are taking level error it will not consider other level
logging so it will print nothing in the .txt file """
import logging

logging.basicConfig(filename="test5.log", level=logging.ERROR, format='%(levelname)s %(asctime)s %(name)s %(message)s')

def devide(a,b):
    logging.info("the number entered by user is %s and %s ", a,b)
    try:
        logging.info("We are in to funciton")
        div = a/b
        logging.info("completed the div")
        logging.info(" final output %d ", div)
        return div
    except Exception as e:
        logging.exception(e)
devide(20,5)
import logging
logging.basicConfig(filename="test4.log", level=logging.INFO, format= '%(levelname)s %(asctime)s %(name)s %(message)s')

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
print(devide(20,5))
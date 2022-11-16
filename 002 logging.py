""" Log Labels
debug/warning/error/critical/info
Debug- dignosis
warning- information about the future action
error- issues in the code
critical - very serious error
info - informaiton about the activity"""
import logging
logging.basicConfig(filename= "test.log", level= logging.INFO)
logging.info("Darshan  is the best data scientist in the world")
logging.warning(" I am also block chain developer")
l= [5,6,4,5,4,6,2,4,2]
for i in l:
    if i == 2:
        # logging.info(i)
        logging.info(l)
        logging.warning(" Dont waste your time")
        logging.error("Distractions are error")

logging.shutdown()
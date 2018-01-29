'''
 Primary program to execute IDS related programs
'''
import datetime
import sys
import os
import time
import hashlib
import threading, queue
import subprocess
import rsa
import yaml
import pickle

# import custom modules
import logger as logger

'''
 Function Purpose: Simplify logging by creating a function
    to streamline the need to do logger.logging.level
 Depencies: custom module logger
 Inputs:
    message => A programmers' specified message. Should contain the error.
        TYPE: String
    level => Specify the severity of the log
        TYPE: String
'''
def log(message, level="INFO", verbose=False):
    if (verbose == True):
        print (message)

    if (level == "INFO"):
        logger.logging.info(message)
    if (level == "DEBUG"):
        logger.logging.debug(message)
    if (level == "WARNING"):
        logger.logging.warning(message)
    if (level == "ERROR"):
        logger.logging.error(message)
    if (level == "CRITICAL"):
        logger.logging.critical(message)
# Test and confirmation log input
log("Starting up program!", verbose=True)

# Record current working directory
log("Current working directory" + str(os.path.dirname(os.path.realpath(__file__))))

# Try to open up the configuration file
try:
    with open("config.yaml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)
except:
    log("Issue opening up configuration file! Error: " + str(sys.exc_info()[0]))
    pass

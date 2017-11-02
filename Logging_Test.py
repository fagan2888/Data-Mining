import logging
import warnings
import os

# Setup Logging File and Format
#########################################################################################################
# Declare Logging Object referenced to what the log file will be named
logger = logging.getLogger("LogExample")

# Declare level of logging to a file
# For details on logging levels see here: https://docs.python.org/2/library/logging.html#logging-levels
# Anything with the level of 'DEBUG' or lower will be recorded to the file
logger.setLevel(logging.DEBUG)

# Setup format for text recorded in the log file:
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Declare object to handle Log file, create Log file name, set to 'w' so it overwrites existing log or 'a' to
# append to existing log
file_handler = logging.FileHandler('LogExample.log', mode='w')

# Set formatting to log handling object
file_handler.setFormatter(formatter)

# (Optional) Declare logging object that will print the logged messages to the console as well
stream_handler = logging.StreamHandler()
# Set formatting to log handling object
stream_handler.setFormatter(formatter)

# Add the 1 or 2 logger objects to enable logging.METHODS('message')
logger.addHandler(file_handler)  # records logging statements to a log file
logger.addHandler(stream_handler)  # prints log statements to the console

# Practice log methods:
logger.info('What is my favorite number?')
logger.debug('Your favorite number must be 0!')

# Using logger.exception('message') will record the message to the log AND the traceback of the error
# IF it is used in a try/except block
# Declared variables in a script can be recorded as well
favorite_num = 0
five = 5
try:
    logger.info('Attempting to calculate: ' + str(five) + '/' + str(favorite_num))
    test = five / favorite_num
except ZeroDivisionError:
    file_object = os.path.abspath('Logging_Test.py')
    logger.exception('There is an error with this file: ' + file_object)

# You can also record warnings to the log (be sure to import warnings though)
# Set the logger to capture Warnings
logging.captureWarnings(True)

# Instantiate a warnings logger object and add the current log file
warnings_logger = logging.getLogger("py.warnings")
warnings_logger.addHandler(file_handler)

# Execute a warning that will print to the console and record to the log file
warnings.warn(u'WARNING: DIVIDING BY 0 IN THIS PROGRAM HAS CAUSED A CRITICAL SYSTEM ERROR')

# Practice Log critical message
logger.critical('ERROR REACHED. SHUTTING DOWN...')

__author__ = 'Matt Wilchek'

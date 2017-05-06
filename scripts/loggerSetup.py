import sys
import logging
import logging.config

# to call use:
#    import loggerSetup
#    loggerSetup.(1,debug,'debug message')
# or loggerSetup.logDBManager(debug,'debug message')

#    loggerSetup(1,info,'info message')
#    loggerSetup(1,warn,'warn message')
#    loggerSetup(1,error,'error message')
#    loggerSetup(1,critical,'critical message')
logging.config.fileConfig('../logs/logging.ini')
logger = logging.getLogger('default')


def log(level,message):
    if level == 'DEBUG':
        logger.debug(' ' + str(message))
    if level == 'INFO':
        logger.info(' ' + str(message))
    if level == 'WARN':
        logger.warn(' ' + str(message))
    if level == 'ERROR':
        logger.error(' ' + str(message))
    if level == 'CRITICAL':
        logger.critical(' ' + str(message))

def logDBManager(level,message):
    logger.debug(' Triggered By Script: dbmanager.py')
    log(level,message)
    
    
def logWizard(level,message):
    logger.debug(' Triggered By Script: wizardHandler.py')
    log(level,message)

def logBlockchain(level,message):
    logger.debug(' Triggered By Script: blockchain.py')
    log(level,message)

def unknownLog():
    logger.debug(' Triggered By Unknown')
    log(level,message)
    return

def main(arg1,arg2,arg3):
    level = arg2
    message = arg3
    if arg1 == 0:
        logDBManager(level,message)
    elif arg1 == 1:
        logWizard(arg2,arg3)
    elif arg1 == 2:
        logBlockchain(arg2,arg3)        
    else:
        unkownLog(arg2,arg3)

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])

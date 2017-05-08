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


def log(level,message,script):
    if level == 'DEBUG':
        logger.debug(' ' + str("Triggered By: ") + script + str(message))
    if level == 'INFO':
        logger.info(' ' + str("Triggered By: ") + script + str(message))
    if level == 'WARN':
        logger.warn(' ' + str("Triggered By: ") + script + str(message))
    if level == 'ERROR':
        logger.error(' ' + str("Triggered By: ") + script + str(message))
    if level == 'CRITICAL':
        logger.critical(' ' + str("Triggered By: ") + script + str(message))

def main(arg1,arg2,arg3):
    level = arg2
    message = arg3
    if arg1 == 0:
        log('dbmanager.py',level,message)
    elif arg1 == 1:
        log('wizardHandler.py',arg2,arg3)
    elif arg1 == 2:
        log('blockchain.py',arg2,arg3)        
    else:
        log('other',arg2,arg3)

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])

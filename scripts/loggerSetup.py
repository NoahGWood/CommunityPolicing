#! /usr/bin/python3
import sys
import logging
import logging.config

# to call use:
#   import loggerSetup
#   def log(level,e):
#       script = __file__
#       loggerSetup.main(script,level,str(e))
#   log('DEBUG','your error')
logging.config.fileConfig('../logs/logging.ini')
logger = logging.getLogger('default')



def log(script,level,message):
    print(' Unknown error Triggered by {0} | {1}'.format(script,message))
    if level in ['D','d','DEBUG','debug','Debug']:
        logger.debug(" Triggered By: " + script + ' ' + str(message))
    if level in ['I','i','INFO','info','Info']:
        logger.info(" Triggered By: " + script + ' ' + str(message))
    if level in ['W','w','WARN','warn','Warn']:
        logger.warn("Triggered By: " + script + ' ' + str(message))
    if level in ['E','e','ERROR','error','Error']:
        logger.error("Triggered By: " + script + ' ' + str(message))
    if level in ['C','c','CRITICAL','critical','Critical']:
        logger.critical(" Triggered By: " + script + ' ' + str(message))
    logger.fatal(' Unknown error Triggered by {0} | {1}'.format(script,message))
        
def xcept(e):
    logger.exception(e)
                     
def main(arg1,arg2,arg3):
    log(arg1,arg2,arg3)

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2],sys.argv[3])

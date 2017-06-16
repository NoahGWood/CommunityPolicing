#!/usr/bin/python3
"""DistribCollabOSINT-dbManager

Usage:
settings.py <Section> <Label> <Value>

Options:
-h --help  Display this help page
-v --version  Display version information
For more RTFM: man ./settings.py
"""
import logging
import configparser

import docopt
from py2neo import Graph, Node, Relationship, remote

#logger settings
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#config and file settings
config = configparser.ConfigParser()

f = 'settings.ini'
def check_file():
    try:
        cfgfile = open(f,'r+')
        return(cfgfile)
    except:
        cfgfile = open(f,'w')
        return(cfgfile)

def set_setting(sect, label, value, cfgfile):
    try:
        if isinstance(sect, str): #checking if values are strings
            if isinstance(label, str):
                if isinstance(value, str) or isinstance(value, bool):
                    logger.debug('reading')
                    config.read(f)
                    try:
                        logger.debug('addsection')
                        config.add_section(sect)
                        logger.debug('addsection-complete')
                        config.set(section,label,value)
                        logger.debug('string-section created')
                        config.write(cfgfile)
                        cfgfile.close()
                    except Exception as e:
                        logger.debug(e)
                        config.set(sect,label,value)
                        logger.debug('string-section exist')
                        config.write(cfgfile)
                        cfgfile.close()
                else:
                    raise Exception('Incorrect type in value: string or bool expected, got {}'.format(value.__name__))
            else: raise Exception('Incorrect type in label: string expected, got {}'.format(value.__name__))
        else:
            if isinstance(sect, list):  # ensure all vars are lists
                if isinstance(label, list):
                    if isinstance(value,list):
                        if len(sect) == len(label):  # check list sizes
                            if len(sect) == len(value):
                                for i in range(len(sect)):
                                    try:  # Test if section exists, create if not
                                        logger.debug('list')
                                        config.options(sect[i])
                                        config.set(sect[i],label[i],value[i])
                                    except:
                                        config.add_section(sect[i])
                                        config.set(sect[i],label[i],value[i])
                                config.write(cfgfile)
                                cfgfile.close()
                            else: # debugging stuff
                                raise Exception('Invalid size in value. Expected {0} got {1}'.format(len(sect), len(value)))
                        else:
                            raise Exception('Invalid size in label. Expected {0} got {1}'.format(len(sect), len(label)))

                    else:
                        raise Exception('Incorrect type in value: list expected, got {}'.format(value.__name__))
                else:
                    raise Exception('Incorrect type in label: list expected got {0}'.format(label))
            else:
                raise Exception('Incorrect type in section: list expected got {0}'.format(sect))
    except Exception as e:
        logger.debug('set_setting in settings.py ' + str(e))

if __name__ == '__main__':
    try:
        cfgfile = check_file()
        arguments = docopt.docopt(__doc__, version='dbDriver: 0.0.1')
        logger.debug(arguments)
        sect = arguments['<Section>']
        label = arguments['<Label>']
        value = arguments['<Value>']
        set_setting(sect, label, value, cfgfile)
    except docopt.DocoptExit as e:
        logger.debug(e)

#!/usr/bin/python3
"""DistribCollabOSINT-dbManager

Usage:
dbDriver.py add <table> <data>
dbDriver.py delete [<node>|--all|--relationship <key>]
dbDriver.py relation <node1,relationship,node2>
dbDriver.py find-relation <node,relationship>
dbDriver.py find-node <node>

/===========================================================\

|# Basic Commands:                                         #|
|#    add  Add to database                                 #|
|#    find  Execute search query                           #|
|#    delete <node>  Delete node                           #|
|#    delete all  DELETES ENTIRE DATABASE                  #|
\===========================================================/

Arguments:
cmd  Commands(e.g. add, rm)
target  Database targets
args  See options


Options:
-h --help  Display this help page
-v --version  Display version information
--limit 

Examples:
person fname,lname,mname,ethn
loc country,state,city,address,zipcode
crime description,date
group name,gtype
media name,MIME,loc,hashd
website name,url
fbu uname,url,uid
fbp post,url
fbe name,url,descr,date
fbg name,url,descr
rel node1,type,node2,properties

For more, RTFM: man ./dbdriver
"""
import logging

import docopt
from py2neo import Graph, Node, Relationship, remote

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
try:
    graph = Graph(host="localhost", user="neo4j", password="password")
except Exception as e:
    logger.debug(str(e))

# TODO(OP): Create an index function
#  Indexes greatly increase querying speed (but remember it's at the expense of writing and storage!)
#  Should be an opt-in function to allow users with less storage space to work.

# These create functions will work for now, however down the line and preferrably before beta testing
#  it should be implemented the ability to add custom structured data which will enable the program to be even more
#  community supported (won't need to send pull requests to the main repo)
# Example: dbDriver.py add NewTable value1=value,value2=value; etc.

def create_person(fname, lname, mname, ethn):
    try:
        person = Node("Person", fname=fname, lname=lname, mname=mname, ethn=ethn)
        graph.create(person)
        return(True)
    except Exception as e:
        logger.debug('createPerson')
        logger.debug(e)
        return(False)


def create_loc(country, state, city, address, zipcode):
    try:
        loc = Node("Location", country=country, state=state, city=city, address=address, zipcode=zipcode)
        graph.create(loc)
        return(True)
    except Exception as e:
        logger.debug('createLoc')
        logger.debug(e)
        return(False)


def create_crime(descr, date):
    try:
        crime = Node("Crime", descr=descr, date=date)
        graph.create(crime)
        return(True)
    except Exception as e:
        logger.debug('createCrime')
        logger.debug(e)
        return(False)

def create_group(name, gtype):
    try:
        group = Node("Group", name=name, gtype=gtype)
        graph.create(group)
        return(True)
    except Exception as e:
        logger.debug('createCrime')
        logger.debug(e)
        return(False)

def create_media(name, MIME, loc, hashd):
    try:
        media = Node("Media", name=name, MIME=MIME, loc=loc, hashd=hashd)
        graph.create(meda)
        return(True)
    except Exception as e:
        logger.debug('createMedia')
        logger.debug(e)
        return(False)

def create_website(name, url):
    try:
        web = Node("Website", name=name, url=url)
        graph.create(web)
        return(True)
    except Exception as e:
        logger.debug('createWebsite')
        logger.debug(e)
        return(False)

def create_fbuser(uname, url, uid):
    try:
        fbuser = Node("FBUser", uname=uname, url=url, uid=uid)
        graph.create(fbuser)
        return(True)
    except Exception as e:
        logger.debug('createFBUser')
        logger.debug(e)
        return(False)

def create_fbpost(post, url):
    try:
        fbpost = Node("FBPost", post=post, url=url)
        graph.create(fbpost)
        return(True)
    except Exception as e:
        logger.debug('createFBPost')
        logger.debug(e)
        return(False)

def create_fbevent(name, url, descr, date):
    try:
        fbevent = Node("FBEvent", name=name, url=url, descr=descr, date=date)
        graph.create(fbevent)
        return(True)
    except Exception as e:
        logger.debug('createFBEvent')
        logger.debug(e)
        return(False)

def create_fbgroup(name, url, descr):
    try:
        fbgroup = Node("FBGroup", name=name, url=url, descr=decsr)
        graph.create(fbgroup)
        return(True)
    except Exception as e:
        logger.debug('createFBGroup')
        logger.debug(e)
        return(False)

def del_db():
    try:
        graph.delete_all()
        return(True)
    except Exception as e:
        logger.debug('delDB')
        logger.debug(e)
        return(False)

def del_entity(*a):
    try:
        graph.delete(*a)
        return(True)
    except Exception as e:
        logger.debug('delEntity')
        logger.debug(e)
        return(False)

def add_rel(start_node, rel_type, end_node):
    tx = graph.begin()
    try:
        start_node = graph.node(int(start_node))
        end_node = graph.node(int(end_node))
        logger.debug(start_node)
        logger.debug(end_node)
        rel = Relationship(start_node, str(rel_type), end_node)
        tx.create(rel)
        tx.commit()
        logger.debug('Returned: ' + str(rel))
        return(True)
    except Exception as e:
        logger.debug('addRel')
        logger.debug(e)
        return(False)

def find_rel(start_node, rel_type):
    returns = []
    try:
        # we have to pull the node before we can begin searching for its' relationships
        for rel in graph.match(start_node=graph.node(int(start_node)), rel_type=rel_type):  
            returns.append(rel.end_node)
        return(True, returns)
    except Exception as e:
        logger.debug('findRel')
        logger.debug(e)
        return(False)

def del_rel(key):
    try:
        tx = graph.begin()
        rel = graph.relationship(int(key)) # see if we can find the key
        tx.separate(rel)
        tx.commit()
        return(True)
    except Exception as e:
        logger.debug('delRel')
        logger.debug(e)
        return(False)

def find_node(node):
    try:
        returns = graph.node(int(node))
        return(True, returns)
    except Exception as e:
        logger.debug('findNode')
        logger.debug(e)
        return(False)

def query(args):
    try:
        returns = graph.run(args)
        return(True, returns)
    except Exception as e:
        logger.debug('query')
        logger.debug('Input =' + str(args))
        logger.debug(e)
        return(False)

if __name__ == '__main__':
    try:
        arguments = docopt.docopt(__doc__, version='dbDriver: 0.0.1')
        logger.debug(arguments)
        # print(arguments)
        if arguments['add'] == True:
            args = ''.join(arguments['<data>'])
            args = args.split(',')
            if arguments['<table>'] in 'person':
                create_person(*args)
            elif arguments['<table>'] in 'loc':
                create_loc(*args)
            elif arguments['<table>'] in 'crime':
                create_crime(*args)
            elif arguments['<table>'] in 'group':
                create_group(*args)
            elif arguments['<table>'] in 'media':
                create_media(*args)
            elif arguments['<table>'] in 'website':
                create_website(*args)
            elif arguments['<table>'] in 'fbu':
                create_fbuser(*args)
            elif arguments['<table>'] in 'fbp':
                create_fbpost(*args)
            elif arguments['<table>'] in 'fbe':
                create_fbevent(*args)
            elif arguments['<table>'] in 'fbg':
                create_fbgroup(*args)
        elif arguments['delete'] == True:
            logger.debug(str(arguments))
            if arguments['--all']==True:
                del_db()
            elif arguments['--relationship']==True:
                del_rel(str(arguments['<key>']))
        elif arguments['relation']==True:
            logger.debug(arguments['<node1,relationship,node2>'])
            args = ''.join(str(arguments['<node1,relationship,node2>']))
            args = args.split(',')
            add_rel(*args)
        elif arguments['find-relation'] == True:
            args = ''.join(str(arguments['<node,relationship>']))
            args = args.split(',')
            find_rel(*args)
        elif arguments['find-node'] == True:
            args = ''.join(str(arguments['<node>']))
            find_node(args)

    except docopt.DocoptExit as e:
        logger.debug(e)


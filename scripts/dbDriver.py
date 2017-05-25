#!/usr/bin/python3
"""DistribCollabOSINT-dbManager

Usage:
dbDriver.py add <table> <data>
dbDriver.py delete [<node>|--all|--relationship <key>]
dbDriver.py relation <node1,relationship,node2>
dbDriver.py find-relation <node,relationship>

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
import docopt
from py2neo import Graph, Node, Relationship, remote
import logging
logger = logging.getLogger()
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
try:
    graph = Graph(host="localhost", user="neo4j", password="password")
except Exception as e:
    logger.debug(str(e))

#To be implemented: Indexes will greatly increase querying speed (at the expense of writing and storage)
#Should be an opt-in function to allow users with less storage space to work.
#def index(_id):
#    index = graph.create_index("Node", "id")
#    tx = g.begin()
#    index = graph.create_index('Node',_id)
#    tx.create(index)
#    tx.commit

#These create functions will work for now, however down the line and preferrably before beta testing
#it should be implemented the ability to add custom structured data which will enable the program to be even more
#community supported (won't need to send pull requests to the main repo)
#Example: dbDriver.py add NewTable value1=value,value2=value; etc.

def createPerson(fname,lname,mname,ethn):
    person = Node("Person",fname=fname,lname=lname,mname=mname,ethn=ethn)
    graph.create(person)

def createLoc(country,state,city,address,zipcode):
    loc = Node("Location",country=country,state=state,city=city,address=address,zipcode=zipcode)
    graph.create(loc)

def createCrime(descr,date):
    crime = Node("Crime",Crime,descr=descr,date=date)
    graph.create(crime)

def createGroup(name,gtype):
    group = Node("Group",name=name,gtype=gtype)
    graph.create(group)

def createMedia(name,MIME,loc,hashd):
    media = Node("Media",name=name,MIME=MIME,loc=loc,hashd=hashd)
    graph.create(meda)

def createWebsite(name,url):
    web = Node("Website",name=name,url=url)
    graph.create(web)

def createFBUser(uname,url,uid):
    fbuser = Node("FBUser",uname=uname,url=url,uid=uid)
    graph.create(fbuser)

def createFBPost(post,url):
    fbpost = Node("FBPost",post=post,url=url)
    graph.create(fbpost)

def createFBEvent(name,url,descr,date):
    fbevent = Node("FBEvent",name=name,url=url,descr=descr,date=date)
    graph.create(fbevent)

def createFBGroup(name,url,descr):
    fbgroup = Node("FBGroup",name=name,url=url,descr=decsr)
    graph.create(fbgroup)

def delDB():
    graph.delete_all()

def delEntity(*a):
    graph.delete(*a)

def addRel(start_node,rel_type,end_node):
#poor documentation of Relationship
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
    except Exception as e:
        logger.debug(e)

def findRel(start_node,rel_type):
    logger.debug('start===============================')
    for rel in graph.match(start_node=graph.node(int(start_node)), rel_type=rel_type):
        logger.debug(rel.end_node()["name"])

def delRel(key):
    tx = graph.begin()
    #see if we can find the key
    rel = graph.relationship(int(key))
    try:
        logger.debug('=================================================')
        tx.separate(rel)
        tx.commit()
    except Exception as e:
        logger.debug(e)
#    graph.re

#def match(self, start_node=None, rel_type=None, end_node=None, bidirectional=False, limit=None):
 #   for rel in graph.match(start_node=alice, rel_type="FRIEND"):
  #      return(rel.end_node.properties["name"])
    
    #do something?
if __name__ == '__main__':
    try:
        arguments = docopt.docopt(__doc__, version='dbDriver: 0.0.1')
        logger.debug(arguments)
        #print(arguments)
        if arguments['add'] == True:
            args = ''.join(arguments['<data>'])
            args = args.split(',')
            if arguments['<table>'] in 'person':
                createPerson(*args)
            elif arguments['<table>'] in 'loc':
                createLoc(*args)
            elif arguments['<table>'] in 'crime':
                createCrime(*args)
            elif arguments['<table>'] in 'group':
                createGroup(*args)
            elif arguments['<table>'] in 'media':
                createMedia(*args)
            elif arguments['<table>'] in 'website':
                createWebsite(*args)
            elif arguments['<table>'] in 'fbu':
                createFBUser(*args)
            elif arguments['<table>'] in 'fbp':
                createFBPost(*args)
            elif arguments['<table>'] in 'fbe':
                createFBEvent(*args)
            elif arguments['<table>'] in 'fbg':
                createFBGroup(*args)
        elif arguments['delete'] == True:
            logger.debug(str(arguments))
            if arguments['--all']==True:
                delDB()
            elif arguments['--relationship']==True:
                delRel(str(arguments['<key>']))
        elif arguments['relation']==True:
            logger.debug(arguments['<node1,relationship,node2>'])
            args = ''.join(str(arguments['<node1,relationship,node2>']))
            args = args.split(',')
            addRel(*args)
        elif arguments['find-relation'] == True:
            args = ''.join(str(arguments['<node,relationship>']))
            args = args.split(',')
            findRel(*args)
            

    except docopt.DocoptExit as e:
        logger.debug(e)


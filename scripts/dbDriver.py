#!/usr/bin/python3
"""DistribCollabOSINT-dbManager

Usage:
dbDriver.py <cmd> <target> [<args>]
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

For more, RTFM: man ./dbdriver
"""
import docopt
from py2neo import Graph, Node
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

#def addRel(*a):

def findRel(start_node,rel_type):
    # def match(self, start_node=None, rel_type=None, end_node=None, bidirectional=False, limit=None):
    for rel in graph.match(start_node=alice, rel_type="FRIEND"):
        return(rel.end_node.properties["name"])
    
    #do something?
if __name__ == '__main__':
    try:
        arguments = docopt.docopt(__doc__, version='dbDriver: 0.0.1')
        logger.debug('docupt succeed')
        logger.debug(arguments)
        args = ''.join(arguments['<args>'])
        args = args.split(',')
        cmd = ''.join(arguments['<cmd>'])
        target = ''.join(arguments['<target>'])
        logger.debug(str(args),str(cmd),str(target))
        if cmd in 'add':
            if target in 'person':
                createPerson(*args)
            elif target in 'loc':
                createLoc(*args)
            elif target in 'crime':
                createCrime(*args)
            elif target in 'group':
                createGroup(*args)
            elif target in 'media':
                createMedia(*args)
            elif target in 'website':
                createWebsite(*args)
            elif target in 'fbu':
                createFBUser(*args)
            elif target in 'fbp':
                createFBPost(*args)
            elif target in 'fbe':
                createFBEvent(*args)
            elif target in 'fbg':
                createFBGroup(*args)
    except docopt.DocoptExit as e:
        print(e)


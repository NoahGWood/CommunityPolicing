#!/usr/bin/python3
"""DistribCollabOSINT-dbManager

Usage: dbDriver.py <cmd> <target> <args>

Arguments:
cmd  Commands(e.g. add, rm)
target  Database targets
args  See options


Options:
add  Add
-h --help
-person fname,lname,mname,ethn
-loc country,state,city,address,zipcode
-crime description,date
-group name,gtype
-media name,MIME,loc,hashd
-website name,url
-fbu uname,url,uid
-fbp post,url
-fbe name,url,descr,date
-fbg name,url,descr
"""
import docopt
from py2neo import Graph, Node
try:
    graph = Graph(host="localhost", user="neo4j", password="password")
except Exception as e:
    print("Something went wrong loading graph")
    print("Error conneting to graph")
    print(e)


def createPerson(fname,lname,mname,ethn):
    person = Node("Person",fname=fname,lname=lname,mname=mname,ethn=ethn)
    graph.create(person)


def createLoc(country,state,city,address,zipcode):
    loc = Node("Location",country=country,state=state,city=city,address=address,zipcode=zipcode)
    graph.create(loc)

def createCrime(descr,date):
    crime = Node(Crime,descr=descr,date=date)
    graph.create(crime)

def createGroup(name,gtype):
    group = Node(name=name,gtype=gtype)
    graph.create(group)

def createMedia(name,MIME,loc,hashd):
    media = Node(name=name,MIME=MIME,loc=loc,hashd=hashd)
    graph.create(meda)

def createWebsite(name,url):
    web = Node(name=name,url=url)
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

    #do something?
if __name__ == '__main__':
    
    try:
        arguments = docopt.docopt(__doc__)
        args = ''.join(arguments['<args>'])
        args = args.split(',')
        cmd = ''.join(arguments['<cmd>'])
        target = ''.join(arguments['<target>'])
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


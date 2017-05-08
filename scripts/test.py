#import loggerSetup
#import peewee
#from peewee import *
#import configparser
#def log(e):
#   return(loggerSetup.main(3,"CRITICAL",str(e)))
import database_model
from database_model import *
#Load settings and connect to database
#config = configparser.ConfigParser()
#settings = config.read('settings.ini')
#if 'DATABASE' in config:
#    global dbset
#    dbset = config['DATABASE']
#    del configparser
#else:
#    log("Settings File Not Found.")

#mysql_db = peewee.MySQLDatabase(dbset['DBName'],
#                                host=dbset['DBServer'],
#                                user=dbset['DBUser'],
#                                passwd=dbset['DBPass'],
#                                charset='utf8mb4')

class MySQLModel(peewee.Model):
    class Meta:
        database = mysql_db

#class Blog(MySQLModel):
#    creator = peewee.CharField()
#   name = peewee.TextField()

#connect to database    
mysql_db.connect()
#Person.create_table()
#Organization.create_table()
#Events.create_table()
#Crimes.create_table()
#create tables defined in class Blog
#Blog.create_table()

#insert record
#Blog.create(creator='Charlie', name='My Blog')

#Read db
print(Person.get(id=1))

# <__main__.Blog obkect at 0xXXXXXXX>
#Blog.get(id=1).name
#u'My Blog'
try:
    print(Person.get(id=1).FName)
except Exception as e:
    log(e)


#! /usr/bin/python3
import loggerSetup
import peewee
from peewee import *
import database_model
from database_model import *

class MySQLModel(peewee.Model):
    class Meta:
        database = mysql_db()

def createDB():
    import os
    usr = dbset['DBUser']
    pwd = dbset['DBPass']
    db = dbset['DBName']
    os.popen("mysql -u{0} -p{1} -e 'CREATE DATABASE {2};'".format(dbset['DBUser'],dbset['DBPass'],dbset['DBName']))
    main()    
def connect():
    #tests if database exists and is populated; creates and populates if not
    try:        
        mysql_db.connect()
        try:
            create_tables()
        except:
            return(True)
    except:
        createDB()
        create_tables()
        return(True)
        
def create_tables():

    Person.create_table()
    Crimes.create_table()
    Photos.create_table()
    Organization.create_table()
    Archives.create_table()
    Events.create_table()
def main():
    connection = connect()
    print('main')
    
main()

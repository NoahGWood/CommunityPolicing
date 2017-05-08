#! /usr/bin/python3
import loggerSetup
import peewee
from peewee import *
import configparser
def log(e):
    return(loggerSetup.main(3,"CRITICAL",str(e)))
#init db
config = configparser.ConfigParser()
settings = config.read('settings.ini')
if 'DATABASE' in config:
    global dbset
    dbset = config['DATABASE']
    del configparser
else:
    log("Settings File Not Found.")

mysql_db = peewee.MySQLDatabase(dbset['DBName'],
                                host=dbset['DBServer'],
                                user=dbset['DBUser'],
                                passwd=dbset['DBPass'],
                                charset='utf8mb4')
class MySQLModel(peewee.Model):
    class Meta:
        database = mysql_db

class Person(MySQLModel):
    FName = peewee.TextField()
    LName = peewee.TextField()
    Alias = peewee.TextField()
    Address = peewee.TextField()
    Phone = peewee.TextField()
#    Crimes = peewee.ForeignKeyField(Crimes)
    Associates = peewee.TextField()
    Photos = peewee.TextField()
    FileLoc = peewee.TextField()
    Ethnicity = peewee.TextField()
#    Organizations = peewee.ForeignKeyField(Organization)
    State = peewee.TextField()
    City = peewee.TextField()
    Zipcode  = peewee.CharField()

class Organization(MySQLModel):
    Organization = peewee.TextField()
    FileLoc = peewee.TextField()
    Websties = peewee.TextField()
    Status = peewee.TextField()
    Affiliates = peewee.TextField()
#    Members = peewee.ForeignKeyField(Person)
    Donors = peewee.TextField()
    Address = peewee.TextField()
    State = peewee.TextField()
    City = peewee.TextField()
#    Events = peewee.ForeignKeyField(Events)
#    Crimes = peewee.ForeignKeyField(Crimes)
    Nonprofit  = peewee.BooleanField(default=False)

class Events(MySQLModel):
    Event = peewee.TextField()
    Date = peewee.TextField()
#    Crimes = peewee.ForeignKeyField(Crimes)
    FileLoc = peewee.TextField()
    Images = peewee.TextField()
    Videos = peewee.TextField()
    Archives = peewee.TextField()
    State = peewee.TextField()
    City = peewee.TextField()
    Zipcode = peewee.TextField()
#    Organizations = peewee.ForeignKeyField(Organization)

class Crimes(MySQLModel):
    FName = peewee.ForeignKeyField(Person)
    Organization = peewee.ForeignKeyField(Organization)
    Crimes = peewee.TextField()
    Events = peewee.ForeignKeyField(Events)
    Date = DateTimeField()

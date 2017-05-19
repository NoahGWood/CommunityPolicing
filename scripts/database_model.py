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
        
DeferredPerson = DeferredRelation()
DeferredCrimes = DeferredRelation()
DeferredPhotos = DeferredRelation()
DeferredOrganization = DeferredRelation()
DeferredArchives = DeferredRelation()
DeferredEvents = DeferredRelation()

class Person(MySQLModel):
    FName = peewee.TextField()
    LName = peewee.TextField()
    Alias = peewee.TextField()
    Address = peewee.TextField()
    Phone = peewee.TextField()
    Crimes = peewee.ForeignKeyField(DeferredCrimes, null=True)
    Associates = peewee.TextField()
    PPhotos = peewee.ForeignKeyField(DeferredPhotos, null=True)
    Ethnicity = peewee.TextField()
    Organizations = peewee.ForeignKeyField(DeferredOrganization, null=True)
    State = peewee.TextField()
    City = peewee.TextField()
    Zipcode  = peewee.CharField()

class Organization(MySQLModel):
    Organization = peewee.TextField()
    OPhotos = peewee.ForeignKeyField(DeferredPhotos, null=True)
    Archives = ForeignKeyField(DeferredArchives, null=True)
    Websties = peewee.TextField()
    Status = peewee.TextField()
    Affiliates = peewee.TextField()
    Members = peewee.ForeignKeyField(Person)
    Donors = peewee.TextField()
    Address = peewee.TextField()
    State = peewee.TextField()
    City = peewee.TextField()
    Events = peewee.ForeignKeyField(DeferredEvents, null=True)
#    Crimes = peewee.ForeignKeyField(DeferredCrimes, null=True)
    Nonprofit  = peewee.BooleanField(default=False)

class Events(MySQLModel):
    Event = peewee.TextField()
    Date = peewee.TextField()
    Crimes = peewee.ForeignKeyField(DeferredCrimes, null=True)
    EPhotos = peewee.ForeignKeyField(DeferredPhotos)
    Archive = peewee.TextField()
    ArchiveLoc = peewee.TextField()
    State = peewee.TextField()
    City = peewee.TextField()
    Zipcode = peewee.TextField()
    Organizations = peewee.ForeignKeyField(DeferredOrganization, null=True)

class Crimes(MySQLModel):
    Crimes = peewee.TextField()
    Date = DateTimeField()

class Photos(MySQLModel):
    Photo = peewee.TextField()
    FileLoc = peewee.TextField()
    
class Archives(MySQLModel):
    Archives = peewee.TextField()
    ArchiveLoc = peewee.TextField()

DeferredPerson.set_model(Person)
DeferredCrimes.set_model(Crimes)
DeferredPhotos.set_model(Photos)
DeferredOrganization.set_model(Organization)
DeferredArchives.set_model(Archives)
DeferredEvents.set_model(Events)

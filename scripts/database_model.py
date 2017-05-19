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

class Names(MySQLModel):
    idNames = peewee.PrimaryKeyField()
    FirstName = peewee.CharField(45)
    LastName = peewee.CharField(45)
    MiddleName = peewee.CharField(45)
    OrgName = peewee.CharField(45)

class Addresses(MySQLModel):
    idAddress = peewee.PrimaryKeyField()
    Address = peewee.CharField(45)

class Phone(MySQLModel):
    idPhone = peewee.PrimaryKeyField()
    Phone = peewee.IntegerField()

class Websites(MySQLModel):
    idWebsites = peewee.PrimaryKeyField()
    WebsiteURL = peewee.CharField(45)

class Media(MySQLModel):
    idMedia = peewee.PrimaryKeyField()
    MediaDesc = peewee.TextField()
    MediaPath = peewee.CharField(45)
    MediaName = peewee.CharField(45)
    MediaMIME = peewee.CharField(45)

class GroupTypes(MySQLModel):
    idGroupTypes = peewee.PrimaryKeyField()
    GroupType = peewee.CharField(45)
    TypeDescription = peewee.TextField()

class Crimes(MySQLModel):
    idCrimes = peewee.PrimaryKeyField()
    CrimesType = peewee.IntegerField()
    Victims = peewee.CharField(45)
    CrimeDescription = peewee.TextField()
    CrimesMedia = peewee.ForeignKeyField(Media)

class Groups(MySQLModel):
    idGroups = peewee.PrimaryKeyField()
    GroupName = peewee.IntegerField()
    GroupTypeFK = peewee.ForeignKeyField(GroupTypes)
    GroupMission = peewee.TextField()

class GroupMem(MySQLModel):
    idGroupMem = peewee.PrimaryKeyField()
    GroupMember = peewee.ForeignKeyField(Names)
    GroupName = peewee.ForeignKeyField(Names, related+name=)

class Friends(MySQLModel):
    idFriends = peewee.PrimaryKeyField()
    R1 = peewee.ForeignKeyField(Names)
    R2 = peewee.ForeingKeyField(Names)

class Objects(MySQLModel):
    idObjects = peewee.PrimaryKeyField()
    ObjectName = peewee.ForeignKeyField(Names)
    ObjectAddress = peewee.ForeignKeyField(Addresses)
    ObjectPhone = peewee.ForeignKeyField(Phone)
    ObjectCrime = peewee.ForeignKeyField(Crimes)
    ObjectMedia = peewee.ForeignKeyField(Media)
    ObjectWebsites = peewee.ForeingKeyField(Websites)

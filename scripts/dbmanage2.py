import loggerSetup
import peewee
from peewee import *
import database_model
from database_model import *

class MySQLModel(peewee.Model):
    class Meta:
        database = mysql_db

mysql_db.connect()


'''
To display from database use the following:
Person = table
FName = column 
>>> Person.get(Person.id == 1)
<__main__.Blog object at 0x25294d0>

>>> Person.get(Person.id == 1).FName
u'Charlie'

>>> Person.get(Person.FName == 'Charlie')
<__main__.Blog object at 0x2529410>

>>> Person.get(Person.FName == 'nobody')
UserDoesNotExist: instance matching query does not exist:
SQL: SELECT t1."id", t1."FName" FROM "person" AS t1 WHERE t1."FName" = ?
PARAMS: ['nobody']
######
To get all instances use:
for Person in Person.select():
    print Person.FName
'''

#to display from database use:
# Table.get(id=(id to look up).ColumnLable
#e.g. Person.get(id=1).FName
print(Person.get(id=1).FName)
for Person in Person.select():
    print(Person.FName,Person.LName,Person.Alias,Person.Address)

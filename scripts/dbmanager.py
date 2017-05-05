def ReadSettings():
    import configparser
    config = configparser.ConfigParser()
    settings = config.read('settings.ini')
    if 'DATABASE' in config:
        global dbset
        dbset = config['DATABASE']
        del configparser
    else:
        import datetime
        with open('/logs/dbmanager.log', 'w') as log:
            log.write(str(datetime.datetime.now()) + '- Settings File Not Found.')
            Alert("Error: See Logs (CommunityPolicing/logs/dbmanager.log)")

def DBConnection():
    if dbset['DBServer'] not in ['localhost']:
        print("This feature not yet implemented")
    else:
        global command
        command=("mysql -u" + dbset['DBUser'] + " -p" + dbset['DBPass'] + ' ' + dbset['DBName'] + " ")
        print(command)
    
def Import(file):
    return(command + '< ' + file)

def Export(file):
    return(command + '> ' + file)
    
def AddEntry():
    return

def DelEntry():
    return

def Alert(string):
    return(string)

def Run(cmd):
    return

def Main(inputs):
    if '-h' in inputs:
        print('-h help file')
        print('-import database.sql')
        print('-export database.sql')
        print('-add Table,Column,Value')
        print('-delete Table,Row')
        print('Commands seperated by ; ')
        print('Examples:')
        print('-i /path/to/database.sql; -e database.sql; -add Individual,FName,John; -del Individual,John')
    elif '-i' in inputs:
        try:
            inputs = inputs.split(' ',1)[1]
            cmd = Import(inputs)
            print(cmd)
        except:
            pass
    elif '-e' in inputs:
        try:
            inputs = inputs.split(' ',1)[1]
            print('e')
        except:
            pass
    elif '-add' in inputs:
        inputs = ''
        return
    elif '-del' in inputs:
        inputs = ''
        return

ReadSettings()
DBConnection()
i = 1
while i > 0:
    Main(input())
#Main('-e name.sql')

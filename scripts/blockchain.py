#! /usr/bin/python3
import loggerSetup
from Savoir import Savoir

def log(e):
    return(loggerSetup.main('blockchain.py',"CRITICAL",str(e)))

def settings():
    import configparser
    config = configparser.ConfigParser()
    settings = config.read('settings.ini')
    try:
        rpc = config['BLOCKCHAIN']
        del configparser
        for i in rpc:
            print(rpc[i])
        rpcuser = rpc['user']
        rpcpasswd = rpc['passwd']
        rpchost = rpc['host']
        rpcport = rpc['port']
        chainname = rpc['chainname']
        return Savoir.Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)
    except Exception as e:
        log(e)

def Utils(cmd,params,value):
    #getblockchainparams
    if cmd == 'getblockparams':
        blockparams = api.getblockchainparams()
        return(blockparams)
    elif cmd == 'getrunparams':
        #getruntimeparams
        runparams = api.getruntimeparams()
        return(runparams)
    elif cmd == 'setrunparam':
        #setruntimeparams
        try:
            api.setruntimeparam(str(param),value)
        except Exception as e:
            return(e)
    elif cmd == 'getinfo':
        #getinfo
        info = api.getinfo()
        return(info)
    elif cmd == 'stop':
        #stop
        try:
            api.stop()
            stop = True
            return(stop)
        except Exception as e:
            return(e)
    else:
        #help
        apihelp = api.help()
        print(apihelp)
        return(apihelp)

def createStream(name,is_open):
    try:
        api.create('type=stream {0} {1}'.format(name,is_open))
    except Exception as e:
        return(e)

def createFrom(from_address,name,is_open):
    try:
        api.create('{0} type=stream {1} {2}'.format(from_address,name,is_open))

def listStream():
    return(api.liststreams(streams=*))

def publishStream(stream,key,datahex):
    try:
        api.publish('{0} {1} {2}'.format(stream,key,datahex))
    except Exception as e:
        return(e)
def publishFrom(from_address,stream,key,datahex):
    try:
        api.publishfrom('{0} {1} {2} {3}'.format(from_address,stream,key,datahex))
    except Exception as e:
        return(e)
def subscribeStream(asset,stream,rescan):
    if rescan == True:
        try:
            api.subscribe('{0}|{1} rescan=true'.format(asset,stream))
        except Exception as e:
            return(e)
    else:
        try:
            api.subscribe('{0}|{1}'.format(asset,stream))
        except Exception as e:
            return(e)
def unsubscribeStream(asset,stream):
    try:
        api.unsubscribe('{0}|{1}'.format(asset,stream))
    except Exception as e:
        return(e)

def addP2PNode(ip,port,command):
    try:
        api.addnode('{0}(:{1}) {2}'.format(ip,port,command))
    except Exception as e:
        return(e)
    
def networkInfo():
    return(api.getnetworkinfo)

def peerInfo():
    return(api.getpeerinfo)

def ping():
    return(api.ping)

def signMessage(address,message):
    try:
        api.signmessage('{0} {1}'format(address,message))
    except Exception as e:
        return(e)
def verMessage(address,signature,message):
    try:
        api.verifymessage('{0} {1} {2}'.format(address,signature,message))
    except Exception as e:
        return(e)
    
def dump(filename):
    try:
        api.dumpwallet('{0}'.format(filename))
    except Exception as e:
        return(e)

def walletimport(filename):
    try:
        api.importwallet('{0}'.format(filename))
    except Exception as e:
        return(e)

def 


    
def GetStream():
    #Create Multichain Script
    #Export Metadata from Stream
    #Save to /tmp/stream
    #Decode Hex
    #untar
    manifest = CheckManifest()
    dbchk = CheckDB()



def main():
    global api
    api = settings()
    api.getinfo()
    Utils('help',0,0)
main()

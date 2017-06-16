#!/usr/bin/python3
import sys
import logging
import configparser
from Savoir import Savoir

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def blockchain_settings():
    config = configparser.ConfigParser()
    settings = config.read('settings.ini')
    try:
        rpc = config['BLOCKCHAIN']
        rpcuser = rpc['user']
        rpcpasswd = rpc['passwd']
        rpchost = rpc['host']
        rpcport = rpc['port']
        chainname = rpc['chainname']
        return Savoir.Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)
    except Exception as e:
        return("in settings: " + str(e))

def blockchain_utils(cmd,params,value):
    if cmd == 'getblockparams':
        blockparams = api.getblockchainparams()
        return(blockparams)
    elif cmd == 'getrunparams':
        runparams = api.getruntimeparams()
        return(runparams)
    elif cmd == 'setrunparams':
        try:
            api.setruntimeparam(str(param),value)
        except Exception as e:
            return('blockchain utils: ' + str(e))

def create_stream(name,is_open):
    try:
        api.create('type=stream {0} {1}'.format(name,is_open))
    except Exception as e:
        return(e)

def create_from_address(from_address,name,is_open):
    try:
        api.create('{0} type=stream {1} {2}'.format(from_address,name,is_open))
    except Exception as e:
        return(e)

def list_streams():
    return(api.liststreams('streams=*'))

def publish_stream(stream,key,datahex):
    try:
        api.publish('{0} {1} {2}'.format(stream,key,datahex))
    except Exception as e:
        return(e)

def publish_from_address(from_address,stream,key,datahex):
    try:
        api.publishfrom('{0} {1} {2} {3}'.format(from_address,stream,key,datahex))
    except Exception as e:
        return(e)

def subscribe_stream(asset,stream,rescan):
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

def unsubscribe_stream(asset,stream):
    try:
        api.unsubscribe('{0}|{1}'.format(asset,stream))
    except Exception as e:
        return(e)

def add_p2p_node(ip,port,command):
    try:
        api.addnode('{0}(:{1}) {2}'.format(ip,port,command))
    except Exception as e:
        return(e)

def get_network_info():
    return(api.getnetworkinfo)

def get_peer_info():
    return(api.getpeerinfo)

def ping():
    return(api.ping)

def sign_message(address,message):
    try:
        api.signmessage('{0} {1}'.format(address,message))
    except Exception as e:
        return(e)

def verify_message(address,signature,message):
    try:
        api.verifymessage('{0] {1} {2}'.format(address,signature,message))
    except Exception as e:
        return(e)

def dump(walletfile):
    try:
        api.dumpwallet('{0}'.format(walletfile))
    except Exception as e:
        return(e)

def wallet_import(walletfile):
    try:
        api.importwallet('{0}'.format(walletfile))
    except Exception as e:
        return(e)

#def get_stream():

def main(*argv):
    global api
    api = settings()
    if 'help' in argv:
        Utils('help',0,0)

#!/usr/bin/python3
"""DistribCollabOSINT-Blockchain-Manager

Usage:
blockchain utils <cmd> <params> <value>
blockchain create-stream <name> [--from <address> | --open]
blockchain list-streams
blockchain publish-stream <name> <key> <hexstring> [--from <address>]
blockchain subscribe <asset> <stream> --rescan
blockchain unsubscribe <asset> <stream>
blockchain add-node <ip> <port> <command>
blockchain info [--network | --peer]
blockchain ping
blockchain sign <address> <message>
blockchain verify <address> <signature> <message>
blockchain dump <wallet>
blockchain import <wallet>

"""
import docopt
import blockchain2 as block
import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    settings = block.blockchain_settings()
    try:
        args = docopt.docopt(__doc__, version='bchainmanager: 0.0.1')
        if args['utils'] == True:
            try:
                ret = block.blockchain_utils(args['<cmd>'],args['<params>'],['<value>'])
                logger.debug(ret)
            except Exception as e:
                logger.debug(e)
                
        elif args['create-stream'] == True:
            if ['--from'] == False:
                try:
                    block.create_from_address(args['<address>'],args['<name>'],args['<open>'])
                    logger.debug(ret)
                except Exception as e:
                    logger.debug(e)
            else:
                try:
                    block.create_stream(args['<name>'],args['<open>'])
                    logger.debug(ret)
                except Exception as e:
                    logger.debug(e)
        elif args['list-streams'] == True:
            try:
                ret = block.list_streams()
                logger.debug(ret)
            except Exception as e:
                logger.debug(e)
        elif args['list-streams'] == True:
            try:
                ret = block.list_streams()
                logger.debug(ret)
            except Exception as e:
                logger.debug(e)
        elif args['publish-stream'] == True:
            if args['--from'] == True:
                try:
                    ret = block.publish_from_address(args['<address>'], args['<name>'], args['<key>'], args['<hexstring>'])
                    logger.debug(ret) 
                except Exception as e:
                    logger.debug(e)
            elif args['--from'] == False:
                try:
                    ret = block.publish_stream(args['<name>'], args['<key>'], args['<datastring>'])
                    logger.debug(ret)
                except Exception as e:
                    logger.debug(e)
        elif args['subscribe'] == True:
            try:
                ret = block.subscribe_stream(args['<asset>'], args['<stream>'], args['<rescan>'])
                logger.debug(ret)
            except Exception as e:
                logger.debug(e)
        elif args['unsubscribe'] == True:
            try:
                ret = block.unsubscribe_stream(args['<asset>'], args['<stream>'])
                logger.debug(ret)
            except Exception as e:
                logger.debug(e)
        elif args['add-node'] == True:
            try:
                ret = block.add_p2p_node(args['<ip>'], args['<port>'], args['<command>'])
                logger.debug(ret)
            except Exception as e:
                logger.debug(e)
        elif args['info'] == True:
            if args['--network'] == True:
                ret = block.get_network_info()
                logger.debug(ret)
            elif args['--peer'] == True:
                ret = block.get_peer_info()
                logger.debug(ret)
            else:
                args['-help'] == True
        elif args['ping'] == True:
            ret = block.ping()
            logger.debug(ret)
        elif args['sign'] == True:
            try:
                ret = block.sign_message(args['<address>'], args['<message>'])
                logger.debug(ret)
            except Exception as e:
                logger.debug(e)
        elif args['verify'] == True:
            try:
                ret = block.verify_message(args['<address>'], args['<signature>'], args['<message>'])
                logger.debug(ret)
            except Exception as e:
                logger.debug(e)
        elif args['dump'] == True:
            ret = block.dump(args['<wallet>'])
            logger.debug(ret)
        elif args['import'] == True:
            try:
                ret = block.wallet_import(args['<wallet>'])
                logger.debug(ret)
            except Exception as e:
                logger.debug(e)   
                    
    except docopt.DocoptExit as e:
        logger.debug(e)

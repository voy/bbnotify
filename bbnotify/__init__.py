import os
import sys
import gtk
import optparse
import simplejson
from ConfigParser import ConfigParser

from bbnotify.notificator import Notificator
from bbnotify.daemonize import daemonize
from bbnotify.config import parse_config



    

def main():
    usage = """Usage: %prog [options] http://buildboturl/xmlrpc"""
    config = parse_config()
    Notificator(**config)
    if not options.nodaemon:
        daemonize()
    gtk.main()

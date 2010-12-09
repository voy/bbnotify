import gtk

from bbnotify.notificator import Notificator
from bbnotify.daemonize import daemonize
from bbnotify.config import parse_config

def main():
    config = parse_config()
    Notificator(**config)

    if config["daemon"]:
        daemonize()

    gtk.main()

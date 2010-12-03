CONFIG_FILE = os.path.expanduser("~/.bbnotifyrc")

DEFAULT_CONFIG = {
    'url': None,
    'protocol': 'xmlrpc',
    'group': False,
    'ignore_builders': [],
    'include_builders': [],
    'groups': None, # no grouping
}

CONFIG_GROUP_ALL = {
    'all': '*'
}

def get_config_format(config_fp):
    config = config_fp.read().strip()
    config_fp.seek(0)
    if config.startswith('{'):
        return 'json'
    return 'config'
    
    
def parse_config(config, config_fp):
    cp = ConfigParser({'url': "", 'ignore-builders': "", 'include-builders': ""})
    cp.read(config_fp)
    config['url'] = cp.get("bbnotify", "url")
    if cp.get("bbnotify", "ignore-builders"):
        config['ignore_builders'] = config['ignore_builders'].split()
    if cp.get("bbnotify", "include-builders"):
        config['include_builders'] = config['include_builders'].split()
    if cp.get("bbnotify", "protocol"):
        config['protocol'] = cp.get("bbnotify", "protocol")
    if cp.get("bbnotify", "group"):
        config['protocol'] = cp.get("bbnotify", "protocol")
    return config

    
def parse_json(config, config_fp):
    config.update(simplejson.load(config_fp))
    return config


CONFIG_PARSERS = {
    'json': parse_json,
    'config': parse_config,
}

parser = optparse.OptionParser()
parser.add_option("-f", "--forward", dest="nodaemon",
    action="store_true", default=False,
    help="don't run in background")
parser.add_option("-i", "--ignore-builder", dest="ignore_builders",
    metavar="builder_name", action="append", default=[],
    help="don't display the status of this builder")
parser.add_option("-I", "--include-builder", dest="include_builders",
    metavar="builder_name", action="append", default=[],
    help="include only listed builders")
parser.add_option("-p", "--protocol", dest="protocol",
    metavar="[xmlrpc|json]", action="store", default=None,
    help="protocol to use when comunicating with buildbot")
parser.add_option("-g", "--group", dest="group",
    action="store_true", default=False,
    help="group status icons into one")
parser.set_usage("%s\n%s" % (usage, parser.format_option_help()))


def parse_config()
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(CONFIG_FILE):
        config_fp = open(CONFIG_FILE)
        config_format = get_config_format(config_fp)
        config = CONFIG_PARSERS[config_format](config, config_fp)
        config_fp.close()
        
    (options, args) = parser.parse_args()
    for option in ('ignore_builders', 'include_builders', 'protocol', 'group'):
        if getattr(options, option, None):
            config[option] = getattr(options, option)
            
    if len(args) > 0:
        config['url'] = args[0]
    if not config['url']:
        parser.error("Missing url")

    return config


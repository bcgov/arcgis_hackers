# example to list group members

from arcgis import gis
from arcgis.features import FeatureLayer
import logging
import json

title = "ENV - WINS Upgrade project"
secrets = r"H:\secrets\maphub_config.json"


def readConfig(configFile):
    # returns list of parameters 
    # with key 'name'
    """
    reads the config file to dictionary
    """
    logging.debug("Loading config")
    with open(configFile) as json_file:  
        try:
            d = json.load(json_file)

        except:
            print ("failed to parse configuration")
        else:
            return d
    logging.debug("Config Loaded")

sites = readConfig(secrets)
for site in sites:
    if site['name'].lower() == 'bc maphub':
        params = site['params']
mh = gis.GIS(params['mapurl'],params['usr'],params['password'])

groups = mh.groups
for group in groups.search(query=f"title:{title}"):
    members = group.get_members()['users']
    c = 0
    for member in members:
        user = mh.users.get(member)
        logging.info(f"{user.fullName} ({user.username})")


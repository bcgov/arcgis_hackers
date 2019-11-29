#from arcgis.gis import GIS
from arcgis.gis import Group
from arcgis import gis
import datetime
import sys

import logging
import json

secrets = r"H:\secrets\maphub_config.json"

# Makes a time stamp
def makeTimeStamp():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

# this is one method to 
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


ts = makeTimeStamp()
print("Time Stamp: {}".format(ts))


sites = readConfig(secrets)
for site in sites:
    if site['name'].lower() == 'bc maphub':
        params = site['params']
mh = gis.GIS(params['mapurl'],params['usr'],params['password'])
contents = mh.content.search(query="owner:{}".format(params['usr']))
items = []
for item in contents:
    #print (f"Name:{item['name']} Id: {item['id']}")
    items.append(item['id'])

usr_groups = mh.groups.search(query="owner:{}".format(params['usr']))
group_of_interest = mh.groups.search(query="title: " + '"M-KMA 2019 PR Developer"')

for group in group_of_interest:
    print("* {}".format(group.get_members()))

for group in usr_groups:
    print("** {}".format(group.get_members()))











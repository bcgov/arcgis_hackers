from arcgis import gis
import datetime
import logging
import os
import sys

def listItemsByUser(ago, user):
    pass

def listItemsByGroup(ago, group_name=None):
    pass

def listGroupsByOwner(ago, owner=None):
    if owner != None:    
        groups = ago.groups.search(query="owner:{}".format(owner))
        return groups
    else:
        print("No owner id provided")

def listGroupsbyTitle(ago, title = None):
    pass

def getItemProperties(item_id):
    pass

def makeTimeStamp():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

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

def agoSignIn(cred_json):
    sites = readConfig(cred_json)
    for site in sites:
        if site['name'].lower() == 'bc maphub':
            params = site['params']
    ago = gis.GIS(params['mapurl'],params['usr'],params['password'])
    return ago

def getItemsInGroup(ago, group_name = None):
    pass
from arcgis import gis
import logging
import json

secrets = r"H:\secrets\maphub_config.json"

def readConfig(configFile):#returns dictionary of parameters
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
contents = mh.content.search(query="owner:{}".format(params['usr']))
for item in contents:
    print (f"Name:{item['name']} Id: {item['id']}")
from arcgis.gis import GIS
from arcgis.gis import Group
import datetime

def makeTimeStamp():
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

ts = makeTimeStamp()
print(ts)
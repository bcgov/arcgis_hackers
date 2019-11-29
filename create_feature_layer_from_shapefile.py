#This script takes a zipped shapefile and publishes it to AGOL

from arcgis.gis import GIS

#change variables below 
bc_maphub_url = r"https://governmentofbc.maps.arcgis.com"
bc_maphub_username = <username>
bc_maphub_password = <password>

zipped_shp_full_path = <full path to zipped shapefile>
feature_layer_name = <feature layer name>
feature_layer_tags = <tags>

#now run this code

gis = GIS(bc_maphub_url, username=bc_maphub_username, password=bc_maphub_password)

shp_properties = {
    'title': feature_layer_name,
    'tags': feature_layer_tags,
    'type': 'Shapefile'
}

my_shp = gis.content.add(shp_properties, data=zipped_shp_full_path)

my_feature_layer_item = my_shp.publish()

print(my_feature_layer_item.url)

print('published ' + feature_layer_name + ' successfully')

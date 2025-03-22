import folium
import pandas

# You can add more data in the 'oilDeposits.txt' file, just follow the same data structure!
data = pandas.read_csv('oilDeposits.txt')

name = list(data['NAME'])
lat = list(data['LAT'])
lon = list(data['LON'])

#print(list(data['LAT']))


# The data in the location field, defines the coordinates for Venezuela
map = folium.Map(location=[6.4238, -66.589], zoom_start=6, tiles="Cartodb dark_matter")

fg = folium.FeatureGroup(name="My Map")

for nm, lt, ln in zip(name, lat, lon):
    map.add_child(folium.CircleMarker(location=[lt, ln], popup=nm, color='lightgreen', fill_color='green', tooltip=nm))

map.add_child(fg)
map.save("Map1.html")

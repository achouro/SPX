#!/usr/bin/env python
# coding: utf-8

# In[16]:


pip install folium==0.7.0


# In[93]:


import folium
import pandas as pd


# In[94]:


from folium.plugins import MarkerCluster
from folium.features import DivIcon


# In[95]:


from folium.plugins import MousePosition


# In[96]:


URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv'
df=pd.read_csv(URL)
df.head()


# In[97]:


spacex_df = df[['Launch Site', 'Lat', 'Long', 'class']]
launch_sites_df=df[['Launch Site', 'Lat', 'Long']].groupby('Launch Site', as_index=False).first()
launch_sites_df


# In[43]:


nasa_coordinate = [29.559684888503615, -95.0830971930759]

site_map=folium.Map(location=nasa_coordinate, zoom_start=10)

circle=folium.Circle(nasa_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup('NASA Johnson Space Center'))

marker=folium.map.Marker(nasa_coordinate, )

site_map.add_child(circle)
site_map.add_child(marker)


# In[53]:


site_map = folium.Map(location=nasa_coordinate, zoom_start=5)
for ix, row in launch_sites_df.iterrows():
    name = row['Launch Site']
    lat  = row['Lat']
    long = row['Long']
    
    nasa_coordinate=[lat, long]
    circle=folium.Circle(nasa_coordinate, radius=1000, color='#d35400', fill=True).add_child(folium.Popup(name))
    marker=folium.map.Marker(nasa_coordinate,
                             icon=DivIcon(icon_size=(10,10),icon_anchor=(0,0), html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % name, ))
    
    site_map.add_child(circle)
    site_map.add_child(marker)
    

site_map


# In[55]:


spacex_df.tail(10)


# In[57]:


marker_cluster = MarkerCluster()


# In[69]:


def colassign(launch_outcome):
    if launch_outcome==1:
        return "green"
    else:
        return "red"
    
    


spacex_df['marker_color']= spacex_df['class'].apply(colassign)
spacex_df.tail()


# In[76]:


site_map.add_child(marker_cluster)

for ix, row in spacex_df.iterrows():
    name = row['Launch Site']
    lat  = row['Lat']
    long = row['Long']
    col  = row['marker_color']
    
    nasa_coordinate=[lat, long]
    circle=folium.Circle(nasa_coordinate, radius=1000, color=col, fill=True).add_child(folium.Popup(name))
    marker=folium.map.Marker(nasa_coordinate,
                             icon=DivIcon(icon_size=(10,10),icon_anchor=(0,0), html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % name, ))
    
    site_map.add_child(circle)
    site_map.add_child(marker)
    marker_cluster.add_child(marker)
site_map



# In[81]:


import folium
import folium.plugins
from folium.plugins import MousePosition

formatter = "function(num) {return L.Util.formatNum(num, 5);};"
mouse_position = MousePosition(
    position='topright',
    separator=' Long: ',
    empty_string='NaN',
    lng_first=False,
    num_digits=20,
    prefix='Lat:',
    lat_formatter=formatter,
    lng_formatter=formatter,
)

site_map.add_child(mouse_position)
site_map


# In[83]:


from math import sin, cos, sqrt, atan2, radians

def calculate_distance(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


# In[85]:


distance = calculate_distance(28.57468,-80.65229,28.573255 ,-80.646895)
distance


# In[91]:


coordinate = [28.57468,-80.65229]
distance_marker = folium.Marker(
    coordinate,
    icon=DivIcon(
        icon_size=(10,10),
        icon_anchor=(0,0),
        html='<div style="font-size: 12; color:#d35400;"><b>%s</b></div>' % "{:10.2f} KM".format(distance),
    )
)
site_map.add_child(distance_marker)
site_map




# In[92]:


coordinates=[[28.57468,-80.65229],[28.573255 ,-80.646895]]
lines=folium.PolyLine(locations=coordinates, weight=1)
site_map.add_child(lines)

site_map


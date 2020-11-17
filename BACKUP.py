#!/usr/bin/env python
# coding: utf-8

# In[1]:


from arcgis.gis import GIS
from IPython.display import display
from arcgis.geoanalytics import manage_data
from arcgis.features import FeatureLayer
gis = GIS()


# In[2]:



print("ArcGIS Online Org account")    
gis = GIS("https://www.arcgis.com", "USERNAME", "PASSWORD")
print("Logged in as " + str(gis.properties.user.username))


# In[3]:


items = gis.content.search(query="owner:" + gis.users.me.username, 
                                item_type="Feature Layer", 
                                max_items=100)

items


# In[ ]:



for item in items:
    try:
        service_title = item.title
        version = "1"
        fgdb_title = service_title+version
        result = item.export(fgdb_title, "File Geodatabase")
        result.download(r'O:\BACKUP')
        result.delete()
    except:
        print("An error occurred downloading"+" "+service_title)


# In[ ]:



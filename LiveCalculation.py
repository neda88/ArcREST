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
gis = GIS("https://www.arcgis.com", "username", "password")
print("Logged in as " + str(gis.properties.user.username))


# In[3]:


search_results = gis.content.search('title: Date_Calculation',
                                    'Feature Layer')
Date_Calculation_item = search_results[0]
Date_Calculation_item


# In[4]:


Date_Calculation_layers = Date_Calculation_item.layers
Date_Calculation_layers


# In[5]:


from arcgis.features import FeatureLayer
feature_layer = Date_Calculation_layers[0]
feature_layer


# In[6]:


for f in feature_layer.properties.fields:
    print(f['name'])


# In[7]:


feature_layer.calculate(where= "1=1",calc_expression={"field": "LiveCal", "sqlExpression": "Shape__Area_2*Cost"})


# In[ ]:





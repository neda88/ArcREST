#!/usr/bin/env python
# coding: utf-8

# In[3]:


from arcgis.gis import GIS
gis = GIS("url", "username", "password")


# In[4]:


gis.users


# In[5]:


org_users = gis.users.search()
print(f'{len(org_users)} users found')
org_users


# In[46]:


my_content = gis.content.search(query="owner:" + gis.users.me.username, 
                                item_type="Web Map", 
                                max_items=15)

my_content


# In[45]:


my_content_Neda = gis.content.search(query="owner:xxx", 
                                item_type="Web Map", 
                                max_items=15)

my_content_Neda


# In[77]:


Item_users = gis.content.search(query="owner:xxx", item_type="Dashboard", max_items=1000)
print(f'{len(Item_users)} content found')
Item_users


# In[62]:


items = gis.content.search(query='type:map AND owner:' + gis.users.me.username,
                           max_items=1000)
items


# In[75]:


item_list = gis.content.search(query='type:* AND owner:*' ,
                           max_items=2000)
item_list


# In[ ]:





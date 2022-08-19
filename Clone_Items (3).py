#!/usr/bin/env python
# coding: utf-8

# In[98]:


from arcgis.gis import GIS
from IPython.display import display
from getpass import getpass


# In[99]:


source = GIS("url", "username", "password")
target = GIS("url", "username", "password")
target_admin_username = 'username'


# In[100]:


print(source)
print(target)


# In[78]:


sou_users = source.users.search()
for user in sou_users:
    print(user.username + "-" + str(user.role))


# In[79]:


tar_users = source.users.search()
for user in tar_users:
    print(user.username + "-" + str(user.role))


# In[80]:


sourceuser ="portaladmin"


# In[81]:


print(sourceuser)


# In[86]:


sourceuser ="portaladmin"
user = source.users.get(sourceuser)
items = user.items()
for item in items:
    print("\t{} : {} : {}".format(item.title,item.type,item.id))
    
folders = user.folders
for fld in folders:
        flditems = user.items(fld['title'])
        print("-->" + fld['title'])
        for item in flditems:
            print("\t{} : {} :{}".format(item.title,item.type, item.id))


# In[87]:


get_ipython().run_line_magic('pinfo', 'target.content.clone_items')


# In[105]:


webmap = source.content.get("a9d0e89131a44d4bae7f7ac4040c42b6")
webmap


# In[102]:


webmap.url


# In[106]:


cloned_items = target.content.clone_items(items=[webmap], owner = "portaladmin", copy_data = True)


# In[108]:


display(cloned_items)


# In[109]:


hosted_flyr = source.content.get("1cb7dfa326974f85be237e04a934f948")
hosted_flyr


# In[110]:


hosted_flyr.url


# In[111]:


cloned_flyr = target.content.clone_items(items=[hosted_flyr],
                                        owner="portaladmin", copy_data=True)


# In[112]:


cloned_flyr=target.content.search(query="title:xxx")
display(cloned_flyr)


# In[131]:


noc = source.content.search(query="title:xxx", max_items=100)
for n in noc:
    print("\t{} : {} :{}".format(n.title,n.type, n.id))
            


# In[133]:


NomenclatureWebMap1 = source.content.get("ebdbd07440f04cfc80131121295ead6e")
NomenclatureWebMap1


# In[134]:


cloned_webmap = target.content.clone_items(items=[NomenclatureWebMap1],
                                        owner="portaladmin", copy_data=True)


# In[135]:


display(cloned_webmap)


# In[136]:


NomenclatureWebMap2 = source.content.get("4cc2356645cc48bb878c08f3224ea9ca")
NomenclatureWebMap2


# In[138]:


cloned_webmap2 = target.content.clone_items(items=[NomenclatureWebMap2],
                                        owner="portaladmin", copy_data=True)
display(cloned_webmap2)


# In[141]:


NomenclatureWebMapFinder = source.content.get("522a847913544d9ca5133ad1ba13750c")
NomenclatureWebMapFinder


# In[142]:


cloned_webmapfinder = target.content.clone_items(items=[NomenclatureWebMapFinder],
                                        owner="portaladmin", copy_data=True)
display(cloned_webmapfinder)


# In[143]:


dash = source.content.get("09ec40b8a6af47a39e0059adafd4e488")
dash


# In[149]:


cloned_dash=target.content.clone_items(items=[dash],
                                        owner="portaladmin", copy_data=True)


# In[147]:


display(cloned_dash)


# In[ ]:





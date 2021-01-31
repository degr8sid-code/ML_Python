#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
url = "https://www.metaweather.com/api/location/search/?query=san"
response = requests.get(url)
print(response.text)


# In[3]:


response = requests.post(url)
print(response.text)


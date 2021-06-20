#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get("http://en.wikipedia.org/wiki/Main_Page")
page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[9]:


first_header=soup.find('h2',class_="mp-h2")
first_header


# In[11]:


first_header.text


# In[13]:


headers=soup.find_all('h2',class_="mp-h2")
headers


# In[15]:


first_header=[]
for i in headers:
    first_header.append(i.text)
first_header


# In[18]:


import pandas as pd
headers=pd.DataFrame({})
headers['all_headers']=first_header
headers


# In[ ]:





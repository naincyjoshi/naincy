#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting")
page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[6]:


Women_player=soup.find('td',class_="table-body__cell rankings-table__name name")
Women_player


# In[7]:


Women_player.text


# In[8]:


Womenplayer=soup.find_all('td',class_="table-body__cell rankings-table__name name")
Womenplayer


# In[9]:


Women_player=[]
for i in Womenplayer:
    Women_player.append(i.text.replace("\n",""))
Women_player


# In[11]:


country_name=soup.find('span',class_="table-body__logo-text")
country_name


# In[12]:


Team=soup.find_all('span',class_="table-body__logo-text")
Team


# In[16]:


country_name=[]
for i in Team:
    country_name.append(i.text)
country_name

    


# In[13]:


rating_=soup.find('td',class_="table-body__cell rating")
rating_


# In[14]:


rating=soup.find_all('td',class_="table-body__cell rating")
rating


# In[18]:


rating_=[]
for i in rating:
        rating_.append(i.text)
rating_


# In[20]:


import pandas as pd
cricket=pd.DataFrame({})
cricket['player']=Women_player
cricket['Team']=country_name
cricket['Rating']=rating_
cricket.head(10)


# In[ ]:





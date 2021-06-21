#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


from bs4 import BeautifulSoup
import requests


# In[4]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
page


# In[5]:


soup=BeautifulSoup(page.content)
soup


# In[6]:


Bowler_player_name=soup.find('div',class_="rankings-block__banner--name-large")
Bowler_player_name


# In[10]:


Bowler_name=soup.find_all('td',class_="table-body__cell rankings-table__name name")
Bowler_name


# In[11]:


Bowlerplayer=[]
Bowlerplayer.append(Bowler_player_name.text.strip())
for i in Bowler_name:
    Bowlerplayer.append(i.text.replace("\n",""))
Bowlerplayer


# In[13]:


country_name=soup.find('div',class_="rankings-block__banner--nationality")
country_name


# In[15]:


Teams=soup.find_all('span',class_="table-body__logo-text")
Teams


# In[16]:


countryname=[]
countryname.append(country_name.text.strip())
for i in Teams:
    countryname.append(i.text)
countryname


# In[17]:


R1=soup.find('div',class_="rankings-block__banner--rating")
R1


# In[18]:


rating=soup.find_all('td',class_="table-body__cell rating")
rating


# In[20]:


ratings_=[]
ratings_.append(R1.text.strip())
for i in rating:
    ratings_.append(i.text)
ratings_


# In[93]:


len(Bowler_player_name)


# In[21]:


import pandas as pd
cricket=pd.DataFrame({})
cricket['Bowlerplayer']=Bowlerplayer
cricket['Teams']=countryname
cricket['ratings']=ratings_
cricket.head(10)


# In[ ]:





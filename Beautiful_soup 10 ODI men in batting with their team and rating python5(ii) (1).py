#!/usr/bin/env python
# coding: utf-8

# In[2]:



get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


from bs4 import BeautifulSoup
import requests


# In[4]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi")
page


# In[5]:


soup=BeautifulSoup(page.content)
soup


# In[6]:


player_name=soup.find('td',class_="table-body__cell name")
player_name


# In[7]:


player_name.text


# In[8]:


player=soup.find_all('td',class_="table-body__cell name")
player


# In[9]:


firstbatsman=soup.find('div',class_="rankings-block__banner--name")
firstbatsman.text


# In[11]:


player_name=[]
player_name.append(firstbatsman.text.strip())
for i in player:
    
    player_name.append(i.text.replace("\n",""))
    
player_name


# In[23]:


team=soup.find_all('span',class_='table-body__logo-text')
team


# In[24]:


countryname=soup.find('div',class_="rankings-block__banner--nationality")
countryname=countryname.text.strip().replace("\n","").split(' ')[0]
countryname


# In[25]:


team_=[]
team_.append(countryname)
for i in team:
    team_.append(i.text.replace("\n",""))
team_


# In[29]:


rating_=soup.find('div',class_="rankings-block__banner--nationality")
rating_=rating_.text.strip().replace("\n","").split(' ')[-1]
rating_


# In[30]:


rating=soup.find_all('td',class_="table-body__cell u-text-right rating")
rating


# In[32]:


rating_Batting=[]
rating_Batting.append(rating_)
for i in rating:
    rating_Batting.append(i.text.replace("\n",""))
rating_Batting


# In[33]:


import pandas as pd
cricket=pd.DataFrame({})
cricket['player']=player_name
cricket['team']=team_
cricket['rating']=rating_Batting
cricket.head(10)


# In[ ]:





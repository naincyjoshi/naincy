#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")
page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[5]:


Women_allrounder=soup.find('div',class_="rankings-block__banner--name-large")
Women_allrounder


# In[7]:


Womenallrounder=soup.find_all('td',class_="table-body__cell rankings-table__name name")
Womenallrounder


# In[8]:


Women_all_rounder=[]
Women_all_rounder.append(Women_allrounder.text.strip())
for i in Womenallrounder:
    Women_all_rounder.append(i.text.replace("\n",""))
Women_all_rounder


# In[9]:


Rating_=soup.find('div',class_="rankings-block__banner--rating")
Rating_


# In[10]:


rating=soup.find_all('td',class_="table-body__cell rating")
rating


# In[11]:


ratings=[]
ratings.append(Rating_.text.strip())
for i in rating:
    ratings.append(i.text)
ratings
    


# In[12]:


Team_=soup.find('div',class_="rankings-block__banner--nationality")
Team_


# In[13]:


Team=soup.find_all('td',class_="table-body__cell nationality-logo rankings-table__team")
Team


# In[16]:


Teams=[]
Teams.append(Team_.text.strip())
for i in Team:
    Teams.append(i.text.replace("\n",""))
Teams


# In[17]:


import pandas as pd
cricket=pd.DataFrame({})
cricket['Women Allrounder']=Women_all_rounder
cricket['Teams']=Teams
cricket['Ratings']=ratings
cricket.head(10)


# In[ ]:






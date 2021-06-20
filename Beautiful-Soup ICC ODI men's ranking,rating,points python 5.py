#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[6]:


ICC_ranking=soup.find('td',class_="rankings-block__banner--team-name")
ICC_ranking


# In[8]:


ranking=soup.find_all('td',class_="table-body__cell rankings-table__team")
ranking


# In[12]:


ODIranking=[]
ODIranking.append(ICC_ranking.text.strip())
for i in ranking:
    ODIranking.append(i.text.replace("\n",""))
ODIranking


# In[13]:


matchbanner=soup.find('td',class_="rankings-block__banner--matches")
matchbanner


# In[29]:


points_=soup.find('td',class_="rankings-block__banner--points")
points_


# In[14]:


matches=soup.find_all('tr',class_="table-body")
matches


# In[30]:


matches_ = []
matches_.append(matchbanner.text.strip())
points=[]
points.append(points_.text.strip())
for i in matches:
    matches_.append(i.find_all('td',class_="table-body__cell u-center-text")[0].text.strip())
    points.append(i.find_all('td',class_="table-body__cell u-center-text")[1].text.strip())


# In[28]:



matches_


# In[31]:


points


# In[32]:


rating=soup.find('td',class_="rankings-block__banner--points")
rating


# In[33]:


ratings=soup.find_all('td',class_="table-body__cell u-text-right rating")
ratings


# In[35]:


ratings_=[]
ratings_.append(rating.text.strip())
for i in ratings:
    ratings_.append(i.text.replace("\n",""))
ratings_


# In[36]:


import pandas as pd
cricket=pd.DataFrame({})
cricket['Teams']=ODIranking
cricket['Matches']=matches_
cricket['Points']=points
cricket['Ratings']=ratings_
cricket.head(10)


# In[ ]:





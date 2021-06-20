#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[46]:


Women_player=soup.find('td',class_="rankings-block__banner--team-name")
#Women_player=Women_player.text.strip().replace("\n","").split(' ')
Women_player


# In[47]:


WomenPlayer=soup.find_all('td',class_="table-body__cell rankings-table__team")

WomenPlayer


# In[48]:


player=[]
player.append(Women_player.text.strip())
for i in WomenPlayer:
    player.append(i.text.replace("\n",""))
player


# In[40]:


Match=soup.find('td',class_="rankings-block__banner--matches")
#Match=Match.text.strip().replace("\n","").split(' ')
Match


# In[41]:


point=soup.find('td',class_="rankings-block__banner--points")
#point=point.text.strip().replace("\n","").split(' ')
point


# In[16]:


matches=soup.find_all('tr',class_="table-body")
matches


# In[42]:


matches_=[]
matches_.append(Match.text.strip())
points=[]
points.append(point.text.strip())

for i in matches:
    matches_.append(i.find_all('td',class_="table-body__cell u-center-text")[0].text.strip())
    points.append(i.find_all('td',class_="table-body__cell u-center-text")[1].text.strip())
        


# In[43]:


matches_


# In[44]:


points


# In[27]:


rating=soup.find('td',class_="rankings-block__banner--rating u-text-right")
rating


# In[28]:


ratings=soup.find_all('td',class_="table-body__cell u-text-right rating")
ratings


# In[31]:


ratings_=[]
ratings_.append(rating.text.strip())
for i in ratings:
    ratings_.append(i.text.replace("\n",""))
ratings_


# In[49]:


import pandas as pd
Women_ranking=pd.DataFrame({})
Women_ranking['Player']=player
Women_ranking['Matches']=matches_
Women_ranking['Points']=points
Women_ranking['Rating']=ratings_
Women_ranking


# In[ ]:





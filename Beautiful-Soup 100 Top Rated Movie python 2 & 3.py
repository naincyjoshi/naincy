#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get("https://www.imdb.com/list/ls056092300/")
page


# In[4]:


page.content


# In[5]:


soup=BeautifulSoup(page.content)
soup


# In[6]:


movie_title=soup.find('h3',class_="lister-item-header")

movie_title


# In[7]:


movie_title.text


# In[8]:


movie_title.text.replace('\n','')


# In[9]:


titles=soup.find_all('h3',class_="lister-item-header")
titles


# In[10]:


movie_title=[]
for i in titles:
    movie_title.append(i.text.replace("\n",""))
movie_title


# In[14]:


star_rating=soup.find_all('div',class_="ipl-rating-widget")
star_rating                  


# In[20]:


starrating=[]
for i in star_rating:
    starrating.append(i.find_all('span',class_="ipl-rating-star__rating")[0].text.strip())
starrating


# In[21]:


import pandas as pd
index=pd.DataFrame({})
index['MOVIE Name and Release YEAR']=movie_title
index['rating']=starrating
index


# In[ ]:





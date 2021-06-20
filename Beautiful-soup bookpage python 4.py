#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get("https://bookpage.com/")
page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[6]:


import pandas as pd
raw_data={'Book Name':['Act Your AGE,Eve Brown','Dusk,Night,Dawn','The Natural Mother Of Child','In','The Hidden Palace'],
         'Author Name':['Talia Hebert','Anne lamotte','Krys Malcom Belc','Will McPhail','Helele wecker'],
         'Genere':['Contemporary Romantic','NonFiction','NonFiction','Graphic Novel','Fiction'],
         'Book Review':['Narrator Ione Butler goes straight for the heart—but never loses the humor—in her rendition of Talia Hibbert’s latest rom-com','Anne Lamott’s narration of Dusk, Night, Dawn is the soundtrack for feeling better in the midst of a troubled landscape','Krys Malcolm Belc’s growing realization that he identified as male happened as his wife bore children and as Belc decided to carry a child as well.','Small talk becomes real talk in Will McPhail’s graphic novel, and the world suddenly seems all that much brighter.','Fans have waited eight years for this sequel, a minor eternity perfectly in keeping with the precarious immortality of Helene Wecker’s hopeful monsters.']}
df=pd.DataFrame(raw_data,columns=['Book Name','Author Name','Genere','Book Review'])
df


# In[ ]:





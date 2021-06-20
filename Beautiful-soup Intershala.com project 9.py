#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get("https://internshala.com/fresher-jobs")
page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[5]:


print(soup.prettify())


# In[6]:


Job_title=soup.find('div',class_="heading_4_5 profile")
Job_title


# In[7]:


Job_title.text


# In[8]:


Jobtitle=soup.find_all('div',class_="heading_4_5 profile")
Jobtitle


# In[9]:


Job_title=[]
for i in Jobtitle:
    Job_title.append(i.text.replace("\n",""))
Job_title


# In[10]:


company_name=soup.find('div',class_="heading_6 company_name")
company_name


# In[11]:


company_name.text


# In[12]:


companyname=soup.find_all('div',class_="heading_6 company_name")
companyname


# In[44]:


company_name=[]
for i in companyname:
    company_name.append(i.text.replace("\n",""))
company_name


# In[26]:


CTC_=soup.find_all('div',class_="internship_other_details_container")
CTC_


# In[40]:


CTC = []
APPLY_DATE=[]
for i in CTC_:
    CTC.append(i.find_all('div',class_="item_body")[1].text.strip())
    APPLY_DATE.append(i.find_all('div',class_="item_body")[2].text.strip())


# In[42]:


CTC


# In[38]:


APPLY_DATE


# In[39]:


CTC


# In[45]:


import pandas as pd
internshala=pd.DataFrame({})
internshala['jobtitle']=Job_title
internshala['companyName']=company_name
internshala['CTC']=CTC
internshala['Apply date']=APPLY_DATE
internshala


# In[ ]:





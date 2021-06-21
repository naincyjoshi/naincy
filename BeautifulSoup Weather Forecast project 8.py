#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get("https://forecast.weather.gov/MapClick.php?textField1=37.78&textField2=-122.42#.YM8q6r4zbIU")
page


# In[4]:


soup=BeautifulSoup(page.content)
soup


# In[18]:


forecast=soup.find_all('div',class_="row row-odd row-forecast")
forecast


# In[27]:


period_name=[]
short_desc=[]
for i in forecast:
     period_name.append(i.find_all('div',class_="col-sm-2 forecast-label")[0].text.strip())
        #short_desc.append(i.find_all('div',class_="col-sm-10 forecast-text")[0].text.strip())
     #templow_.append(i.find_all('p',class_="temp temp-low")[3].text.strip())
    


# In[20]:


period_name


# In[30]:


short_desc=[]
for i in forecast:
    short_desc.append(i.find_all('div',class_="col-sm-10 forecast-text")[-1].text.strip())


# In[31]:


short_desc


# In[34]:


import pandas as pd
Forecast_=pd.DataFrame({})
Forecast_['Period Name']=period_name
Forecast_['short Desc with Temp']=short_desc
Forecast_


# In[ ]:





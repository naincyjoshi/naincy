#!/usr/bin/env python
# coding: utf-8

# In[35]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[36]:


from bs4 import BeautifulSoup
import requests


# In[40]:


page=requests.get("https://www.amazon.in/s?i=electronics&bbn=1389401031&rh=n%3A1389401031%2Cp_36%3A1318506031&dc&qid=1624182524&ref=sr_ex_p_89")
page


# In[41]:


soup=BeautifulSoup(page.content)
soup


# In[42]:


mobile_name=soup.find_all('h2',class_="a-size-mini a-spacing-none a-color-base s-line-clamp-4")
mobile_name


# In[43]:


productname=[]
for i in mobile_name:
    productname.append(i.text.replace("\n",""))
productname


# In[44]:


review=soup.find_all('div',class_="a-row a-size-small")
review


# In[45]:


review_=[]
for i in review:
    review_.append(i.text.replace("\n",""))
review_


# In[59]:


url=soup.find_all('div',class_="a-section aok-relative s-image-square-aspect")
url


# In[61]:


import re
images = soup.find_all('img', {'src':re.compile('.jpg')})

for image in images: 
    (print(image['src']+'\n',""))


# In[68]:


price=soup.find_all('span',class_="a-price-whole")
price


# In[69]:


price_=[]
for i in price:
    price_.append(i.text.replace("\n",""))
price_


# In[ ]:





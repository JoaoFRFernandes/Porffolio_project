#!/usr/bin/env python
# coding: utf-8

# In[32]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[34]:


def extract(page):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    url= f'https://ca.myprotein.com/nutrition/bestsellers-en-us.list?pageNumber={page}'
    r= requests.get(url, headers) # starting to get data from myprotein website
    soup= BeautifulSoup(r.content,'html.parser') # pull html from the website
    return soup
objectlist=[]
def transform(soup):
    page= soup.find_all('div', class_='athenaProductBlock')
    for each in page:
        Title= each.find('h3', class_='athenaProductBlock_productName')
        try:
            price = each.find('span',class_='athenaProductBlock_fromValue').get_text().strip()
        except:
            price='TBA'
        try:
            saving = each.find('span',class_='athenaProductBlock_saveValue').get_text().strip() 
        except:
            saving='NP'
        Title=BeautifulSoup(Title.prettify(), 'html.parser').text.strip()
        try:
            star = each.find('span',class_='visually-hidden athenaProductBlock_rating_hiddenLabel').get_text()
        except:
            star='NP'
       
        object = {'Title': Title,
                 'price': price,
                 'saving up to': saving,
                 'star': star}
        objectlist.append(object)
    return
for i in range(0,4):
    print(f'Getting page {i}')
    c= extract(i)
    transform(c) 


# In[31]:


df = pd.DataFrame(objectlist)
print(df.head())
df.to_csv('Suplement.csv')


# In[ ]:





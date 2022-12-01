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
    page= soup.find_all('div', class_='athenaProductBlock')# find Xpath for the obejcts 
    for each in page:# do a cycle in order to retreive all the objects in the page with the Xpath
        Title= each.find('h3', class_='athenaProductBlock_productName') # in this case Title of the projecy
        try:# in this case we need to go a try since not all html path is the same
            price = each.find('span',class_='athenaProductBlock_fromValue').get_text().strip()#get text from the string and delete the tab from the format
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
       
        object = {'Title': Title, # put all the gotten information into one table to be easier to read it
                 'price': price,
                 'saving up to': saving,
                 'star': star}
        objectlist.append(object) # add the table into the list objectlist
    return
for i in range(0,4):# get all the information from all pages(loading script)
    print(f'Getting page {i}')
    c= extract(i)
    transform(c) 


# In[31]:


df = pd.DataFrame(objectlist)#pandas library give us the chance to format the list into rows and columns to be easier to put into CSV file
print(df.head())# print the frist 5 lines to see if the content is correct
df.to_csv('Suplement.csv')# transform and put the data into the CSV file


# In[ ]:





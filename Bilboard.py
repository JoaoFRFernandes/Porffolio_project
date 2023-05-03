#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import etree
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re


# In[25]:


def extract(year):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    url= f'https://www.billboard.com/charts/hot-100/{year}-02-14'
    r= requests.get(url, headers) # starting to get data from bilboard website
    soup= BeautifulSoup(r.content,'html.parser') # pull html from the website
    return soup
objectlist2=[]
def transform(soup):
    page= soup.find_all('li', class_="lrv-u-width-100p")
    Count=1
    for each in page:# do a cycle in order to retreive all the objects in the page with the Xpath   
        if Count>10:
            break
        try:
            Title= each.find('h3', id='title-of-a-story')
            TitleTEXT=BeautifulSoup(Title.prettify(), 'html.parser').get_text()
            Count +=1       
        except:
                pass         
        try:
            Artist=Title.findNext('span').get_text()
            object2={'Title': TitleTEXT,
            'Artist':Artist,
                    'Year':i}
            objectlist2.append(object2) 
        except:
            pass
Year=[]
objectlist=[]  
for i in range(1988,1999):# get all the information from all pages
  print(f'Getting year {i}\n')
  c= extract(i)
  object1={'Year':int(i)}
  objectlist.append(object1)
  Year.append(i)
  transform(c)


# In[26]:


for i in objectlist2:
    a=i['Title'].strip()
    b=i['Artist'].strip()
    c=i['Year']
    print(a,' ',b, c)


# In[27]:


songs_1970 = []
songs_1980 = []
songs_1990 = []
songs_2000 = []
songs_2010 = []

def extract(Title):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel M"ac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    url = f"https://www.google.com/search?q=lyrics {Title}"
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup, title):
    try:
        page = soup.find('div', class_ ="hwc").text
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(page)
        if sentiment['compound'] > 0:
            return (title, "Positive")
        else:
            return (title, "Negative")
    except:
        return None

for i in objectlist2:
    year = i["Year"]
    decade = int(year / 10) * 10
    title = i["Title"]
    a = title.strip()
    soup = extract(a)
    song_tuple = transform(soup, title)
    if song_tuple: 
        if decade == 1970:
            object5={'Title': song_tuple[0],
            'happy':song_tuple[1]}
            songs_1970.append(object5)
        
        if decade == 1980:
            object6={'Title': song_tuple[0],
            'happy':song_tuple[1]}
            songs_1980.append(object6)
        if decade == 1990:
            object7={'Title': song_tuple[0],
            'happy':song_tuple[1]}
            songs_1990.append(object7)
        if decade == 2000:
            object8={'Title': song_tuple[0],
            'happy':song_tuple[1]}
            songs_2000.append(object8)
        if decade == 2010:
            object9={'Title': song_tuple[0],
            'happy':song_tuple[1]}
            songs_2010.append(object9)
            


# In[19]:


print("70's")
for i in songs_1970:
    a=i['Title'].strip()
    b=i['happy'].strip()
    print(a,' ',b)

print("80's")
for i in songs_1980:
    a=i['Title'].strip()
    b=i['happy'].strip()
    print(a,' ',b)
    
print("90's")
for i in songs_1990:
    a=i['Title'].strip()
    b=i['happy'].strip()
    print(a,' ',b)

print("2000's")
for i in songs_2000:
    a=i['Title'].strip()
    b=i['happy'].strip()
    print(a,' ',b)
print("2010's")

for i in songs_2010:
    a=i['Title'].strip()
    b=i['happy'].strip()
    print(a,' ',b)


# In[20]:


import csv


# In[28]:


import pandas as pd

# Create a data frame from each of the songs lists
df_1970 = pd.DataFrame(songs_1970)
df_1980 = pd.DataFrame(songs_1980)
df_1990 = pd.DataFrame(songs_1990)
df_2000 = pd.DataFrame(songs_2000)
df_2010 = pd.DataFrame(songs_2010)

# Write each data frame to a separate sheet in an Excel file
with pd.ExcelWriter('songs.xlsx') as writer:
    df_1970.to_excel(writer, sheet_name='1970s')
    df_1980.to_excel(writer, sheet_name='1980s')
    df_1990.to_excel(writer, sheet_name='1990s')
    df_2000.to_excel(writer, sheet_name='2000s')
    df_2010.to_excel(writer, sheet_name='2010s')


# In[22]:


def extract(Title):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel M"ac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    url= f"https://www.google.com/search?q=lyrics{a}"
    r= requests.get(url, headers)# starting to get data from bilboard website
    soup= BeautifulSoup(r.content,'html.parser')# pull html from the website
    return soup
musiclist=[]
def transform(soup, year):
    try:
        page = soup.find('div', class_ ="hwc").text
        object11={'Lyrics': page,
            'Year':year}
        musiclist.append(object11)
    except:
        return

for i in objectlist2:
    year = i["Year"]
    title = i["Title"]
    a = title.strip()
    soup = extract(a)
    song_tuple = transform(soup, year)


    


# In[23]:



love_words1 = ['love', 'affection', 'devotion', 'passion', 'desire', 'romance', 'intimacy', 'happiness', 'joy', 'bliss', 'togetherness', 'unity', 'partnership', 'falling', 'fall', 'forever', 'adoration', 'cherish', 'adore']
breakup_words1 = ['heartbreak', 'Broke','heart', 'pain', 'alone', 'hearted', 'sorrow', 'loss', 'goodbye', 'farewell', 'betrayal', 'hurt', 'disappointment', 'loneliness', 'emptiness', 'solitude', 'regret', 'guilt', 'blame', 'moving on', 'died', 'healing', 'recovery', 'cry', 'cried', 'anger', 'frustration', 'bitterness', 'tears', 'devastation']
word_count_love1 = {}
word_count_breakup1 = {}
love_word_patterns1 = [re.compile(r'\b' + word + r'\b') for word in love_words1]
breakup_word_patterns1 = [re.compile(r'\b' + word + r'\b') for word in breakup_words1]

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

classifications1 = []

for song in musiclist:
    lyrics1 = song["Lyrics"]
    words1 = remove_punctuation(lyrics1).split()
    love_score1 = 0
    breakup_score1 = 0
    for word in words1:
        for pattern in love_word_patterns1:
            if pattern.search(word):
                if word in word_count_love1:
                    word_count_love1[word] += 1
                    love_score1 += word_count_love1[word]
                else:
                    word_count_love1[word] = 1
        for pattern in breakup_word_patterns1:
            if pattern.search(word):
                if word in word_count_breakup1:
                    word_count_breakup1[word] += 1
                    breakup_score1 += word_count_breakup1[word]
                else:
                    word_count_breakup1[word] = 1
    if love_score1 > breakup_score1:
        classifications1.append("Love")
    elif breakup_score1 > love_score1:
        classifications1.append("Breakup")
    else:
        classifications1.append("Neutral")

sorted_word_count_love1 = sorted(word_count_love1.items(), key=lambda x: x[1], reverse=True)
sorted_word_count_breakup1 = sorted(word_count_breakup1.items(), key=lambda x: x[1], reverse=True)
love_count = classifications1.count("Love")
Breakup_count = classifications1.count("Breakup")
Neutral_count=classifications1.count("Neutral")
print(sorted_word_count_love1)
print(sorted_word_count_breakup1)
print(classifications1)
print("Music:")
print("Love",love_count)
print("SAD/Breakup",Breakup_count)
print("Neutral",Neutral_count)




# In[24]:


import csv


with open("music_classifications.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Variable", "Value"])
    writer.writerow(["Calssifications", Clas])
    writer.writerow(["Love Count", love_count])
    writer.writerow(["Breakup Count", Breakup_count])
    writer.writerow(["Neutral Count", Neutral_count])
    writer.writerow(["Sorted Word Count Love", sorted_word_count_love1])
    writer.writerow(["Sorted Word Count Breakup", sorted_word_count_breakup1])


# In[ ]:


df_1970 = pd.DataFrame(classifications1)

with pd.ExcelWriter('songs3.xlsx') as writer:
    df_1970.to_excel(writer, sheet_name='1980s')


# In[25]:


word_count_love_by_year = {}
word_count_breakup_by_year = {}

for song in musiclist:
    lyrics = song["Lyrics"]
    year = song["Year"]
    words = remove_punctuation(lyrics).split()
    love_score = 0
    breakup_score = 0
    for word in words:
        for pattern in love_word_patterns1:
            if pattern.search(word):
                if word in word_count_love1:
                    word_count_love1[word] += 1
                if year not in word_count_love_by_year:
                    word_count_love_by_year[year] = {}
                if word in word_count_love_by_year[year]:
                    word_count_love_by_year[year][word] += 1
                    love_score += word_count_love_by_year[year][word]
                else:
                    word_count_love_by_year[year][word] = 1
        for pattern in breakup_word_patterns1:
            if pattern.search(word):
                if word in word_count_breakup1:
                    word_count_breakup1[word] += 1
                if year not in word_count_breakup_by_year:
                    word_count_breakup_by_year[year] = {}
                if word in word_count_breakup_by_year[year]:
                    word_count_breakup_by_year[year][word] += 1
                    breakup_score += word_count_breakup_by_year[year][word]
                else:
                    word_count_breakup_by_year[year][word] = 1
if love_score > breakup_score:
    classifications1.append("Love")
elif breakup_score > love_score:
    classifications1.append("Breakup")
else:
    classifications1.append("Neutral")

for year in word_count_love_by_year:
    sorted_word_count_love = sorted(word_count_love_by_year[year].items(), key=lambda x: x[1], reverse=True)
    print("Year:", year)
    print("Love words:", sorted_word_count_love)

for year in word_count_breakup_by_year:
    sorted_word_count_breakup = sorted(word_count_breakup_by_year[year].items(), key=lambda x: x[1], reverse=True)
    print("Year:", year)
    print("Breakup words:", sorted_word_count_breakup)


# In[27]:


import pandas as pd

# Convert dictionaries to dataframes
df_love = pd.DataFrame(word_count_love_by_year)
df_breakup = pd.DataFrame(word_count_breakup_by_year)

# Write dataframes to excel
writer = pd.ExcelWriter('word_counts.xlsx', engine='xlsxwriter')
df_love.to_excel(writer, sheet_name='Love_Words')
df_breakup.to_excel(writer, sheet_name='Breakup_Words')
writer.save()


# In[227]:


word_count = {}
for item in objectlist2:
    words = item['Title'].split() # assuming title is the key
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print(sorted_word_count)


# In[ ]:





# In[ ]:





# In[ ]:





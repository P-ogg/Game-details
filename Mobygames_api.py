#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd


# ## Test code: print dataframe of one game

# In[2]:


# Set prameters
x=100
parameters = {
    "offset": x,
    "limit":1
}

# Get json from API
#While response.status_code == 200:
response = requests.get('https://api.mobygames.com/v1/games?api_key=moby_BE9XIO2SOpkDndSUZiNv29zEiT4', params=parameters)
x=x+100
    
if response.status_code == 200:
    print("Succesful connection to API.")
    print('-------------------------------')
    data = response.json()
    #print(data)
elif response.status_code == 404:
    print("Unable to reach URL.")
else:
    print("Unable to connect to API or retrieve data.")

# Prepare to print nice-looking JSON
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Print nice-looking JSON
#jprint(response.json())

# Convert JSON to DataFtrame 
data = data['games']

#df.genres[0][0]

df = pd.json_normalize(data,)

df = df.explode('genres')
df = df.explode('platforms')
df = pd.concat([df,df['genres'].apply(pd.Series)],axis=1)
df = pd.concat([df,df['platforms'].apply(pd.Series)],axis=1)

# Drop irrelevatnt columns
df = df.drop(columns=['platforms','sample_screenshots','alternate_titles','genres', 'sample_cover.height', 'official_url', 'sample_cover.image', 'sample_cover.thumbnail_image', 'sample_cover.platforms', 'sample_cover.width', 'description'])
df



# ## Test code: download info on first 5000 games to csv

# In[5]:


# Set prameters
x=0
parameters = {
    "offset": x,
    "limit":100
}

# Get json from API

response = requests.get('https://api.mobygames.com/v1/games?api_key=moby_BE9XIO2SOpkDndSUZiNv29zEiT4', params=parameters)

while response.status_code == 200 and x< 5000:
    response = requests.get('https://api.mobygames.com/v1/games?api_key=moby_BE9XIO2SOpkDndSUZiNv29zEiT4', params={"offset":x, "limit":100})
    if x==0:
        print("Succesful connection with API.")
        print('-------------------------------')
    elif x%500==0:
        print("Data on ", x, " games collected")
    data = response.json()
    #print(data)
    data = data['games']

    df = pd.json_normalize(data,)

    df = df.explode('genres')
    df = df.explode('platforms')
    df = pd.concat([df,df['genres'].apply(pd.Series)],axis=1)
    df = pd.concat([df,df['platforms'].apply(pd.Series)],axis=1)

    # Drop irrelevatnt columns
    df = df.drop(columns=['platforms','sample_screenshots','alternate_titles','genres', 'sample_cover.height', 'official_url', 'sample_cover.image', 'sample_cover.thumbnail_image', 'sample_cover.platforms', 'sample_cover.width', 'description'])

    if x ==0:
        header=True
    else:
        header=False

    df.to_csv(r'bygames_moby.csv', index=False, mode='a', header=header, chunksize=5000)
    x=x+100
else:
    if response.status_code == 404:
        print("Unable to reach URL.")
    else:
        print("Unable to connect API or retrieve data.")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import DBSCAN


# In[2]:


df = pd.read_json('livedata.json')
df.head()


# In[3]:


import plotly.express as px

fig = px.scatter(df, x='latitude', y='longitude',hover_data=df ,size_max=200, color="id")
fig.update_layout(title_text='Latitude-Longitude', title_x=0.5)
print('Hover over the data to get the complete info')
fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})

fig.show()


# In[7]:


def get_infected_people(input_name):

    epsilon = 0.0018288 # a radial distance of 6 feet in kilometers
    model = DBSCAN(eps=epsilon, min_samples=3, metric='haversine')
    model.fit(df[['latitude', 'longitude']])
    df['cluster'] = model.labels_.tolist()

    name_clusters = []
    for i in range(len(df)):
        if df['id'][i] == input_name:
            if df['cluster'][i] in name_clusters:
                pass
            else:
                name_clusters.append(df['cluster'][i])
    
    infected_names = []
    for cluster in name_clusters:
        if cluster != -1:
            id_cluster = df.loc[df['cluster'] == cluster, 'id']
            for i in range(len(id_cluster)):
                member_id = id_cluster.iloc[i]
                if (member_id not in infected_names) and (member_id != input_name):
                    infected_names.append(member_id)
                else:
                    pass
    return infected_names


# In[8]:


get_infected_names("David")


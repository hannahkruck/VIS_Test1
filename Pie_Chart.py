#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


# In[2]:


df = pd.read_csv("piechart.csv", encoding ="utf8", sep=";")
#df


# In[3]:

# Daten in Liste übergeben
labels = df['year'].tolist()
values = df['2019'].tolist()

# Pie Charterstellen
fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent', insidetextorientation='radial', title='Kuchendiagramm')])
            
st.plotly_chart(fig)

# In[ ]:

# In[ ]:





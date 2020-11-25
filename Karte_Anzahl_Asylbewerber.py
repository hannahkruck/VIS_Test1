#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import altair as alt
from altair import Chart, X, Y, Axis, SortField, OpacityValue
import numpy as np
# In[2]:
#Datentabelle laden und ausblenden
#def load_data():
  
# read CSV
df = pd.read_csv("https://raw.githubusercontent.com/hannahkruck/VIS_Test1/Develop/map.csv", encoding ="utf8", sep=";")

# Remove 'overall' and 'Überseeische Länder und Hoheitsgebiet'
indexNames = df[ df['destinationCountry'] == 'Overall' ].index
df.drop(indexNames , inplace=True)
indexNames = df[ df['homeCountry'] == 'Overall' ].index
df.drop(indexNames , inplace=True)

indexNames = df[ df['destinationCountry'] == 'Überseeische Länder und Hoheitsgebiete' ].index
df.drop(indexNames , inplace=True)
indexNames = df[ df['homeCountry'] == 'Überseeische Länder und Hoheitsgebiete' ].index
df.drop(indexNames , inplace=True)


# In[4]:


# Berechnung der Anzahl aller Antragssteller in einem Land nach Jahr (diese Daten sind nur von Europa verfügbar)
# Speichern in neu erstellten Zeile 'sum'

df['sum']=df.groupby(['destinationCountry','year'])['total'].transform('sum')


# In[5]:

#Datentabelle ausblenden
#    return df
# df = load_data()


# Delete all cells, except one year!
a = 2018
indexNames = df[ df['year'] != a ].index
df.drop(indexNames , inplace=True)


# In[6]:
#Vollbild verwenden
st.set_page_config(layout="wide")

# Map with colours (Number of asylum applications)
fig = go.Figure(data=go.Choropleth(
    locations = df['geoCodeDC'],
    z = df['sum'],
    text = df['destinationCountry'],
    colorscale = 'Blues', #Viridis
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = '',
    colorbar_title = 'Number of asylum applications'
))


fig.update_layout(
    title_text='Asylum seekers in Europe in the year %s' % a,
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    autosize=True,
    #width=1500,
    #height=1080,
)
#--------------------Slider Steps------------------------------------#
#https://stackoverflow.com/questions/46777047/how-to-make-a-choropleth-map-with-a-slider-using-plotly


st.plotly_chart(fig, width=1920)

st.slider("Timeline Years", 2010,  2019)

#Sidebar
st.sidebar.header("Filters")
st.sidebar.multiselect("Select Age", ("All", "under 18", "18 - 35", "26 - 35", "36 - 45"))
st.sidebar.multiselect("Select Gender", ("All", "Male", "Female", "Other/unknown"))
st.sidebar.multiselect("Select Origin Country", ("All", "Belgium", "Bulgaria", "Czech Republic", "Denmark", "Germany", "Estonia", "Ireland", "Greece", "Spain"))
st.sidebar.multiselect("Select Destination Country", ("All", "Belgium", "Bulgaria", "Czech Republic", "Denmark", "Germany", "Estonia", "Ireland", "Greece", "Spain"))

#st.sidebar.subheader("Filter option 2")
# Checkbox widget
#checkbox = st.sidebar.checkbox("Datensatz einblenden")
#print(checkbox)
#add select widget
#select_box_age = st.sidebar.selectbox(label='AGE', options=columns_checkbox)
#print(select_box_age)

#https://stackoverflow.com/questions/63158617/multiple-same-key-button-generated-in-streamlit
#st.sidebar.text('AGE')
#select_box1 = st.sidebar.checkbox("Select all", "under 18", "18 - 35", "26 - 35", "36 - 45")
#select_box1 = st.sidebar.checkbox(label="Select all", key="1")
#select_box2 = st.sidebar.checkbox(label="under 18", key="2")
#select_box3 = st.sidebar.checkbox(label="18 - 35", key="3")
#select_box4 = st.sidebar.checkbox(label="26 - 35", key="4")
#select_box5 = st.sidebar.checkbox(label="36 - 45", key="5")

#print(select_box1)
#print(select_box2)
#print(select_box3)
#print(select_box4)
#print(select_box5)


#st.sidebar.text('GENDER')
#select_box6 = st.sidebar.checkbox(label="Select all", key="6")
#select_box7 = st.sidebar.checkbox(label="Female", key="7")
#select_box8 = st.sidebar.checkbox(label="Male", key="8")
#select_box9 = st.sidebar.checkbox(label="Other/unknown", key="9")
#print(select_box6)
#print(select_box7)
#print(select_box8)
#print(select_box9)

# In[ ]:



#https://discuss.streamlit.io/t/st-bar-chart/4922
    #chart = alt.Chart(df).mark_bar().encode(
    #alt.Y("sum", bin=True),
    #x='GeoCode',).interactive()
    #st.altair_chart(chart)


st.dataframe(data=df)


# In[ ]:





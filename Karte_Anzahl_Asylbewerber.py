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
    
# CSV einlesen
df = pd.read_csv("https://raw.githubusercontent.com/hannahkruck/VIS_Test1/Develop/Kartenuebersicht.csv", encoding ="utf8", sep=";")

# Umwandeln funktioniert nicht, da es NA nicht verarbeiten kann
# df["wU18"]= df["wU18"].astype('int')

#df


# In[3]:


    # Ländernamen ersetzen/kürzen
df['Geo'].replace({'Deutschland (bis 1990 früheres Gebiet der BRD)':'Deutschland','Kosovo (gemäß der Resolution 1244/99 des Sicherheitsrates der Vereinten Nationen)':'Kosovo', 'Föderierte Staaten von Mikronesien': 'Mikronesien'},inplace=True)
df['Citizen'].replace({'Deutschland (bis 1990 früheres Gebiet der BRD)':'Deutschland','Kosovo (gemäß der Resolution 1244/99 des Sicherheitsrates der Vereinten Nationen)':'Kosovo', 'Föderierte Staaten von Mikronesien': 'Mikronesien'},inplace=True)

# Insgesamt entfernen
indexNames = df[ df['Geo'] == 'Insgesamt' ].index
df.drop(indexNames , inplace=True)
indexNames = df[ df['Citizen'] == 'Insgesamt' ].index
df.drop(indexNames , inplace=True)
#df


# In[4]:


# Berechnung der Anzahl aller Antragssteller in einem Land nach Jahr (diese Daten sind nur von Europa verfügbar)
# Speichern in neu erstellten Zeile 'sum'

df['sum']=df.groupby(['Geo','Year'])['PersonenGesamt'].transform('sum')
    

# In[5]:

#Datentabelle ausblenden
#    return df
# df = load_data()


# Lösche alle Zellen, außer ein Jahr!
a = 2018
indexNames = df[ df['Year'] != a ].index
df.drop(indexNames , inplace=True)
#df

    

# In[6]:


# Karte mit Farben (Anzahl Asylbewerber)
fig = go.Figure(data=go.Choropleth(
    locations = df['GeoCode'],
    z = df['sum'],
    text = df['Geo'],
    colorscale = 'Blues', #Viridis
    autocolorscale=False,
    reversescale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = '',
    colorbar_title = 'Anzahl Antraege'
))


fig.update_layout(
    title_text='Asylbewerber in Europa im Jahr %s' % a,
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    )
)
#--------------------Slider Steps------------------------------------#
#https://stackoverflow.com/questions/46777047/how-to-make-a-choropleth-map-with-a-slider-using-plotly




st.plotly_chart(fig)




st.sidebar.header("Filteroptionen")
st.sidebar.multiselect("Select Age", ("Select all", "under 18", "18 - 35", "26 - 35", "36 - 45"))

# Checkbox widget
#checkbox = st.sidebar.checkbox("Datensatz einblenden")
#print(checkbox)

st.sidebar.subheader("Filter option 2")
#add select widget
#select_box_age = st.sidebar.selectbox(label='AGE', options=columns_checkbox)
#print(select_box_age)

#https://stackoverflow.com/questions/63158617/multiple-same-key-button-generated-in-streamlit
st.sidebar.text('AGE')
#select_box1 = st.sidebar.checkbox("Select all", "under 18", "18 - 35", "26 - 35", "36 - 45")
select_box1 = st.sidebar.checkbox(label="Select all", key="1")
select_box2 = st.sidebar.checkbox(label="under 18", key="2")
select_box3 = st.sidebar.checkbox(label="18 - 35", key="3")
select_box4 = st.sidebar.checkbox(label="26 - 35", key="4")
select_box5 = st.sidebar.checkbox(label="36 - 45", key="5")

print(select_box1)
print(select_box2)
print(select_box3)
print(select_box4)
print(select_box5)


st.sidebar.text('GENDER')
select_box6 = st.sidebar.checkbox(label="Select all", key="6")
select_box7 = st.sidebar.checkbox(label="Female", key="7")
select_box8 = st.sidebar.checkbox(label="Male", key="8")
select_box9 = st.sidebar.checkbox(label="Other/unknown", key="9")
print(select_box6)
print(select_box7)
print(select_box8)
print(select_box9)

# In[ ]:



#https://discuss.streamlit.io/t/st-bar-chart/4922
    #chart = alt.Chart(df).mark_bar().encode(
    #alt.Y("sum", bin=True),
    #x='GeoCode',).interactive()
    #st.altair_chart(chart)


st.dataframe(data=df)


# In[ ]:





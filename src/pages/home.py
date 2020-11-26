"""Home page shown when the user enters the application"""
import streamlit as st
import awesome_streamlit as ast
import plotly.graph_objects as go
import pandas as pd
import altair as alt
from altair import Chart, X, Y, Axis, SortField, OpacityValue
import numpy as np

# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading Home ..."):
        ast.shared.components.title_awesome("")
        
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



        # Berechnung der Anzahl aller Antragssteller in einem Land nach Jahr (diese Daten sind nur von Europa verfügbar)
        # Speichern in neu erstellten Zeile 'sum'

        df['sum']=df.groupby(['destinationCountry','year'])['total'].transform('sum')


        #Datentabelle ausblenden
        #    return df
        # df = load_data()


        # Delete all cells, except one year!
        a = 2018
        indexNames = df[ df['year'] != a ].index
        df.drop(indexNames , inplace=True)


        # In[6]:
        #Vollbild verwenden
        #st.set_page_config(layout="wide")

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
            width=1500,
            height=1080,
        )
        #--------------------Slider Steps------------------------------------#
        #https://stackoverflow.com/questions/46777047/how-to-make-a-choropleth-map-with-a-slider-using-plotly


        st.plotly_chart(fig)

        st.slider("Timeline Years", 2010,  2019)

        #Sidebar
        st.sidebar.header("Filters")
        st.sidebar.multiselect("Select Age", ("All", "under 18", "18 - 35", "26 - 35", "36 - 45"))
        st.sidebar.multiselect("Select Gender", ("All", "Male", "Female", "Other/unknown"))
        st.sidebar.multiselect("Select Origin Country", ("All", "Belgium", "Bulgaria", "Czech Republic", "Denmark", "Germany", "Estonia", "Ireland", "Greece", "Spain"))
        st.sidebar.multiselect("Select Destination Country", ("All", "Belgium", "Bulgaria", "Czech Republic", "Denmark", "Germany", "Estonia", "Ireland", "Greece", "Spain"))

#Datentabelle einblenden
    #    st.dataframe(data=df)
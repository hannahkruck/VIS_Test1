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
        #ast.shared.components.title_awesome("")    #Title Awesome Streamlit ausgeblendet
        
        st.title("Welcome to the Asylum Seekers EU Information Website")
        
        # read CSV
        df = pd.read_csv("https://raw.githubusercontent.com/hannahkruck/VIS_Test1/Develop/mapNew.csv", encoding ="utf8", sep=";")
        df2 = pd.read_csv("https://raw.githubusercontent.com/hannahkruck/VIS_Test1/Develop/mapNew.csv", encoding ="utf8", sep=";")

        # Remove 'overall' and 'Überseeische Länder und Hoheitsgebiet'
        indexNames = df[ df['destinationCountry'] == 'Overall' ].index
        df.drop(indexNames , inplace=True)
        indexNames = df[ df['homeCountry'] == 'Overall' ].index
        df.drop(indexNames , inplace=True)

        indexNames = df[ df['destinationCountry'] == 'Überseeische Länder und Hoheitsgebiete' ].index
        df.drop(indexNames , inplace=True)
        indexNames = df[ df['homeCountry'] == 'Überseeische Länder und Hoheitsgebiete' ].index
        df.drop(indexNames , inplace=True)

        # Remove 'overall' and 'Überseeische Länder und Hoheitsgebiet'
        indexNames = df2[ df2['destinationCountry'] == 'Overall' ].index
        df2.drop(indexNames , inplace=True)
        indexNames = df2[ df2['homeCountry'] == 'Overall' ].index
        df2.drop(indexNames , inplace=True)

        indexNames = df2[ df2['destinationCountry'] == 'Überseeische Länder und Hoheitsgebiete' ].index
        df2.drop(indexNames , inplace=True)
        indexNames = df2[ df2['homeCountry'] == 'Überseeische Länder und Hoheitsgebiete' ].index
        df2.drop(indexNames , inplace=True)



        # Berechnung der Anzahl aller Antragssteller in einem Land nach Jahr (diese Daten sind nur von Europa verfügbar)
        # Speichern in neu erstellten Zeile 'sum'

        df['sum']=df.groupby(['homeCountry','year'])['total'].transform('sum')


        #Datentabelle ausblenden
        #    return df
        # df = load_data()


        # Delete all cells, except one year!
        year = 2019
        indexNames = df[ df['year'] != year ].index
        df.drop(indexNames , inplace=True)

        indexNames = df2[ df2['year'] != year ].index
        df2.drop(indexNames , inplace=True)
        indexNames = df2[ df2['total'] == 0 ].index
        df2.drop(indexNames , inplace=True)
        
        # Auswahl eines bestimmten Ziellandes
        countryCategory = 'homeCountry'#homeCountry or destinationCountry
        countryName = 'Syria'
        indexNames = df2[ df2[countryCategory] != countryName ].index
        df2.drop(indexNames , inplace=True)


    
        st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        

#----------------Sidebar und Parameter------------------------------
        st.sidebar.header("Filters")
        st.sidebar.multiselect("Select Age", ("All", "under 18", "18 - 34", "35 - 64", "over 64"))
        st.sidebar.multiselect("Select Gender", ("All", "Male", "Female"))
        
        st.sidebar.header("Filter for Choropleth Map")
        st.sidebar.multiselect("Select Map Information",("Applications to target countries", "Applicants by country of origin"))
        #st.sidebar.multiselect("Select Origin Country", ("All", "Belgium", "Bulgaria", "Czech Republic", "Denmark", "Germany", "Estonia", "Ireland", "Greece", "Spain"))
        #st.sidebar.multiselect("Select Destination Country", ("All", "Belgium", "Bulgaria", "Czech Republic", "Denmark", "Germany", "Estonia", "Ireland", "Greece", "Spain"))





        # Parameterfilter - Nur bestimmte Ziellaender anzeigen lassen
        #country_name_input = st.sidebar.multiselect(
        #'Select Destination Country (funktioniert)',
        #df.groupby('destinationCountry').count().reset_index()['destinationCountry'].tolist())
        # by country name
        #if len(country_name_input) > 0:
        #    df = df[df['destinationCountry'].isin(country_name_input)]
            
        #Vollbild verwenden
        #st.set_page_config(layout="wide")
            
#----------------Create Maps (alt)---------------------------

        # Map with colours (Number of asylum applications)
#           fig = go.Figure(data=go.Choropleth(
#            locations = df['geoCodeDC'],
#            z = df['sum'],
#            text = df['destinationCountry'],
#            colorscale = 'Blues', #Viridis
#            autocolorscale=False,
#            reversescale=False,
#            marker_line_color='darkgray',
#            marker_line_width=0.5,
#            colorbar_tickprefix = '',
#            colorbar_title = 'Number of asylum applications'
#        ))

#        fig.update_layout(
#            title_text='Asylum seekers in Europe in the year %s' % a,
#            geo=dict(
#                showframe=False,
#            showcoastlines=False,
#                projection_type='equirectangular'
#            ),
#            autosize=True,
#            width=1500,
#            height=1080,
#        )
        
        
#----------------Create Maps (Color und Line Map)---------------------------
        
        #Link Toggle Map https://plotly.com/python/custom-buttons/
                # Choropleth Map with colours (Number of asylum applications)
                
              
        
                
        fig = go.Figure()
    
        fig.add_trace(
            go.Choropleth(
            locations = df['geoCodeHC'],
            z = df['sum'],
            text = df['homeCountry'],
            colorscale = 'Reds',                   #Magenta
            autocolorscale=False,
            reversescale=False,
            marker_line_color='darkgray',
            marker_line_width=0.5,
            colorbar_tickprefix = '',
            colorbar_title = 'Number of<br>asylum<br>applications<br>',
        
                
        ))    

        
    
    
        fig.add_trace(
            go.Scattergeo(
            locationmode = 'country names',
            lon = df2['lonDC'],
            lat = df2['latDC'],
            hoverinfo = 'text',
            text = df2['destinationCountry'],
            line = dict(width = 1,color = 'red'),
            opacity = 0.510,
            visible=False,
            mode = 'markers',
            marker = dict(
                size = 3,
                color = 'rgb(255, 0, 0)',
                line = dict(
                    width = 3,
                    color = 'rgba(68, 68, 68, 0)',
                ))))
    
    
        lons = []
        lats = []
        lons = np.empty(2 * len(df2))
        lons[::2] = df2['lonDC']
        lons[1::2] = df2['lonHC']
        lats = np.empty(2 * len(df2))
        lats[::2] = df2['latDC']
        lats[1::2] = df2['latHC']
    
        fig.add_trace(
            go.Scattergeo(
                locationmode = 'country names',
                visible= False,
                lon = lons,
                lat = lats,
                mode = 'lines',
                line = dict(width = 1,color = 'red'),
                opacity = 0.5
            )
        )
    
        fig.update_layout(
            showlegend = True,
            geo = go.layout.Geo(
                scope = 'world',
                #projection_type = 'azimuthal equal area',
                showland = True,
                showcountries=True,
                landcolor = 'rgb(243, 243, 243)',
                countrycolor = 'rgb(105,105,105)',
            ),
            height=700,
        )
        
        
        
        fig.update_layout(
            
            updatemenus=[
                dict(
                    type="buttons",
                    direction="right",
                    active=0,
                    x=0.57,
                    y=1.2,
                    buttons=list([
                        dict(label="Choropleth Map",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                    ]),
                        
                        dict(label="Line Map",
                            method="update",
                            args=[{"visible": [False,True,True]},
                                    ]),
                        
                    ]),
                )
            ])        
    
        fig.update_layout(
            title_text='Asylum seekers in Europe in the year %s' % year,
            geo=dict(
                showframe=False,            # Map Rahmen ausgeblendet
                showcoastlines=False,
                projection_type='equirectangular'
            ),
            
            autosize=True,
            width=1500,
            height=1080,
        )
        
        
        
        st.plotly_chart(fig)
        
        
#--------------------Slider Steps------------------------------------#
#https://stackoverflow.com/questions/46777047/how-to-make-a-choropleth-map-with-a-slider-using-plotly

        st.slider("Timeline Years", 2010,  2019)

        
#Datentabelle einblenden
    #    st.dataframe(data=df)
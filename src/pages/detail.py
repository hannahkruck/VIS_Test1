"""This page is for more details"""
import logging

import streamlit as st

import awesome_streamlit as ast
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np


logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

def write():
    """Writes content to the app"""
    ast.shared.components.title_awesome("Detail")

    # read CSV
    df = pd.read_csv("https://raw.githubusercontent.com/hannahkruck/VIS_Test1/Develop/piechart.csv", encoding ="utf8", sep=";")
    
    c1, c2 = st.beta_columns((1, 1))
    container = st.beta_container()
    

#---------------Create sankey diagramm--------------------------
#https://www.geeksforgeeks.org/sankey-diagram-using-plotly-in-python/
#https://coderzcolumn.com/tutorials/data-science/how-to-plot-sankey-diagram-in-python-jupyter-notebook-holoviews-and-plotly#2
    
    # Nodes & links
    nodes = [['ID', 'Label', 'Color'],
            [0,'Afghanistan','#4CB24C'],    # AKJ
            [1,'Syria','grey'],             # '#8A5988'
            [2,'Serbia','#CDC037'],
            [3,'Irak','#C37522'],
            [4,'Kosovos','#D3D3D3'],
            [5,'Iran','#2270C3'],
            [6,'Germany', '#0B2641'],
            [7,'France','#0B2641'],
            [8,'Sweden','#0B2641'],
            [9,'Greece','#0B2641']]
    
    # links with your data
    links = [['Source','Target','Value','Link Color'],
        
        # Afghanistan
        [0,6,11280,'rgba(76, 178, 76, 0.35)'], #Afghanistan - Deutschland Value
        [0,7,12085,'rgba(76, 178, 76, 0.35)'],
        [0,8,905,'rgba(76, 178, 76, 0.35)'],
        [0,9,23820,'rgba(76, 178, 76, 0.35)'],
        
        # Syria
        [1,6,41060,'rgba(211, 211, 211,  0.35)'],
        [1,7,3080,'rgba(211, 211, 211, 0.35)'],
        [1,8,5225,'rgba(211, 211, 211, 0.35)'],
        [1,9,10855,'rgba(211, 211, 211, 0.35)'],
        
        # Serbia
        [2,6,6795,'rgba(178, 170, 76, 0.35)'],
        [2,7,790,'rgba(178, 170, 76, 0.35)'],
        [2,8,6250,'rgba(178, 170, 76, 0.35)'],
        [2,9,0,'rgba(178, 170, 76, 0.35)'],
        
        # Irak
        [3,6,15325,'rgba(220, 142, 59, 0.35)'],
        [3,7,1370,'rgba(220, 142, 59, 0.35)'],
        [3,8,1220,'rgba(220, 142, 59, 0.35)'],
        [3,9,5740,'rgba(220, 142, 59, 0.35)'],
        
        # Iran
        [5,6,9490,'rgba(59, 137, 220, 0.35)'],
        [5,7,630,'rgba(59, 137, 220, 0.35)'],
        [5,8,1115,'rgba(59, 137, 220, 0.35)'],
        [5,9,2390,'rgba(59, 137, 220, 0.35)']]
    
    
    # Retrieve headers and build dataframes
    nodes_headers = nodes.pop(0)
    links_headers = links.pop(0)
    df_nodes = pd.DataFrame(nodes, columns = nodes_headers)
    df_links = pd.DataFrame(links, columns = links_headers)
    
    # Sankey plot setup
    data_trace = dict(
            type='sankey',
            domain = dict(
                x =  [0,1],
                y =  [0,1]
            ),
            orientation = "h",
            valueformat = ".0f",
            node = dict(
                pad = 10,
            # thickness = 30,
                line = dict(
                    color = "black",
                    width = 0
                ),
                label =  df_nodes['Label'].dropna(axis=0, how='any'),
                color = df_nodes['Color']
            ),
            link = dict(
                source = df_links['Source'].dropna(axis=0, how='any'),
                target = df_links['Target'].dropna(axis=0, how='any'),
                value = df_links['Value'].dropna(axis=0, how='any'),
                color = df_links['Link Color'].dropna(axis=0, how='any'),
        )
    )
    
    layout = dict(
                    title = "Top 10",
            height = 500,                   
            font = dict(
                size = 10),)
    
    fig1 = dict(data=[data_trace], layout=layout)
    
    
    
#------------Create pie chart-------------------
        
    # Daten in Liste übergeben
    labels = df['year'].tolist()
    values = df['2019'].tolist()
    
    fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent', insidetextorientation='radial', title='Kuchendiagramm')])
    
    
    # Create figure 3
    fig3 = go.Figure()
    
    # Add traces, one for each slider step
    for step in np.arange(10):                                  # Zeitrahl Schritte von 2010 bis 2019
        fig3.add_trace(
            go.Scatter(
                visible=False,
                line=dict(color='LightSkyBlue', width=3),       # Zeitstrahl Linie
                
                name="𝜈 = " + str(step),
                x=np.arange(0, 5, 0.01),
                y=np.sin(step * np.arange(0, 1, 0.02))))        # Sinus Formel
    
    
    # Make 10th trace visible
    fig3.data[2].visible = True
    
# ------------------Create and add slider VS 1.0---------------
    #steps = []
    #for i in range(len(fig3.data)):
        #step = dict(
            #method="update",
            #args=[{"visible": [False] * len(fig3.data)},
                #  {"title": "Slider switched to step: " + str(i)}],  # layout attribute
        #)
        #step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        #steps.append(step)
    
        #sliders = [dict(
        #active=10,
        #currentvalue={"prefix": "Frequency: "},
        #pad={"t": 50},
        #steps=steps
        #)]
    
# ------------------Create and add slider VS 1.1---------------
    steps = []
    for i in range(len(fig3.data)):
        step = dict(method='restyle',
                    args=['visible', [False] * len(fig3.data)],
                    #label='{}'.format(i + 2010))
                    label = i + 2010)
        step['args'][1][i] = True
        steps.append(step)
        
        
    sliders = [dict(active=9,
        pad={"t": 20},          #padding
        steps=steps)]    
    
    
    fig3.update_layout(
        sliders=sliders,
        width=1000
    )    
    
    #fig.show()
    
    # disable the modebar for such a small plot
    #fig1.show(config=dict(displayModeBar=False))
    #st.plotly_chart(fig1)
    #second chart
    with c1:
        st.plotly_chart(fig2)
    with c2:
        st.plotly_chart(fig1)
    with container:
        st.plotly_chart(fig3)

if __name__ == "__main__":
    write()
    
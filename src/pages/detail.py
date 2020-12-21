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
    #ast.shared.components.title_awesome("Detail")      # Titel Awesome_Streamlit
    
    # Page title
    st.title("Detailed view")
#   st.header('Hier kann ein Text rein')
    
    # read CSV
    # CSV for Pie Chart
    df = pd.read_csv("https://raw.githubusercontent.com/hannahkruck/VIS_Test1/Develop/piechart.csv", encoding ="utf8", sep=";")
    

    #-----------------Markdown info-----------------
    
    st.markdown('''
    <!-- https://www.w3schools.com/css/tryit.asp?filename=trycss_tooltip_transition & https://www.w3schools.com/css/tryit.asp?filename=trycss_tooltip_right-->
    <style>
        .tooltip {
            position: relative;
            display: inline-block;
            font-size:1.6rem;
            
        }
        
        .tooltip .tooltiptext {
            visibility: hidden;
            width: 50vw;
            background-color: #f1f3f7;
            color: #262730;
            text-align: justify;
            border-radius: 6px;
            padding: 5px;
            font-size:0.9rem;
            
            /* Position the tooltip */
            position: absolute;
            z-index: 1;
            top: -5px;
            left: 105%;
            
            opacity: 0;
            transition: opacity 0.8s;
        }
        
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
    </style>
    ''', unsafe_allow_html=True)

    st.markdown('''
        <div class="tooltip">&#x24D8
        <span class="tooltiptext">
        <b>Pie Chart</b><br>
        The pie chart represents the age distribution.
        <br><br>
        <b>Sankey Diagram</b><br>
        The Sankey diagram shows the distribution of asylum applications from the different countries of origin (left) to the different countries of destination (right).
        top 10 destination countries of a year are illustrated here.
        <br><br>
        </span></div>
        ''', unsafe_allow_html=True)  


    # Layout setting of the page 
    c1, c2 = st.beta_columns((1, 1))
    container = st.beta_container()
    st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    
#-------------------------Create Sankey diagram-------------------------------
#https://www.geeksforgeeks.org/sankey-diagram-using-plotly-in-python/
#https://coderzcolumn.com/tutorials/data-science/how-to-plot-sankey-diagram-in-python-jupyter-notebook-holoviews-and-plotly#2
    
    # Variabel fuer Sankey diagramm
    yearVar = 2019                       
    
    #daten einlesen & selectieren
    show_df = pd.read_csv('https://raw.githubusercontent.com/hannahkruck/VIS_Test1/Develop/Datensatz_Sankey_Diagramm_eng.csv',sep = ';')

    #YEAR
    yearRows = show_df[show_df['Year'] != yearVar].index
    show_df.drop(yearRows , inplace=True)


    # Nodes & links & colors
    label_souce = show_df['Label_Source'].dropna(axis=0, how='any')
    label_souce2 = []
    elementVar = ''

    for i in label_souce: 
        if(i != elementVar) : 
            label_souce2.append(i)
        elementVar = i

    label_target = show_df['Label_Target'].dropna(axis=0, how='any')
    label = [*label_souce2, *label_target]
    source = show_df['Source'].dropna(axis=0, how='any')
    target = show_df['Target'].dropna(axis=0, how='any')
    value = show_df['Value'].dropna(axis=0, how='any')

    #color
    color_node = [
    #Source
    '#2e8b57', '#cd8162', '#00e5ee', '#458b74', '#C37522', '#2270C3', '#ff6a6a', '#9370db', '#CDC037', '#787878',
    #Target
    '#0B2641', '#0B2641', '#0B2641', '#0B2641', '#0B2641', '#0B2641', '#0B2641', '#0B2641', '#0B2641', '#0B2641']
    color_link = [
    '#4ab24a', '#4ab24a', '#4ab24a', '#4ab24a', '#4ab24a', '#4ab24a', '#4ab24a', '#4ab24a', '#4ab24a', '#4ab24a',
    '#ce8161', '#ce8161', '#ce8161', '#ce8161', '#ce8161', '#ce8161', '#ce8161', '#ce8161', '#ce8161', '#ce8161', 
    '#00e5ee', '#00e5ee', '#00e5ee', '#00e5ee', '#00e5ee', '#00e5ee', '#00e5ee', '#00e5ee', '#00e5ee', '#00e5ee',
    '#458a73', '#458a73', '#458a73', '#458a73', '#458a73', '#458a73', '#458a73', '#458a73', '#458a73', '#458a73', 
    '#dd8c39', '#dd8c39', '#dd8c39', '#dd8c39', '#dd8c39', '#dd8c39', '#dd8c39', '#dd8c39', '#dd8c39', '#dd8c39',
    '#398add', '#398add', '#398add', '#398add', '#398add', '#398add', '#398add', '#398add', '#398add', '#398add',
    '#ff6a6a', '#ff6a6a', '#ff6a6a', '#ff6a6a', '#ff6a6a', '#ff6a6a', '#ff6a6a', '#ff6a6a', '#ff6a6a', '#ff6a6a', 
    '#9270da', '#9270da', '#9270da', '#9270da', '#9270da', '#9270da', '#9270da', '#9270da', '#9270da', '#9270da', 
    '#ffd700', '#ffd700', '#ffd700', '#ffd700', '#ffd700', '#ffd700', '#ffd700', '#ffd700', '#ffd700', '#ffd700', 
    '#787878', '#787878', '#787878', '#787878', '#787878', '#787878', '#787878', '#787878', '#787878', '#787878']

    # data to dict, dict to sankey
    link = dict(source = source, target = target, value = value, color=color_link)
    node = dict(label = label, pad=50, thickness=5, color=color_node)
    layout = dict(
            #"Top 10 Verteilung der Asylanträge eines Landes auf die verschiedenen Zielländer"
            title= 'Top 10 Distribution of a Countries Asylum Applications among the various <br>Countries of Destination  %s' % yearVar,
            height = 800,                   
            font = dict(size = 11),)
    data = go.Sankey(link = link, node=node)
    
    # Eigenschaften Sanky Diagram Layout 
    fig2 = go.Figure(data, layout= layout)
    
#------------Create pie chart-------------------
    
    # Transfer data to list
    labels = df['year'].tolist()
    values = df['2019'].tolist()
    layout = dict( 
        height = 600,       
        font = dict(size = 11),            
        title='Age Distribution of Asylum Seekers Worldwide %s' % yearVar)
    data = go.Pie(labels=labels, values=values)

    # Create pie figure
    fig1 = go.Figure(data=[go.Pie(
        labels=labels, 
        values=values, 
        textinfo='label+percent', 
        insidetextorientation='radial',)])
    
    # Features Pie Diagram Layout
    fig1 = go.Figure(data, layout=layout)

    

#------------Create Timeline Years-------------------
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
        st.plotly_chart(fig1)
    with c2:
        st.plotly_chart(fig2)
    with container:
        st.plotly_chart(fig3)

if __name__ == "__main__":
    write()
    
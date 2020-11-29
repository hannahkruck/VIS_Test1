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
    
    #Titel der Seite
    st.title("Detailansicht")
#   st.header('Hier kann ein Text rein')
    
    # lese CSV
    df = pd.read_csv("https://raw.githubusercontent.com/hannahkruck/VIS_Test1/Develop/piechart.csv", encoding ="utf8", sep=";")
    
    c1, c2 = st.beta_columns((1, 1))
    container = st.beta_container()
    

#-------------------------Create Sankey diagram-------------------------------
#https://www.geeksforgeeks.org/sankey-diagram-using-plotly-in-python/
#https://coderzcolumn.com/tutorials/data-science/how-to-plot-sankey-diagram-in-python-jupyter-notebook-holoviews-and-plotly#2
    
    # Variabel: Auswahl Jahr fuer Sankey diagramm
    a = 2019                           
    
    # Nodes & links & colors
    nodes = [['ID', 'Label', 'Color'],  
            #Origins
            [0,'Syria','#2e8b57'],
            [1,'Irak','#cd8162'],
            [2,'Iran','#00e5ee'],
            [3,'Türkei','#458b74'],
            [4,'Nigeria','#C37522'], 
            [5,'Afghanistan','#2270C3'], 
            [6,'Albanien','#ff6a6a'],
            [7,'Pakistan','#9370db'], 
            [8,'Venezuela','#CDC037'], 
            [9,'Colombia','#787878'],

            #Target
            [10,'Germany', '#0B2641'],
            [11,'Sweden','#0B2641'],
            [12,'Netherlands','#0B2641'],
            [13,'Switzerland','#0B2641'],
            [14,'Belgium', '#0B2641'],
            [15,'United Kindgom','#0B2641'],
            [16,'Greece','#0B2641'],
            [17,'France','#0B2641'],
            [18,'Italy','#0B2641'],
            [19,'Spain','#0B2641']]
    
    # Verlinkungen Source und Target mit folgenden Daten 
    links = [['Source','Target','Value','Link Color'],
        
        # Syrien
        [0,10,41060,'rgba(76, 178, 76, 0.35)'], 
        [0,11,5225,'rgba(76, 178, 76, 0.35)'],
        [0,12,3840,'rgba(76, 178, 76, 0.35)'],
        [0,13,1095,'rgba(76, 178, 76, 0.35)'],
        [0,14,2900,'rgba(76, 178, 76, 0.35)'], 
        [0,15,1350,'rgba(76, 178, 76, 0.35)'],
        [0,16,10855,'rgba(76, 178, 76, 0.35)'],
        [0,17,3080,'rgba(76, 178, 76, 0.35)'],
        [0,18,200,'rgba(76, 178, 76, 0.35)'],
        [0,19,2360,'rgba(76, 178, 76, 0.35)'],
        
        # Irak
        [1,10,15325,'rgba(205, 129, 98, 0.35)'], 
        [1,11,1220,'rgba(205, 129, 98, 0.35)'],
        [1,12,930,'rgba(205, 129, 98, 0.35)'],
        [1,13,555,'rgba(205, 129, 98, 0.35)'],
        [1,14,1475,'rgba(205, 129, 98, 0.35)'], 
        [1,15,3970,'rgba(205, 129, 98, 0.35)'],
        [1,16,5740,'rgba(205, 129, 98, 0.35)'],
        [1,17,1370,'rgba(205, 129, 98, 0.35)'],
        [1,18,940,'rgba(205, 129, 98, 0.35)'],
        [1,19,115,'rgba(205, 129, 98, 0.35)'],
        
        # Iran
        [2,10,9490,'rgba(0, 229, 238, 0.35)'],
        [2,11,1115,'rgba(0, 229, 238, 0.35)'],
        [2,12,1785,'rgba(0, 229, 238, 0.35)'],
        [2,13,540,'rgba(0, 229, 238, 0.35)'],
        [2,14,780,'rgba(0, 229, 238, 0.35)'],
        [2,15,5350,'rgba(0, 229, 238, 0.35)'], 
        [2,16,2390,'rgba(0, 229, 238, 0.35)'],
        [2,17,630,'rgba(0, 229, 238, 0.35)'],
        [2,18,7275,'rgba(0, 229, 238, 0.35)'],
        [2,19,195,'rgba(0, 229, 238, 0.35)'],
        
        # Türkei 
        [3,10,11400,'rgba(69, 139, 116, 0.35)'],
        [3,11,660,'rgba(69, 139, 116, 0.35)'],
        [3,12,1285,'rgba(69, 139, 116, 0.35)'],
        [3,13,1280,'rgba(69, 139, 116, 0.35)'],
        [3,14,1075,'rgba(69, 139, 116, 0.35)'],
        [3,15,1260,'rgba(69, 139, 116, 0.35)'],
        [3,16,3795,'rgba(69, 139, 116, 0.35)'],
        [3,17,4515,'rgba(69, 139, 116, 0.35)'],
        [3,18,460,'rgba(69, 139, 116, 0.35)'],
        [3,19,165,'rgba(69, 139, 116, 0.35)'],
        
        # Nigeria
        [4,10,10510,'rgba(220, 142, 59, 0.35)'],
        [4,11,395,'rgba(220, 142, 59, 0.35)'], 
        [4,12,2200,'rgba(220, 142, 59, 0.35)'],
        [4,13,355,'rgba(220, 142, 59, 0.35)'],
        [4,14,200,'rgba(220, 142, 59, 0.35)'],
        [4,15,1395,'rgba(220, 142, 59, 0.35)'], 
        [4,16,215,'rgba(220, 142, 59, 0.35)'],
        [4,17,6390,'rgba(220, 142, 59, 0.35)'],
        [4,18,3515,'rgba(220, 142, 59, 0.35)'],
        [4,19,385,'rgba(220, 142, 59, 0.35)'],
        
        #Afghanistan
        [5,10,11280,'rgba(59, 137, 220, 0.35)'],
        [5,11,905,'rgba(59, 137, 220, 0.35)'],
        [5,12,795,'rgba(59, 137, 220, 0.35)'],
        [5,13,1400,'rgba(59, 137, 220, 0.35)'],
        [5,14,3400,'rgba(59, 137, 220, 0.35)'],
        [5,15,2170,'rgba(59, 137, 220, 0.35)'],
        [5,16,23820,'rgba(59, 137, 220, 0.35)'],
        [5,17,12085,'rgba(59, 137, 220, 0.35)'],
        [5,18,590,'rgba(59, 137, 220, 0.35)'],
        [5,19,130,'rgba(59, 137, 220, 0.35)'],
        
        #Albania 
        [6,10,2565,'rgba(255, 106, 106, 0.35)'],
        [6,11,550,'rgba(255, 106, 106, 0.35)'],
        [6,12,265,'rgba(255, 106, 106, 0.35)'],
        [6,13,140,'rgba(255, 106, 106, 0.35)'],
        [6,14,675,'rgba(255, 106, 106, 0.35)'],
        [6,15,3980,'rgba(255, 106, 106, 0.35)'],
        [6,16,3055,'rgba(255, 106, 106, 0.35)'],
        [6,17,10370,'rgba(255, 106, 106, 0.35)'],
        [6,18,1565,'rgba(255, 106, 106, 0.35)'],
        [6,19,160,'rgba(255, 106, 106, 0.35)'],
        
        #Pakistan 
        [7,10,3400,'rgba(147, 112, 219, 0.35)'],
        [7,11,375,'rgba(147, 112, 219, 0.35)'],
        [7,12,445,'rgba(147, 112, 219, 0.35)'],
        [7,13,100,'rgba(147, 112, 219, 0.35)'],
        [7,14,215,'rgba(147, 112, 219, 0.35)'],
        [7,15,2535,'rgba(147, 112, 219, 0.35)'],
        [7,16,7140,'rgba(147, 112, 219, 0.35)'],
        [7,17,5105,'rgba(147, 112, 219, 0.35)'],
        [7,18,8725,'rgba(147, 112, 219, 0.35)'],
        [7,19,630,'rgba(147, 112, 219, 0.35)'],
        
        #Venezuela 
        [8,10,725,'rgba(255, 215, 0, 0.35)'],
        [8,11,210,'rgba(255, 215, 0, 0.35)'],
        [8,12,200,'rgba(255, 215, 0, 0.35)'],
        [8,13,45,'rgba(255, 215, 0, 0.35)'],
        [8,14,545,'rgba(255, 215, 0, 0.35)'],
        [8,15,30,'rgba(255, 215, 0, 0.35)'],
        [8,16,30,'rgba(255, 215, 0, 0.35)'],
        [8,17,935,'rgba(255, 215, 0, 0.35)'],
        [8,18,1550,'rgba(255, 215, 0, 0.35)'],
        [8,19,40840,'rgba(255, 215, 0, 0.35)'],
        
        #Colombia
        [9,10,465,'rgba(120, 120, 120, 0.35)'],
        [9,11,495,'rgba(120, 120, 120, 0.35)'],
        [9,12,165,'rgba(120, 120, 120, 0.35)'],
        [9,13,120,'rgba(120, 120, 120, 0.35)'],
        [9,14,370,'rgba(120, 120, 120, 0.35)'],
        [9,15,30,'rgba(120, 120, 120, 0.35)'],
        [9,16,0,'rgba(120, 120, 120, 0.35)'],
        [9,17,545,'rgba(120, 120, 120, 0.35)'],
        [9,18,875,'rgba(120, 120, 120, 0.35)'],
        [9,19,29275,'rgba(120, 120, 120, 0.35)'],]
    
    
    # Abrufen von Header und Aufbau des Datenrahmens
    nodes_headers = nodes.pop(0)
    links_headers = links.pop(0)
    df_nodes = pd.DataFrame(nodes, columns = nodes_headers)
    df_links = pd.DataFrame(links, columns = links_headers)
    
    # Eigenschaften fuer Sankey plot
    data_trace = dict(
            type='sankey',
            domain = dict(
                x =  [0,1],
                y =  [0,1]
            ),
            orientation = "h",      # Diagram horizontal
            valueformat = ".0f",    
            
            node = dict(            # Eigenschaften Knoten
                pad = 10,              

            line = dict(            # Eigenschaften Kantenlinien 
                color = "black",    
                width = 0),
                label =  df_nodes['Label'].dropna(axis=0, how='any'),   # Label anzeigen
                color = df_nodes['Color']                               # Kantenfarben
            ),
            link = dict(            # Alle Verlinkungen
                source = df_links['Source'].dropna(axis=0, how='any'),
                target = df_links['Target'].dropna(axis=0, how='any'),
                value = df_links['Value'].dropna(axis=0, how='any'),
                color = df_links['Link Color'].dropna(axis=0, how='any'),
        )
    )
    
    # Eigenschaften Sanky Diagram Layout 
    layout = dict(
            #"Top 10 Verteilung der Asylanträge eines Landes auf die verschiedenen Zielländer"
            title='Top 10 Distribution of a Countries Asylum Applications among the various Countries of Destination  %s' % a,
            height = 700,                   
            font = dict(size = 10),)
    
    fig1 = dict(data=[data_trace], layout=layout)
    
    
#------------Create pie chart-------------------

    # Daten in Liste übergeben
    labels = df['year'].tolist()
    values = df['2019'].tolist()
    #header = st.header('Age Distribution of Asylum Seekers Worldwide %s' % a)
    
    
    fig2 = go.Figure(data=[go.Pie(
        labels=labels, 
        values=values, 
        textinfo='label+percent', 
        insidetextorientation='radial', 
        title='Age Distribution of Asylum Seekers Worldwide %s' % a)])
    

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
        st.plotly_chart(fig2)
    with c2:
        st.plotly_chart(fig1)
    with container:
        st.plotly_chart(fig3)

if __name__ == "__main__":
    write()
    
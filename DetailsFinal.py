import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")
st.markdown("""
<style>
body {
    color: #000;
    background-color: #fff;
    padding: 0px 0px 0px 0px;
}
</style>
    """, unsafe_allow_html=True)

# read CSV
df = pd.read_csv("https://raw.githubusercontent.com/hannahkruck/VIS_Test1/Develop/piechart.csv", encoding ="utf8", sep=";")

st.title("Streamlit Title")
c1, c2 = st.beta_columns((1, 1))
container = st.beta_container()
#https://www.geeksforgeeks.org/sankey-diagram-using-plotly-in-python/
fig1 = go.Figure(data=[go.Sankey( 
		node = dict( 
			thickness = 5, 
			line = dict(color = "blue", width = 0.1), 
			label = ["Deutschland", "Syrien", "Irak", "Türkei", "Afghanistan", "Nigeria", "Iran", "Russland", "Somalia"], 
			
			color = "purple"
		), 
		link = dict( 
			
			# indices correspond to labels 
			source = [1, 2, 3, 4, 5, 6, 7, 8],  
			target = [0, 0, 0, 0, 0, 0, 0, 0], 
			value = [41060, 15325, 11400, 11280, 10510, 9490,4450,4145] 
	))]) 

#sankeyone= st.plotly_chart(fig1)

#df = px.data.gapminder().query("year == 2007").query("continent == 'Americas'")
#fig2 = px.pie(df, values='pop', names='country',
#             title='Population of American continent',
#             hover_data=['lifeExp'], labels={'lifeExp':'life expectancy'})
#fig2.update_traces(textposition='inside', textinfo='percent+label')


#Create pie chart

# Daten in Liste übergeben
labels = df['year'].tolist()
values = df['2019'].tolist()

fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent', insidetextorientation='radial', title='Kuchendiagramm')])


# Create figure 3
fig3 = go.Figure()

# Add traces, one for each slider step
for step in np.arange(0, 5, 0.1):
    fig3.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color='LightSkyBlue', width=3),

            name="𝜈 = " + str(step),
            x=np.arange(0, 10, 0.01),
            y=np.sin(step * np.arange(0, 10, 0.01))))

# Make 10th trace visible
fig3.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig3.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig3.data)},
              {"title": "Slider switched to step: " + str(i)}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Frequency: "},
    pad={"t": 50},
    steps=steps
)]

fig3.update_layout(
    sliders=sliders,
    width=1500
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
   
    
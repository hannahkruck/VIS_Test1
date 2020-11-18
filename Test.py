import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(layout="wide")
st.topbar.header("Titel")

st.title("Streamlit Title")
c1, c2 = st.beta_columns((1, 1))

#Flightdata

df_airports = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df_airports.head()

df_flight_paths = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_aa_flight_paths.csv')
df_flight_paths.head()


#first chart

fig1 = go.Figure()

fig1.add_trace(go.Scattergeo(
    locationmode = 'USA-states',
    lon = df_airports['long'],
    lat = df_airports['lat'],
    hoverinfo = 'text',
    text = df_airports['airport'],
    mode = 'markers',
    marker = dict(
        size = 2,
        color = 'rgb(255, 0, 0)',
        line = dict(
            width = 3,
            color = 'rgba(68, 68, 68, 0)'
        )
    )))
    

lons = []
lats = []
import numpy as np
lons = np.empty(3 * len(df_flight_paths))
lons[::3] = df_flight_paths['start_lon']
lons[1::3] = df_flight_paths['end_lon']
lons[2::3] = None
lats = np.empty(3 * len(df_flight_paths))
lats[::3] = df_flight_paths['start_lat']
lats[1::3] = df_flight_paths['end_lat']
lats[2::3] = None

fig1.add_trace(
    go.Scattergeo(
        locationmode = 'USA-states',
        lon = lons,
        lat = lats,
        mode = 'lines',
        line = dict(width = 1,color = 'red'),
        opacity = 0.5
    )
)

fig1.update_layout(
    title_text = 'Feb. 2011 American Airline flight paths<br>(Hover for airport names)',
    showlegend = False,
    geo = go.layout.Geo(
        scope = 'north america',
        projection_type = 'azimuthal equal area',
        showland = True,
        landcolor = 'rgb(243, 243, 243)',
        countrycolor = 'rgb(204, 204, 204)',
    ),
    height=700,
)


#second chart


df = px.data.gapminder().query("year == 2007").query("continent == 'Americas'")
fig2 = px.pie(df, values='pop', names='country',
             title='Population of American continent',
             hover_data=['lifeExp'], labels={'lifeExp':'life expectancy'})
fig2.update_traces(textposition='inside', textinfo='percent+label')


with c1:
    st.plotly_chart(fig1)
with c2:
    st.plotly_chart(fig2)

#sidebar

st.sidebar.header("Filter")
st.sidebar.multiselect("Where do you work?", ("London", "New York"))
st.sidebar.slider("Age",1,99)

st.markdown("## Party time!")
st.write("Yay! You're done with this tutorial of Streamlit. Click below to celebrate.")
btn = st.button("Celebrate!")
if btn:
    st.balloons()



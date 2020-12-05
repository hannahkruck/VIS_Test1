#!/usr/bin/env python3

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
	
#ast.shared.components.title_awesome("Welcome")      # Titel Awesome_Streamlit ausblenden
	
		st.title("Welcome")
		st.header('Text')
		st.text("Text")
	
		#test = st.sidebar.radio("Map",('Choropleth Map', 'Line Map'))
	
		c1, c2 = st.beta_columns((2, 1))
		container = st.beta_container()
		st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
	
	#https://blog.streamlit.io/introducing-new-layout-options-for-streamlit/
	
		my_expander = st.beta_expander("Click me to see what happens", expanded=False)
		with my_expander:
			#st.sidebar.title("Click2")
			selectedGender = st.radio("Radiobuttons", ("1", "2", "3"))
			selectYear = st.slider("Testslider", 2010, 2019)
			infoText = st.text("Freut mich das du mehr Informationen haben willst")
			my_expander = st.sidebar((selectedGender)) 
			
			
		# my_expander1 = st.beta_expander("Test", expanded=True)
		# st.beta_expander = st.sidebar("Test")
		# with st.sidebar:
		#     clicked = st.sidebar.radio("Clfefick")
		#     selectedGender = st.sidebar.multiselect("Select Gender", ("All", "Male", "Female"))
		#     my_expander = st.beta_expander(st.sidebar(selectedGender), expanded=True)   
			
			
			
		with c1:
			st.plotly_chart(fig2)
		with c2:
			st.plotly_chart(fig1)
		with container:
			st.plotly_chart(fig3)
			
			
if __name__ == "__main__":
	write()
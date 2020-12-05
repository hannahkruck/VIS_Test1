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
	
	st.title("Titel")
	st.header('Header')
	st.subheader('Subheader')
	st.text("Text")

	#Expander - Wenn unter titel dann muss es ueber Spalten erstellen stehen
	my_expander = st.beta_expander("Click me to see what happens", expanded=False)
	with my_expander:
		#selectedRadio = st.radio("Radiobuttons", ("1", "2", "3"))
		#my_expander = st.sidebar((selectedRadio))
		selectYear = st.slider("Testslider   ", 2010, 2019)
		infoText = st.text("Freut mich das du mehr Informationen haben willst")
		selectedBoxes = st.multiselect("Map", ("Choro", "Line"))
		#test = st.sidebar.radio("Map",('Choropleth Map', 'Line Map'))
		
		
	c1, c2 = st.beta_columns((1,1))
	container = st.beta_container()
	st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
	
	c1.info('Ich bin eine Info message Spalte1')
	#c1.text("Ich bin ein Text Spalte1")
	
	c2.success("Ich bin wichtig Spalte2")

	

	# my_expander1 = st.beta_expander("Test", expanded=True)
	# st.beta_expander = st.sidebar("Test")
	# with st.sidebar:
	#     clicked = st.sidebar.radio("Test")
	#     selectedGender = st.sidebar.multiselect("Select Gender", ("All", "Male", "Female"))
	#     my_expander = st.beta_expander(st.sidebar(selectedGender), expanded=True)   
				
				
				
				
				
			
			
if __name__ == "__main__":
	write()
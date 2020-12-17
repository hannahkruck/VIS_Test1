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
	
# CSS Startseite
	st.markdown("""
	<style>
	body {
		color: black;
		font-color: black;
		background-color: white;
	}

	h3 {
		color: #1878a1;
	}
	</style>
    """, unsafe_allow_html=True)

	st.title("Willkommen bei (TOOLNAME)")

# HTML Inhalt
	html = """
	<h3>"Toolname" ist ein Visualisierungstool ..." <br>
	Ziel<br>
	Was kann Tool alles zeigen<br>
	Welche Optionen haben Nutzer</h3>
	
	<hr>
	<br>
	"""
	st.markdown(html, unsafe_allow_html=True)
	
	#Expander - Wenn unter titel dann muss es ueber Spalten erstellen stehen
	my_expander_one = st.beta_expander("Woher stammen die Daten?", expanded=False)
	with my_expander_one:
		html_one = """ 
			<p> Die Daten stammen aus der ... </p>
			Datensatz: <a target="_blank" href="https://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=migr_asyappctza&lang=de">Asylbewerber und erstmalige Asylbewerber nach Staatsangehörigkeit, Alter und Geschlecht - jährliche aggregierte Daten (gerundet)<br></a>
			<br>"""
		st.markdown(html_one, unsafe_allow_html=True)


	#Expander - Wenn unter titel dann muss es ueber Spalten erstellen stehen
	my_expander_two = st.beta_expander("Wer ist die Zielgruppe?", expanded=False)
	with my_expander_two:
		html_two = """ 
			<p> Die Zielgruppe ... (Experten, Laien?) </p>"""
		st.markdown(html_two, unsafe_allow_html=True)


	#Expander - Wenn unter titel dann muss es ueber Spalten erstellen stehen
	my_expander_three = st.beta_expander("Umsetzung des Visualisierungstools", expanded=False)
	with my_expander_three:
		html_three = """ 
			<p> Mit Streamlit, Bibliotheken, HTML, CSS </p>"""
		st.markdown(html_three, unsafe_allow_html=True)

	#Expander - Wenn unter titel dann muss es ueber Spalten erstellen stehen
	my_expander_four = st.beta_expander("Expander 4", expanded=False)
	with my_expander_four:
		html_four = """ 
			<p> Inhalt </p>"""
		st.markdown(html_four, unsafe_allow_html=True)
		
		
	c1, c2 = st.beta_columns((1,1))
	container = st.beta_container()
	st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
	
	c1.info('Ich bin eine Info message Spalte1')
	#c1.text("Ich bin ein Text Spalte1")
	
	c2.success("Ich bin wichtig Spalte2")

	

				
				
			
			
if __name__ == "__main__":
	write()
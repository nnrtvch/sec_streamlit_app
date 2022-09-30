import streamlit as lit
import pandas as pd
import requests
import snowflake.connector

my_cnx = snowflake.connector.connect(**lit.secrets["snowflake"])
my_cur = my_cnx.cursor()

                                   
my_cur.execute("select color_or_style from catalog_for_website")
color_catalogue = my_cur.fetchall()

df = pd.DataFrame(color_catalogue)

color_list = df[0].values.tolist()

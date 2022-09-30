import streamlit as lit
import requests
import snowflake.connector
import pandas as pd

lit.title("Zena's Amazing Athleisure Catalog")


my_cnx = snowflake.connector.connect(**lit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_data_row_2 =  my_cur.execute("select distinct color_or_style from catalog")
df = pd.DataFrame(my_data_row_2)
color_list = df[0].values.tolist()

option = lit.selectbox('Pick a sweatsuit color or style:', list(color_list))
product_caption = 'Our warm, comfortable, ' + option + ' sweatsuit!'

my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + option + "'")
df2 = my_cur.fetchone()

lit.image(
  df2[0],
  width=400,
  caption= product_caption
)


lit.stop()

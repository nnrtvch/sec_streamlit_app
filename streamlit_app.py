import streamlit as lit
import requests
import snowflake.connector

lit.title("Zena's Amazing Athleisure Catalog")

lit.header("View Our Fruit List - Add Your Favorites!")

def get_color_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select distinct color_or_style from catalog")
    return my_cur.fetchall()
  
if lit.button('Get fruit list'):
  my_cnx = snowflake.connector.connect(**lit.secrets["snowflake"])
  my_data_row = get_color_list()
  my_cnx.close()
  ert = list(my_data_row)
  lit.dataframe(ert)

my_cnx = snowflake.connector.connect(**lit.secrets["snowflake"])
my_data_row_2 = get_color_list()
my_cnx.close()
fruits_selected  = lit.multiselect('Pick some fruits: ', list(my_data_row_2))
fruits_to_show = my_fruit_list.loc[fruits_selected]
lit.dataframe(fruits_to_show)
lit.stop()
  
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


fruits_to_show = my_fruit_list.loc[fruits_selected]
lit.dataframe(fruits_to_show)



my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected  = lit.multiselect('Pick some fruits: ', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
lit.dataframe(fruits_to_show)

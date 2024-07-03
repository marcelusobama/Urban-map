import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.title("Mapa com Dados")
m = leafmap.Map(google_map="HYBRID",center=[-15.83, -47.86], zoom=10)
in_geojson = "https://github.com/marcelusobama/Urban-map/blob/master/Cadastro_Ambiental_Rural_-_Perimetro.geojson"
m.add_geojson(in_geojson, layer_name="Cable lines")

m.to_streamlit(height=700)

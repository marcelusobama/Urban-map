import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")


st.title("Mapa com Dados")



m = leafmap.Map(center=[0, 0], zoom=2)

in_geojson = "https://raw.githubusercontent.com/opengeos/leafmap/master/examples/data/cable_geo.geojson"
m.add_geojson(in_geojson, layer_name="Cable lines")

m
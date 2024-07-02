import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")


st.title("Mapa de Calor")

with st.expander("See source code"):
    with st.echo():
       filepath = "https://raw.githubusercontent.com/marcelusobama/Urban-map/master/br_cidades.csv"
m = leafmap.Map(center=[-15, -48], zoom=4)
m.add_heatmap(
    filepath,
    latitude="latitude",
    longitude="longitude",
    value="pop_max",
    name="Heat map",
    radius=20,
)
m.to_streamlit(height=700)

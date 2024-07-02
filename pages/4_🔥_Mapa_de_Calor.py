import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")


st.title("Mapa de Calor")

with st.expander("See source code"):
    with st.echo():
       filepath = "https://github.com/marcelusobama/Urban-map/blob/master/Data/br_cidades.csv"
m = leafmap.Map(center=[-15, -48], zoom=4)
m.add_heatmap(
    filepath,
    latitude="latitude",
    longitude="longitude",
    value="pop_max",
    name="Heat map",
    radius=10,
)
        
      
m.to_streamlit(height=700)

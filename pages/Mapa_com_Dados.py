import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")
st.title("Mapa com Dados")
m = leafmap.Map(google_map="HYBRID",center=[-15.83, -47.86], zoom=10)
in_geojson = "https://ide.geobases.es.gov.br/geoserver/ows?service=WFS&version=1.0.0&request=GetFeature&typename=geonode%3AAREA_IMOVEL_1&outputFormat=json&srs=EPSG%3A31984&srsName=EPSG%3A31984"
m.add_geojson(in_geojson, layer_name="Cable lines")

m.to_streamlit(height=700)

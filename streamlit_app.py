import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Aplicativo Criado em Pyhthon - BrisaGeo
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://brisageo.com.br/wp-content/uploads/2023/08/222.png"
st.sidebar.image(logo)

# Customize page title
st.title("Aplicação Geoespacial")


st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)

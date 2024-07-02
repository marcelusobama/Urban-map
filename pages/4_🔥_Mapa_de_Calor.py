import streamlit as st
import leafmap.leafmap as leafmap

# Modificação do endereço do link
filepath = "https://github.com/marcelusobama/Urban-map/blob/master/MunicipiosBrasil.csv"

with st.expander("See source code"):
    with st.echo():
        # Inicialização do mapa com centro e zoom definidos
        m = leafmap.Map(center=[-14.235, -51.9253], zoom=4)  # Ajustando o centro para o Brasil

        # Adicionando o heatmap ao mapa
        m.add_heatmap(
            filepath,
            latitude="latitude",
            longitude="longitude",
            value="region",  # Ajuste conforme os dados no CSV
            name="Heat map",
            radius=20,
        )

        # Exibindo o mapa no Streamlit
        m.to_streamlit(height=700)

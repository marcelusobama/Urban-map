import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")


st.title("Comparação de Mapas")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map(google_map="HYBRID", center=[-15.83, -47.86], zoom=4)
        m.split_map(
            left_layer='ESA WorldCover 2020 S2 FCC', right_layer='ESA WorldCover 2020'
        )
        legend_dict = {
    'Floresta Tropical': '#006400',
    'Arbustivo' : 'FFBB22',
    'Pastagem': 'FFFF4C',
    'Terras Cultivadas': 'F096FF',
    'Corpos de água permanentes': '0064C8',
    'Construído' : 'FA0000',
    'Manguezais' : '00CF75',    
    # Adicione outras categorias e cores conforme necessário
}

m.add_legend(title='Cobertura da Terra ESA', legend_dict=legend_dict)
        

m.to_streamlit(height=700)

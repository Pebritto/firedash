import streamlit as st
from streamlit_option_menu import option_menu
from common import set_page_container_style

set_page_container_style(
    max_width = 1100, max_width_100_percent = True,
    padding_top = 0, padding_right = 10, padding_left = 5, padding_bottom = 10
)

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: 'firedash-logo.png';
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "My Company Name";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

with st.sidebar:
    
    # st.markdown("""<style> your css </style>""" , unsafe_allow_html=True)
    st.image('firedash-logo.svg', width=200)
    selected = option_menu(
        menu_title=None,
        options=['Home', 'Dashboard', 'About Us'],
        icons=['house-door-fill', 'bar-chart-fill', 'people-fill'],
        menu_icon='cast',
        default_index=0,
        styles={
            'container': {'padding': '0!important', 'background-color': 'None'},
            'icon': {'color': '#F3F3F3'},
            'nav-link': {
                'font-size': '18px',
                'text-align': 'left',
                'margin': '10px',
                '--hover-color': '#7802D6',
            },
            'nav-link-selected': {
                'background-color': '#7802D6',
            },
        },
    )

st.header('Firedash', anchor=False)

if selected == 'Home':
    st.subheader('Maiores altas do dia', anchor=False)
if selected == 'Dashboard':
    st.subheader('Veja todas as ações do em tempo real', anchor=False)
if selected == 'About Us':
    st.subheader('Conheça nosso projeto!', anchor=False)

st.button('Botão Primário', type='primary')
st.button('Botão Secundário', type='secondary')
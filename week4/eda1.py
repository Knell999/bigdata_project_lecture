import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

def run_eda_home():
    st.markdown("### 탐색적 자료 분석 개요\n"
                "탐색적 자료 분석 페이지 입니다."
                "여기에 포함하고 싶은 내용을 넣을 수 있습니다")
    
    selected = option_menu(None, ['Home', 'Visualization', 'Statistics', 'Map'],
                           icons=['house', 'bar-chart', 'file-spreadsheet', 'map'],
                           menu_icon='cast', default_index=0, orientation='horizontal',
                           styles={
                               'container' : {
                                   'padding' : '0!important',
                                   'background-color' : '#808080'},
                                'icon' : {
                                    'color' : 'orange',
                                    'font-size' : '25px'},
                                'nav-link' : {
                                    'font-size' : '15px',
                                    'text-align' : 'left',
                                    'margin' : '0px',
                                    '--hover-color' : '#eee'},
                                'nav-link-selected' : {
                                    'background-color' : 'green'}
                                })
if selected == 'Home' :
    pass
elif selected == 'Visualization' :
    pass
elif selected == 'Statistics' :
    pass
elif selected == 'Map' :
    pass
else:
    st.warning('Wrong')
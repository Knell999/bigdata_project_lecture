import streamlit as st
import pandas as pd
from plotly.subplots import make_subplots
import plotly.express as px

def showViz(total_df) :
    total_df['DEAL_YMD'] = pd.to_datetime(total_df['DEAL_YMD'], format='%Y-%m-%d')

    sgg_nm = st.sidebar.selectbox('자치구명', sorted(total_df['SGG_NM'].unique()))
    selected = st.sidebar.radio('차트메뉴',
                                ['가구당 평균 가격 추세', '가구당 거래 건수', '지역별 평균 가격 막대 그래프'])
    if selected == '가구당 평균 가격 추세' :
        pass
    elif selected == '가구당 거래 건수' :
        pass
    elif selected == '지역별 평균 가격 막대 그래프' :
        pass
    else :
        st.warning("Error")
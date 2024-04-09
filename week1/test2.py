import streamlit as st
from streamlit_option_menu import option_menu

def run_home() :

    st.markdown("## 대시보드 개요 \n"
                "본 프로젝트는 서울시 부동산 실거래가를 알려주는 대시보드입니다."
                "여기에 추가하고 싶은 내용을 추가하면 됩니다.")
    
    sgg_nm = st.sidebar.selectbox("자치구", ['구로구', '영등포구', '관악구'])

    acc_year = st.sidebar.selectbox("년도", [2023, 2024])

    month_dic = {'1월' : 1, '2월' : 2, '3월' : 3, '4월' : 4, '5월' : 5, '6월' : 6,
                 '7월' : 7, '8월' : 8, '9월' : 9, '10월' : 10, '11월' : 11, '12월' : 12}
    
    select_month = st.sidebar.selectbox("확인하고 싶은 월을 선택하세요", list(month_dic.keys()))

    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader(f'{sgg_nm} {acc_year}년 {select_month} 아파트 가격 개요')
    st.markdown('자치구와 월을 클릭하면 자동으로 각 지역구에서 거래된 **최소가격**, **최대가격**을 확인할 수 있습니다.')

def main() :
 
    with st.sidebar:
        selected = option_menu('대시보드 메뉴', ['홈', '탐색적 자료분석', '부동산 예측'],
            icons=['house', 'file-bar_graph', 'graph-up-arrow'], menu_icon='cast', default_index=0)
 
    if selected == '홈':
        pass
    elif selected == '탐색적 자료분석' :
        run_home()
    elif selected == '부동산 예측' :
        pass
    else :
        print('error')
 
if __name__ == "__main__":
    main()

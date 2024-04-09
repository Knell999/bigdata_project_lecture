import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# 스트림릿 앱의 사이드바에 날짜 선택 위젯 추가
selected_date = st.sidebar.date_input("날짜를 선택하세요", datetime.today())

# API 키와 기타 필요한 변수 설정
KEY = '657057486963726136396863684441'
TYPE = 'json'  # 예시에서는 json 형식으로 고정
SERVICE = 'TbUseDaystatusView'

# 스트림릿 앱의 메인 화면에 선택된 날짜 표시
st.write(f"선택된 날짜: {selected_date.strftime('%Y-%m-%d')}")

# API URL 구성
url = f'http://openapi.seoul.go.kr:8088/{KEY}/{TYPE}/{SERVICE}/1/1000'

# API 요청 및 응답 처리
try:
    response = requests.get(url)
    if response.status_code == 200:
        content = response.json()
        con = content[SERVICE]['row']
        result = pd.DataFrame(con)

        # 'DT' 열이 선택된 날짜와 일치하는 데이터만 필터링
        # 'DT' 열의 날짜 형식을 'YYYY/MM/DD'로 가정
        formatted_date = selected_date.strftime('%Y/%m/%d')
        result_filtered = result[result['DT'] == formatted_date]

        # 사용량 평균 계산
        result_filtered['USE_MEAN'] = result_filtered['USE_MIN'].astype(float) / result_filtered['USE_CNT'].astype(float)

        # 평균사용시간 기준 내림차순으로 데이터 정렬
        result_sorted = result_filtered.sort_values(by='USE_MEAN', ascending=False)

        # 결과 데이터 프레임 스트림릿 앱에 표시
        st.write(result_sorted)
    else:
        st.error("API 요청 오류")
except Exception as e:
    st.error(f"오류 발생: {e}")

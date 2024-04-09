import streamlit as st
import requests
import pandas as pd
import xml.etree.ElementTree as ET

def fetch_apartment_sales(lawd_cd, deal_ym):
    serviceKey = 'PT7s57yQ6NYjF%2BK4IX03RFJISja7dPlVceXQn7%2Fm2DWnibRv2u9288PJ6m9t4hi6sH2A%2B8fa8AGF3nDiGmeZRw%3D%3D'
    url = f"http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?serviceKey={serviceKey}&LAWD_CD={lawd_cd}&DEAL_YMD={deal_ym}&pageNo=1&numOfRows=100"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            root = ET.fromstring(response.content)
            items = []
            for item in root.findall('.//item'):
                items.append({child.tag: child.text for child in item})
            df = pd.DataFrame(items)
            return df[['년','월','일','도로명','거래금액']]
        except Exception as e:
            st.error(f"Error parsing response: {e}")
            return pd.DataFrame()
    else:
        st.error("Failed to fetch data from API")
        return pd.DataFrame()

def main():
    st.sidebar.title("검색 옵션")

    region_dict = {'구로구': '11530', '영등포구': '11560', '양천구': '11470'}
    region = st.sidebar.selectbox("지역 선택", list(region_dict.keys()))
    year = st.sidebar.number_input("년도 입력", min_value=2000, max_value=2024, value=2023)
    month = st.sidebar.selectbox("월 선택", list(range(1, 13)))

    if st.sidebar.button("검색"):
        lawd_cd = region_dict[region]
        deal_ym = f"{year}{month:02d}"
        result_df = fetch_apartment_sales(lawd_cd, deal_ym)
        if not result_df.empty:
            st.write(f"## {region}, {year}년 {month}월 매매 거래 정보")
            st.dataframe(result_df, width=1200)
        else:
            st.write("검색 결과가 없습니다.")

if __name__ == "__main__":
    main()
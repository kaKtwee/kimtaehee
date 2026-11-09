import streamlit as st
import pandas as pd
import numpy as np

# 여기서부터 자유롭게 작성하세요

# 페이지 설정
st.set_page_config(
    page_title="삼성SDS 주가 대시보드",
    page_icon="📈",
    layout="wide"
)

# 제목
st.title("관심 있는 주식 - 삼성SDS")
st.write("제가 관심 있는 주식인 삼성SDS의 주가 정보를 살펴보는 대시보드입니다.")

# 예시 데이터
# 실제 주가 데이터가 아닌 Streamlit 실습을 위한 예시 데이터입니다.
data = {
    "날짜": [
        "11/03", "11/04", "11/05",
        "11/06", "11/07", "11/08", "11/09"
    ],
    "종가": [
        170000, 172000, 171000,
        174000, 176000, 175000, 178000
    ],
    "거래량": [
        120000, 145000, 110000,
        160000, 180000, 140000, 190000
    ]
}

df = pd.DataFrame(data)

# 전날 대비 등락률 계산
df["등락률(%)"] = df["종가"].pct_change() * 100
df["등락률(%)"] = df["등락률(%)"].round(2)

st.divider()

# 데이터 확인
st.subheader("삼성SDS 주가 데이터")
st.caption("※ 아래 데이터는 Streamlit 실습을 위해 만든 예시 데이터입니다.")
st.dataframe(df, use_container_width=True)

st.divider()

# 날짜 선택
st.subheader("날짜별 주가 확인")

selected_date = st.selectbox(
    "확인하고 싶은 날짜를 선택하세요.",
    df["날짜"]
)

selected_data = df[df["날짜"] == selected_date].iloc[0]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="종가",
        value=f"{selected_data['종가']:,.0f}원"
    )

with col2:
    st.metric(
        label="거래량",
        value=f"{selected_data['거래량']:,.0f}주"
    )

with col3:
    if pd.isna(selected_data["등락률(%)"]):
        st.metric(
            label="전일 대비 등락률",
            value="-"
        )
    else:
        st.metric(
            label="전일 대비 등락률",
            value=f"{selected_data['등락률(%)']:.2f}%"
        )

st.divider()

# 조회 기간 설정
st.subheader("조회 기간 설정")

days = st.slider(
    "최근 며칠의 데이터를 확인할까요?",
    min_value=3,
    max_value=7,
    value=7
)

filtered_df = df.tail(days)

# 차트 종류 선택
chart_type = st.radio(
    "확인하고 싶은 차트를 선택하세요.",
    ["주가", "거래량"],
    horizontal=True
)

if chart_type == "주가":
    st.write(f"최근 {days}일 삼성SDS 주가")
    
    chart_df = filtered_df.set_index("날짜")[["종가"]]
    st.line_chart(chart_df)

else:
    st.write(f"최근 {days}일 삼성SDS 거래량")
    
    chart_df = filtered_df.set_index("날짜")[["거래량"]]
    st.bar_chart(chart_df)

st.divider()

# 관심 가격 설정
st.subheader("나의 관심 가격")

target_price = st.slider(
    "삼성SDS의 관심 가격을 설정하세요.",
    min_value=150000,
    max_value=200000,
    value=175000,
    step=1000
)

current_price = df.iloc[-1]["종가"]

st.write(f"관심 가격: **{target_price:,}원**")
st.write(f"최근 예시 주가: **{current_price:,}원**")

if current_price < target_price:
    st.success("현재 주가가 관심 가격보다 낮습니다.")
elif current_price > target_price:
    st.warning("현재 주가가 관심 가격보다 높습니다.")
else:
    st.info("현재 주가와 관심 가격이 같습니다.")

st.divider()

# 간단한 분석
st.subheader("삼성SDS 주가 간단 분석")

highest_price = df["종가"].max()
lowest_price = df["종가"].min()
average_price = df["종가"].mean()

st.write(f"기간 중 최고가: **{highest_price:,.0f}원**")
st.write(f"기간 중 최저가: **{lowest_price:,.0f}원**")
st.write(f"기간 중 평균 종가: **{average_price:,.0f}원**")

if df.iloc[-1]["종가"] > df.iloc[0]["종가"]:
    st.write("예시 데이터에서는 처음보다 마지막 날의 주가가 상승했습니다.")
elif df.iloc[-1]["종가"] < df.iloc[0]["종가"]:
    st.write("예시 데이터에서는 처음보다 마지막 날의 주가가 하락했습니다.")
else:
    st.write("예시 데이터에서는 처음과 마지막 날의 주가가 같습니다.")

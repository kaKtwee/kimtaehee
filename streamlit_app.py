import streamlit as st
import pandas as pd
import numpy as np

# ── 여기서부터 자유롭게 수정하세요 ───────────────

st.title("나의 생활 양식 대시보드")   # ← 제목을 바꿔보세요

# ── 사이드바 ──────────────────────────────────
st.sidebar.title("설정")

chart_type = st.sidebar.radio(
    "차트 유형",
    ["면적 그래프", "막대 그래프"]   # ← 유형을 바꿔보세요
)

n = st.sidebar.slider(
    "데이터 개수",
    min_value=0,    # ← 최솟값을 바꿔보세요
    max_value=24,   # ← 최댓값을 바꿔보세요
    value=30
)

# ── 메인 화면 ─────────────────────────────────
st.write("원하는 항목의 시간을 조절해 그래프로 비교해보세요.")   # ← 설명을 바꿔보세요

data = pd.DataFrame(
    np.random.randn(n, 3),
    columns=['공부', '수면', '동아리']   # ← 컬럼 이름을 바꿔보세요
)

if  chart_type == "막대 그래프":
    st.bar_chart(data)
else:
    st.area_chart(data)

st.dataframe(data.head(5))

# ── 여기까지 ──────────────────────────────────

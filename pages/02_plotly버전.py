import streamlit as st
import pandas as pd
import plotly.express as px

# CSV 파일 읽기
data = pd.read_csv('countriesMBTI_16types.csv')

# 앱 제목
st.title("MBTI 비율에 따른 나라별 분석")

# MBTI 유형 선택
mbti_type = st.selectbox("MBTI 유형을 선택하세요", data.columns[1:])

# MBTI 비율이 높은 10개 나라
top_10_countries = data[['Country', mbti_type]].sort_values(by=mbti_type, ascending=False).head(10)

# MBTI 비율이 낮은 10개 나라
bottom_10_countries = data[['Country', mbti_type]].sort_values(by=mbti_type, ascending=True).head(10)

# 첫 번째 그래프: MBTI 비율이 높은 10개 나라
st.subheader(f"MBTI 유형 {mbti_type} 비율이 가장 높은 10개 나라")
fig_top = px.bar(top_10_countries, x='Country', y=mbti_type,
                 title=f"{mbti_type} 비율이 높은 10개 나라",
                 labels={'Country': '나라', mbti_type: f'{mbti_type} 비율'})
st.plotly_chart(fig_top)

# 두 번째 그래프: MBTI 비율이 낮은 10개 나라
st.subheader(f"MBTI 유형 {mbti_type} 비율이 가장 낮은 10개 나라")
fig_bottom = px.bar(bottom_10_countries, x='Country', y=mbti_type,
                    title=f"{mbti_type} 비율이 낮은 10개 나라",
                    labels={'Country': '나라', mbti_type: f'{mbti_type} 비율'})
st.plotly_chart(fig_bottom)

import streamlit as st
import pandas as pd
import altair as alt

# 데이터 로드
data = pd.read_csv('countriesMBTI_16types.csv')

# MBTI 유형 리스트
mbti_types = data.columns[1:]

# Streamlit 앱의 제목
st.title("MBTI 비율에 따른 국가 분석")

# MBTI 유형 선택
mbti_selected = st.selectbox('MBTI 유형을 선택하세요:', mbti_types)

# 선택한 MBTI 유형에 대한 데이터를 가져오기
mbti_data = data[['Country', mbti_selected]]

# MBTI 비율이 가장 높은 10개 국가
top_10 = mbti_data.sort_values(by=mbti_selected, ascending=False).head(10)

# MBTI 비율이 가장 낮은 10개 국가
bottom_10 = mbti_data.sort_values(by=mbti_selected, ascending=True).head(10)

# 가장 높은 국가들에 대한 막대 그래프
st.subheader(f"{mbti_selected} 비율이 가장 높은 10개 국가")
top_chart = alt.Chart(top_10).mark_bar().encode(
    x=alt.X(f'{mbti_selected}:Q', title=f'{mbti_selected} 비율'),
    y=alt.Y('Country:N', sort='-x', title='국가'),
    color=alt.Color(f'{mbti_selected}:Q', scale=alt.Scale(scheme='blues')),
    tooltip=['Country', f'{mbti_selected}:Q']
).properties(width=600, height=400)

st.altair_chart(top_chart, use_container_width=True)

# 가장 낮은 국가들에 대한 막대 그래프
st.subheader(f"{mbti_selected} 비율이 가장 낮은 10개 국가")
bottom_chart = alt.Chart(bottom_10).mark_bar().encode(
    x=alt.X(f'{mbti_selected}:Q', title=f'{mbti_selected} 비율'),
    y=alt.Y('Country:N', sort='-x', title='국가'),
    color=alt.Color(f'{mbti_selected}:Q', scale=alt.Scale(scheme='reds')),
    tooltip=['Country', f'{mbti_selected}:Q']
).properties(width=600, height=400)

st.altair_chart(bottom_chart, use_container_width=True)

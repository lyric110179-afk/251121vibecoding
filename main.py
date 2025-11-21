import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천🎯", page_icon="✨")

# MBTI별 진로 추천 데이터
careers = {
    "ISTJ": [
        ("📊 회계사", "수치 분석과 정확성을 중시하는 직업으로 ISTJ의 꼼꼼함을 최대 발휘"),
        ("⚖️ 군인", "규율과 책임감이 중요한 환경에서 뛰어난 조직력 발휘"),
        ("🏛️ 공무원", "안정적이고 체계적인 구조를 선호하는 성향에 잘 맞는 분야")
    ],
    "ISFJ": [
        ("🏥 간호사", "타인을 돕고 배려하는 능력으로 환자 케어에 강점"),
        ("🍎 초등교사", "학생 한 명 한 명을 세심하게 돌보는 데 탁월"),
        ("🤝 사회복지사", "현장에서 사회적 약자를 보호하고 지원")
    ],
    # ... 다른 MBTI 유형도 동일한 구조로 추가 ...
}

# 상세 설명 페이지 함수
def show_details(mbti, job, desc):
    st.header(f"{mbti} - {job}")
    st.write(desc)
    st.markdown("---")
    st.button("뒤로 가기", on_click=st.session_state.pop)

# 메인 페이지
st.title("✨ MBTI 진로 추천 웹 앱 ✨")

selected_mbti = st.selectbox("당신의 MBTI를 선택하세요!", list(careers.keys()))

if st.button("진로 추천 보기 🚀"):
    st.session_state["selected"] = selected_mbti

if "selected" in st.session_state:
    mbti = st.session_state["selected"]
    st.subheader(f"{mbti} 유형에게 어울리는 TOP 3 진로! 💡")

    for i, (job, desc) in enumerate(careers[mbti]):
        if st.button(f"{i+1}. {job}"):
            st.session_state["detail"] = (mbti, job, desc)
            
if "detail" in st.session_state:
    mbti, job, desc = st.session_state["detail"]
    show_details(mbti, job, desc)

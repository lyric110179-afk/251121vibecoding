import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천", page_icon="🎯")

st.title("🎯 MBTI 기반 진로 추천")
st.write("당신의 성향에 맞는 진로 3가지를 추천해드립니다!")

mbti = st.selectbox(
    "MBTI 유형을 선택하세요 👇",
    ["ISTJ", "ISFJ", "INFJ", "INTJ",
     "ISTP", "ISFP", "INFP", "INTP",
     "ESTP", "ESFP", "ENFP", "ENTP",
     "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
)

careers = {
    "ISTJ": ["공무원 🏛️", "회계사 📊", "데이터 분석가 📈"],
    "ISFJ": ["간호사 🏥", "교사 👩‍🏫", "행정 사무원 🗂️"],
    "INFJ": ["심리 상담사 🧠", "작가 ✍️", "사회 연구원 🔍"],
    "INTJ": ["연구개발자 🔬", "전략기획가 🧩", "엔지니어 ⚙️"],
    "ISTP": ["정비사 🔧", "파일럿 ✈️", "보안 전문가 🔐"],
    "ISFP": ["패션 디자이너 👗", "작곡가 🎶", "일러스트레이터 🎨"],
    "INFP": ["에디터 📝", "사회복지사 🤝", "콘텐츠 크리에이터 🎥"],
    "INTP": ["AI 연구자 🤖", "수학자 ➗", "개발자 💻"],
    "ESTP": ["기업가 🚀", "스포츠 트레이너 🏋️‍♂️", "세일즈 🛍️"],
    "ESFP": ["배우 🎭", "아나운서 🎙️", "이벤트 기획자 🎉"],
    "ENFP": ["광고기획자 📣", "작가 ✒️", "인사담당자 🧑‍💼"],
    "ENTP": ["스타트업 창업자 🚀", "비즈니스 컨설턴트 💼", "방송인 📺"],
    "ESTJ": ["경영관리자 📋", "프로젝트 매니저 🧱", "군 장교 🎖️"],
    "ESFJ": ["초등교사 📚", "간호사 🩺", "조직관리자 🧩"],
    "ENFJ": ["교육 컨설턴트 🧑‍🏫", "홍보전문가 📢", "인권운동가 ✊"],
    "ENTJ": ["CEO 🏢", "투자분석가 💹", "국제정치 분석가 🌍"]
}

if mbti:
    st.subheader(f"✨ {mbti} 유형 추천 진로")
    for c in careers.get(mbti, []):
        st.write(f"- {c}")

st.markdown("—")
st.caption("📚 참고: 16Personalities Career Paths")
st.markdown("[16Personalities Career Paths](https://www.16personalities.com/career-paths)")

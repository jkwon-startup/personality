import streamlit as st
from utils.analysis import analyze_personality, get_zodiac_sign

@st.cache_data
def load_data():
    # 여기에 필요한 데이터 로딩 로직을 추가할 수 있습니다.
    pass

def main():
    # 페이지 설정
    st.set_page_config(page_title="귀여운 성격 분석기", page_icon="🐾", layout="wide")

    # 제목
    st.title("🌟 귀여운 성격 분석기 🌟")
    st.write("생년월일, 혈액형, MBTI를 입력하여 귀여운 성격 분석을 받아보세요!")

    # 사용자 입력
    col1, col2, col3 = st.columns(3)

    with col1:
        birth_month = st.selectbox("태어난 월", range(1, 13))
        birth_day = st.selectbox("태어난 일", range(1, 32))

    with col2:
        blood_type = st.selectbox("혈액형", ["A", "B", "O", "AB"])

    with col3:
        mbti = st.selectbox("MBTI", ["ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP", 
                                     "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"])

    # 분석 버튼
    if st.button("성격 분석하기"):
        try:
            zodiac_sign = get_zodiac_sign(birth_month, birth_day)
            analysis_result = analyze_personality(zodiac_sign, blood_type, mbti)
            
            display_analysis_result(zodiac_sign, blood_type, mbti, analysis_result)
        except Exception as e:
            st.error(f"분석 중 오류가 발생했습니다: {str(e)}")

    # 추가 정보
    display_additional_info()

    # 푸터
    st.markdown("---")
    st.markdown("© 2024 귀여운 성격 분석기. 모든 분석 결과는 재미로만 봐주세요! 🎉")

@st.cache_data
def display_analysis_result(zodiac_sign, blood_type, mbti, analysis_result):
    st.header("🎨 당신의 성격 분석 결과")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader(f"🌠 {zodiac_sign} 특성")
        for trait in analysis_result['zodiac']:
            st.write(f"✨ {trait}")
    
    with col2:
        st.subheader(f"🩸 {blood_type}형 특성")
        for trait in analysis_result['blood_type']:
            st.write(f"💉 {trait}")
    
    with col3:
        st.subheader(f"🧠 {mbti} 특성")
        for category, traits in analysis_result['mbti'].items():
            st.write(f"📊 {category}:")
            for trait in traits:
                st.write(f"🔹 {trait}")
    
    st.header("🌈 종합 분석 및 조언")
    for advice in analysis_result['advice']:
        st.write(f"🌟 {advice}")

def display_additional_info():
    with st.expander("성격 유형에 대해 더 알아보기"):
        st.write("🔮 별자리: 천체의 위치에 따른 성격 특성을 나타냅니다.")
        st.write("💉 혈액형: 혈액형에 따른 성격 특성을 나타냅니다.")
        st.write("🧠 MBTI: 개인의 선호도에 따른 16가지 성격 유형을 나타냅니다.")

    with st.expander("성격 개발 팁"):
        st.write("🌱 자기 이해: 자신의 장단점을 인식하고 받아들이세요.")
        st.write("🤝 소통 능력: 다양한 성격의 사람들과 소통하는 방법을 배우세요.")
        st.write("🧘 마음 챙김: 명상이나 자기 성찰을 통해 내면의 평화를 찾으세요.")
        st.write("📚 지속적 학습: 새로운 기술과 지식을 습득하여 성장하세요.")

if __name__ == "__main__":
    main()
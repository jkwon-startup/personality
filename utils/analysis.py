def analyze_personality(zodiac_sign, blood_type, mbti):
    """사용자 입력을 기반으로 성격을 분석합니다."""
    try:
        mbti_data, zodiac_data, blood_type_data = load_data()

        # 디버깅: 로드된 MBTI 유형 출력
        st.write("로드된 MBTI 유형:", list(mbti_data.keys()))

        analysis = {
            "zodiac": zodiac_data.get(zodiac_sign, {}).get("특징", []),
            "blood_type": blood_type_data.get(blood_type, {}).get("특징", []),
            "mbti": {}
        }

        # MBTI 데이터 처리
        if mbti in mbti_data:
            for category in ["심리적 특성", "직업적 특성", "대인관계", "연애 관계"]:
                traits = mbti_data[mbti].get(category, [])
                if traits:
                    analysis["mbti"][category] = traits
        else:
            analysis["mbti"] = {"심리적 특성": ["MBTI 정보를 찾을 수 없습니다."]}

        all_traits = analysis["zodiac"] + analysis["blood_type"] + \
                     [trait for traits in analysis["mbti"].values() for trait in traits]
        combined = list(set(all_traits))  # 중복 제거

        analysis["combined"] = combined
        analysis["advice"] = generate_advice(combined)

        return analysis
    except Exception as e:
        raise Exception(f"성격 분석 중 오류 발생: {str(e)}")

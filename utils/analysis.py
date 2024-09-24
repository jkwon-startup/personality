def analyze_personality(zodiac_sign, blood_type, mbti):
    """사용자 입력을 기반으로 성격을 분석합니다."""
    try:
        mbti_data, zodiac_data, blood_type_data = load_data()
        
        analysis = {
            "zodiac": zodiac_data[zodiac_sign]["특징"],
            "blood_type": blood_type_data[blood_type]["특징"],
            "mbti": {}
        }
        
        # MBTI 데이터 처리
        if mbti in mbti_data:
            analysis["mbti"] = mbti_data[mbti]
        else:
            analysis["mbti"] = {"심리적 특성": ["MBTI 정보를 찾을 수 없습니다."]}
        
        all_traits = (analysis["zodiac"] + analysis["blood_type"] + 
                      analysis["mbti"].get("심리적 특성", []) + 
                      analysis["mbti"].get("대인관계", []) + 
                      analysis["mbti"].get("직업적 특성", []) + 
                      analysis["mbti"].get("연애 관계", []))
        combined = list(set(all_traits))  # 중복 제거
        
        analysis["combined"] = combined
        analysis["advice"] = generate_advice(combined)
        
        return analysis
    except Exception as e:
        raise Exception(f"성격 분석 중 오류 발생: {str(e)}")

# get_zodiac_sign 함수는 제거합니다.
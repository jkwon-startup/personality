import json
import os
import random

def load_data():
    """JSON 파일들에서 데이터를 로드합니다."""
    try:
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(current_dir, 'data')
        
        with open(os.path.join(data_dir, 'mbti_traits.json'), 'r', encoding='utf-8') as f:
            mbti_data = json.load(f)
        with open(os.path.join(data_dir, 'zodiac_traits.json'), 'r', encoding='utf-8') as f:
            zodiac_data = json.load(f)
        with open(os.path.join(data_dir, 'blood_type_traits.json'), 'r', encoding='utf-8') as f:
            blood_type_data = json.load(f)
        return mbti_data, zodiac_data, blood_type_data
    except Exception as e:
        raise Exception(f"데이터 로딩 중 오류 발생: {str(e)}")

def generate_advice(traits):
    """성격 특성을 기반으로 조언을 생성합니다."""
    positive_traits = [trait for trait in traits if any(keyword in trait for keyword in ["강한", "뛰어난", "좋은", "잘하는"])]
    negative_traits = [trait for trait in traits if any(keyword in trait for keyword in ["부족", "어려운", "싫어하는", "잘 못하는"])]
    
    advice = []
    
    if positive_traits:
        advice.append(f"당신의 가장 큰 강점은 {random.choice(positive_traits)}입니다. 이를 더욱 발전시켜 나가세요.")
    
    if negative_traits:
        advice.append(f"{random.choice(negative_traits)}에 대해 어려움을 느낄 수 있지만, 이는 성장의 기회가 될 수 있습니다.")
    
    advice.extend([
        "자신의 특성을 잘 이해하고 받아들이는 것이 중요합니다. 그것이 바로 당신만의 독특한 매력이 됩니다.",
        "다른 사람들과의 차이를 인정하고 존중하세요. 그 차이가 우리 사회를 더욱 풍요롭게 만듭니다.",
        "때로는 자신의 약점을 보완하기 위해 노력하는 것도 좋지만, 강점을 더욱 강화하는 것도 중요합니다.",
        "새로운 경험을 두려워하지 마세요. 그것이 당신을 더욱 성장시킬 것입니다.",
        "자신을 너무 혹독하게 대하지 마세요. 우리 모두는 완벽하지 않으며, 그것이 우리를 인간답게 만듭니다.",
        "당신의 특성은 특정 상황에서 큰 장점이 될 수 있습니다. 그 상황을 찾아 최대한 활용해보세요.",
        "타인의 의견을 듣되, 최종적인 판단은 항상 자신의 내면의 소리에 귀 기울이세요.",
        "자신의 감정을 솔직히 표현하는 것도 중요하지만, 때로는 상황에 맞게 조절하는 것도 필요합니다.",
        "당신의 특성을 직업이나 취미에 연결시켜보세요. 그것이 당신의 삶을 더욱 풍요롭게 만들 수 있습니다.",
        "때로는 편안한 휴식도 필요합니다. 자신을 돌보는 시간을 가지세요."
    ])
    
    return random.sample(advice, 5)  # 무작위로 5개의 조언을 선택

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

def generate_combined_analysis(zodiac_sign, blood_type, mbti, combined_traits):
    analysis = f"{zodiac_sign}, {blood_type}형, 그리고 {mbti} 성격 유형의 특성이 복합적으로 나타나는 당신은 "
    
    trait_categories = {
        "창의성": ["창의적", "혁신적", "독창적"],
        "책임감": ["책임감", "신뢰", "성실"],
        "감성": ["감성적", "공감", "이해심"],
        "논리성": ["논리적", "분석적", "전략적"],
        "사교성": ["사교적", "외향적", "친화력"],
        "독립성": ["독립적", "자립적", "자족적"]
    }
    
    identified_traits = []
    for category, keywords in trait_categories.items():
        if any(keyword in trait.lower() for trait in combined_traits for keyword in keywords):
            identified_traits.append(category)
    
    if identified_traits:
        analysis += ", ".join(identified_traits[:-1])
        if len(identified_traits) > 1:
            analysis += f" 그리고 {identified_traits[-1]}"
        elif len(identified_traits) == 1:
            analysis += identified_traits[0]
        analysis += "의 특성을 가지고 있습니다. "
    
    analysis += "이러한 특성들이 조화롭게 어우러져 당신만의 독특한 성격을 형성하고 있습니다. "
    analysis += f"{zodiac_sign}의 {random.choice(combined_traits)}, {blood_type}형의 {random.choice(combined_traits)}, 그리고 {mbti}의 {random.choice(combined_traits)} 특성이 특히 두드러집니다."
    
    return analysis
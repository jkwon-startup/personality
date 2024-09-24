import json
from datetime import datetime
import os
import random

def load_data():
    """JSON 파일들에서 데이터를 로드합니다."""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, '..', 'data')  # app.py와 utils가 같은 루트에 있다고 가정

        with open(os.path.join(data_dir, 'mbti_traits.json'), 'r', encoding='utf-8') as f:
            mbti_data = json.load(f)
        with open(os.path.join(data_dir, 'zodiac_traits.json'), 'r', encoding='utf-8') as f:
            zodiac_data = json.load(f)
        with open(os.path.join(data_dir, 'blood_type_traits.json'), 'r', encoding='utf-8') as f:
            blood_type_data = json.load(f)
        return mbti_data, zodiac_data, blood_type_data
    except Exception as e:
        raise Exception(f"데이터 로딩 중 오류 발생: {str(e)}")

def get_zodiac_sign(month, day):
    """생일을 기반으로 별자리를 반환합니다."""
    zodiac_dates = [
        ((1, 20), (2, 18), "물병자리"),
        ((2, 19), (3, 20), "물고기자리"),
        ((3, 21), (4, 19), "양자리"),
        ((4, 20), (5, 20), "황소자리"),
        ((5, 21), (6, 20), "쌍둥이자리"),
        ((6, 21), (7, 22), "게자리"),
        ((7, 23), (8, 22), "사자자리"),
        ((8, 23), (9, 22), "처녀자리"),
        ((9, 23), (10, 22), "천칭자리"),
        ((10, 23), (11, 21), "전갈자리"),
        ((11, 22), (12, 21), "사수자리"),
        ((12, 22), (12, 31), "염소자리"),
        ((1, 1), (1, 19), "염소자리")
    ]
    
    try:
        date = datetime(2000, month, day)
    except ValueError:
        return "유효하지 않은 날짜"

    for (start_month, start_day), (end_month, end_day), sign in zodiac_dates:
        start_date = datetime(2000, start_month, start_day)
        end_date = datetime(2000, end_month, end_day)
        if start_date <= date <= end_date:
            return sign
        if start_month == 12 and end_month == 1:
            if date >= datetime(2000, 12, start_day) or date <= datetime(2000, 1, end_day):
                return sign
    
    return "별자리를 찾을 수 없습니다"

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

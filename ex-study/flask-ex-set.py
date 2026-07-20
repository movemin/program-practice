"""제이슨 키값 중복 유니크만 모으기 위해 씀"""

from flask import Flask, jsonify

app = Flask(__name__)

# 💡 [핵심] JSON 출력 시 한글이 깨지지(유니코드로 변환되지) 않게 설정
app.json.ensure_ascii = False

# 1. 기본 대문 주소 (http://127.0.0.1:5000/) 접속 시 실행
@app.route('/')
def home():
    # DB나 외부에서 들어온 중복 포함 JSON/Dict 데이터 예시
    products = [
        {"name": "운동화A", "brand": "나이키"},
        {"name": "운동화B", "brand": "아디다스"},
        {"name": "운동화C", "brand": "나이키"},  # 중복
        {"name": "운동화D", "brand": "뉴발란스"},
        {"name": "운동화E", "brand": "아디다스"},  # 중복
    ]

    # 💡 [핵심 패턴] Dict에서 brand 키값만 뽑아 set으로 중복 제거!
    unique_brands = list(set(item['brand'] for item in products))

    # 웹 브라우저에 JSON 형태로 응답
    return jsonify({"unique_brands": unique_brands})


if __name__ == '__main__':
    app.run(debug=True)
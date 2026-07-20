"""
[쇼핑몰 서비스]
기획자:
오늘 판매된 상품의 카테고리 종류(유니크한 값만)가 총 몇 개인지
뽑아주세요
"""

# 쇼핑몰 서비스에서 다음과 같은 JSON 데이터를 받음
shopping_mall = [
  {"order_id": 1, "category": "전자기기", "price": 100000},
  {"order_id": 2, "category": "의류", "price": 30000},
  {"order_id": 3, "category": "전자기기", "price": 50000},
  {"order_id": 4, "category": "식품", "price": 15000},
  {"order_id": 5, "category": "의류", "price": 20000}
]


# "category"라는 키(Key)의 값(Value)들만 뽑아내면
categories = []
for dictionary in shopping_mall:
    categories.append(dictionary["category"])
print(categories)

# set을 이용해 중복 제거하고 유니크만 모으기
unique_categories = set(categories)
print(unique_categories)

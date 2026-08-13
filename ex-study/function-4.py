# 함수 정의
# def bar(a, b=2, c=3):  # Parameter -> positional, defaultvalue(인자값 생략이 가능하다라는 의미 내포)
#     print(a, b, c)
    
# # 함수 호출
# def bar(a, b, c):
#     print(a, b, c)
# bar(1, 2, 3)  # Positional
# bar(b=2, c=3, a=1)  # Keyword
# bar(2, 3, c=1)  # Positional + Keyword

# keyword를 쓰는 순간 positional은 무너진다

# bar(1)
# bar(1, 4)
# # bar(3, c=20)  # a값은 무조건 넣어야 하고, 나머지는 안 넣어도 되네. b값은 기본값이니까 안넣어 주고, c값은 변경해주자


# # ---가변---
# # 필요성
# def get_sum(*args):  # *: 매개는 가변으로 쓰인다
#     print(f"len: {len(args)}")
#     total = 0
#     for value in args:
#         total += value
#     print(f"sum: {total}")
#     # print(f"type: {type(args)}, {args}")
#     # total = sum(args)
#     # print(f"sum: {total}")

# # 인자값이 매개변수를 거쳐서 튜플로 변한다
# get_sum(1, 2)  # 인자값 4개로????
# get_sum(4, 5, 6, 7)


# 매개변수에다가 *를 붙이면 인자가 몇개이든지 상관없이 처리할 수 있다
# def bar(a, b, c, *args):  # *: 매개는 가변으로 쓰인다
#     print(a, b, c)
#     print(args)
    # print(f"type: {type(args)}, {args}")
    # total = sum(args)
    # print(f"sum: {total}")

# 의미: a, b, c는 무조건, 뒤에 있는 가변 위치 인자는 옵션!!
# ex) 가전제품 살 때 사용자 정보 등 필수 정보, 뒤에는 옵션
# bar(1, 2, 3)  # 인자값 4개로????
# bar(1, 2, 3, 4)
# bar(1, 2, 3, 4, 5)


# (*args, a, b, c) => 앞에서 무제한으로 받으니까 뒤에가 의미 없어짐 -> 기준 모름
# 문법: 포지셔너리, 

# 매개변수 정의를 하면
# 정의 순서
# positional -> variable P

# 앞으로 알고리즘 생각 시 **개수**가 정해져 있는 문제인지 아닌지 생각해라
# 매개변수의 **개수**가 핵심적인 차이이다
# def bar(a, b, c, *args):  # 개수가 정해지지 않음
#     print(a, b, c)
#     print(args)

# def foo(a, b, c, d=1, e=2):  # 5개
#     print(a, b, c, d, e)

# bar(1, 2, 3, 4, 5, 6)  # 무제한으로 받으니까 에러 안남
# foo(1, 2, 3, 4, 5, 6)  # 개수는 5개로 정해져 있음


# 자동차 주문 함수 정의
# 1) Madatory: model, color
# 2) Option: equipments
# 3) Default: special discount
def car_order(model, color, *options, discount=False):
    print(model, color, *options, discount)

car_order("SUV", "Black", "무광", "네비게이션")
car_order("SUV", "Black", "무광", "네비게이션", discount=True)
car_order("SUV", "Black", discount=True)
# # 함수 정의 : def + 동사or동사구 + parameter + :
# def add(a, b):
#     result = a + b
#     return result

# # 함수 호출(Call)
# result = add(3, 5)  # 반환값을 변수에 저장
# print(result)       # 8

# def greet(name):
#     print(f"Hello, {name}!")    # return 없음

# x = greet("kim")    # 출력만 수행
# print(x)            # None

# 예제 1: 잘못된 입력이면 함수 즉시 종료
# def check_score(score):
#     if score < 0:
#         print("잘못된 점수입니다.")
#         return      # 함수 종료 목적
#     print("점수 확인 완료")
#     return score

# check_score(-10)

# # 예제 2: return 뒤 코드는 실행되지 않음
# def test():
#     print("시작")
#     return          # 함수 즉시 종료
#     print("이 문장은 실행되지 않음")
    
# test()

def min_max(numbers):
    return min(numbers), max(numbers)   # 값 2개 -> 튜플

result = min_max([3, 1, 9, 5])
print(result)           # (1, 9)  튜플 하나

low, high = min_max([3, 1, 9, 5])       # 언패킹
print(low, high)        # 1 9
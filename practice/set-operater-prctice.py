# 예시 set
temp_A_set = {1, 2, 3, 4, 5, 6}
temp_B_set = {4, 5, 6, 7, 8, 9}
# 집합의 가장 큰 특징: 중복값x
# 집합 연산은 네가지가 있음
# {합집합, 교집합, 차집합, 대칭집합}

# 합집합: |
print(f"합집합: {temp_A_set | temp_B_set}")

# 교집합: &
print(f"교집합: {temp_A_set & temp_B_set}")

# 차집합: -
print(f"차집합: {temp_A_set - temp_B_set}")

# 대칭집합: ^
print(f"대칭집합: {temp_A_set ^ temp_B_set}")
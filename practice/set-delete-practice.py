ex_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(f"초기 set: {ex_set}")
# 삭제는 3가지 유형
# 1. 삭제 대상 x시: 키에러
# 2. 삭제 대상 x시: 그냥 통과
# 3. 삭제와 동시에 엑세스

# 1
try:
    ex_set.remove(11)
except KeyError:
    print("[remove] -> This is KeyError")
    
ex_set.remove(10)
print(f"[remove] -> 안에 값이 있으면(ex. 10): {ex_set}")

# 2
ex_set.discard(11)
print(f"안에 값이 없어도 error가 없음(ex. 11): {ex_set}")
ex_set.discard(9)
print(f"[discard] -> 안에 값이 있으면(ex. 9): {ex_set}")

# 3
print(f"stack: {ex_set.pop()}")

print(f"최종 set: {ex_set}")
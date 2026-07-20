bar = {1, 2, 3}
print(3 not in bar)
print(4 not in bar)

# 제이슨 키값 중복 유니크만 모으기 위해 씀


# 그 값이 있는 지 없는지 확인하고 싶을 때 사용
import random
lotto = set()
while len(lotto) < 6:
    lotto.add(random.randrange(1, 46))

lotto_list = sorted(list(lotto))
# lotto_list = list(lotto)
# list(lotto_list).sort()
print(lotto_list)

for v in lotto:
    print(v)
    
    
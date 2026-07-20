import random

# random.randrange(1, 47): 1부터 46까지의 정수 중 아무 숫자를 호출한다
lotto = set()

for _ in range(6):  # 로또는 6자리
    lotto.add(random.randrange(46))

lotto = list(lotto)
lotto.sort()  # 원본값 변경 정렬

print(lotto)
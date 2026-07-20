import random
lotto = set()
indexes = range(0, 46)
while len(lotto) < 6:
    lotto.add(random.randrange(1, 46))

print(lotto)
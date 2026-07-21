bar = "hello world"

print(bar[:5])
print(bar[-5:])


bar = "hello world"
foo = bar  # 생성 하여 저장한다
foo += " gsc"

print(bar)  # 그래서 bar는 그대로
print(foo)

pos = [1, 2, 3]
king = pos  # list는 reference 변수이기 때문에 같은 주소값을 가리킨다
king.append(10)
print(pos)
print(king)
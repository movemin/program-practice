bar = ["안녕", "GSC", "반가워요"]

print(" ".join(bar))
print(", ".join(bar))

bar2 = "2000 3000 4000"
print(", ".join(f"{price}원" for price in bar2.split())) # 나중에 중간에 컴마찍는거 제미나이에게 물어보기

bar3 = ["안녕", "하세요", "gsc"]
print("".join(bar3))

result = ""
for msg in bar3:
    result += msg
print(result)
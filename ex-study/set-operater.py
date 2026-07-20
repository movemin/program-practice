bar = {1, 2, 3, 4}
foo = {3, 4, 5, 6}

print(f"합집합: {' '.join(map(str, bar | foo))}")
print(f"차집합: {' '.join(map(str, bar - foo))}")
print(f"교집합: {' '.join(map(str, bar & foo))}")
print(f"대칭집합: {' '.join(map(str, bar ^ foo))}")

std_info = {'id': '123', 'name':'gsc',
            'email':'abc@a,com'}

required_fields = {'id', 'email', 'phone'}

print(required_fields - std_info.keys())
# 사용자로부터 받아야 되는 정보가 뭔지 알 수 있다(실무)
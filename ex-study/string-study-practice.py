text = """
안녕하세요      탭
두 번째 라인입니다.

힘들어요~~~엉엉
방학 때 연락하면 나뻤어~~~~
"""
print(text)

lines = text.splitlines()  # 한 문단씩 끊어준다
for line in lines:
    print(line)
    
for line in lines:
    print(line.split())
file_name = "test.py"

name, extention = file_name.split(".")

print(name)
print(extention)

bar = "hello world gsc~~"
pos = bar.split()
print(f"type: {type(pos)}\n {pos}")
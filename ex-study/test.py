file = open("test2.csv", 'r', encoding='utf-8')

content = file.read()

print(content.split("\n")[0])
num_of_fields = len(content.split("\n")[0].split(","))

print(f"필드 개수: {num_of_fields}")

file.close()
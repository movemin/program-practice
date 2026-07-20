bar = {1, 2, 3, 4}

try:
    bar.remove(5)
except KeyError:
    print("메롱 난 없지롱")

# print(bar)
# bar.discard(3)
# print(bar)
while bar:
    print(bar.pop())
    
file_list = ["a.jpg", "b.txt", "c.k.pdf", "d.svg", "e.png"]
img_types = (".jpg", ".svg", ".png")
for name in file_list:
    *name, file = name.split(".")
    print("".join(name), file)
    
bar = "a.jpg"
server_address = "https://www.gsc.com"
print(bar.endswith(".jpg"))
print(bar.startswith("https://"))

# for name in file_list:
#     name, file = name.split(".", maxsplit=1.)
#     print(name, file)

for name in file_list:
    if name.endswith(img_types):
        print(name)
        
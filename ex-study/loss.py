# 손실 무손실 파일
file_list = ["a.jpg", "b.txt", "c.k.pdf", "d.svg", "e.png"]

# 손실 파일
img_loss = ['.jpg', 'webp']

# 무손실 파일
img_without_loss = ['.png', '.raw', '.bmp']

# 대상 파일
img_types = set(img_loss) | set(img_without_loss)
print(img_types)


img_a = ['.jpg', 'webp', '.bmp']
img_b = ['.png', '.raw', '.bmp', '.jpg']

img_types = set(img_a) | set(img_b)
print(img_types)


img_loss = ['.jpg', 'webp', '.bmp']
img_without_loss = ['.png', '.raw', '.bmp', '.jpg']

img_file = [ file for file in file_list
            if file.endswith(tuple(img_types))]
print(img_file)


bar = "hello"
bar += " world"
print(" ".join(bar.split()))
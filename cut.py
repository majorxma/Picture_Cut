from PIL import Image

img = Image.open("./699+7.5g+20170721A.jpg")
a = img.size
print(a)
width = a[0]
height = a[1]
#rx, ry代表希望将图片分割为 rx * ry 的图片
rx = 128
ry = 128
x = width // rx
y = height // ry
print("x is " + str(x))
print("y is " + str(y))
num = 0
for i in range(x):
    for j in range(y):
        left = i * rx
        bottom = j * ry
        cropped = img.crop((left, bottom, left + rx, bottom + ry))
        cropped.save("./128_128/" + str(num) + ".jpg")
        num += 1

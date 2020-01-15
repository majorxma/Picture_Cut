from PIL import Image
from numpy import average, dot, linalg
 
# 对图片进行统一化处理
def get_thum(image, size=(64,64), greyscale=False):
    # 利用image对图像大小重新设置, Image.ANTIALIAS为高质量的
    image = image.resize(size, Image.ANTIALIAS)
    if greyscale:
        # 将图片转换为L模式，其为灰度图，其每个像素用8个bit表示
        image = image.convert('L')
    return image
 
# 计算图片的余弦距离
def image_similarity_vectors_via_numpy(image1, image2):
    image1 = get_thum(image1)
    image2 = get_thum(image2)
    images = [image1, image2]
    vectors = []
    norms = []
    for image in images:
        vector = []
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        # linalg=linear（线性）+algebra（代数），norm则表示范数
        # 求图片的范数？？
        norms.append(linalg.norm(vector, 2))
    a, b = vectors
    a_norm, b_norm = norms
    # dot返回的是点积，对二维数组（矩阵）进行计算
    res = dot(a / a_norm, b / b_norm)
    return res

images = []
for i in range(70):
    image = image1 = Image.open('./64_64/' + str(i) + '.jpg')
    images.append(image)
#images用来存储所有的照片， simu矩阵用来存储所有计算的结果
simu = []
for i in range(70):
    simu1 = []
    for j in range(70):
        simu1.append(0)
    simu.append(simu1)

result = []
min = 1
min1 = 100
for i in range(70):
    sum = 0
    for j in range(70):
        if (i != j):
            if(simu[i][j] != 0):
                sum += simu[i][j]
            else:
                image1 = images[i]
                image2 = images[j]
                cosin = image_similarity_vectors_via_numpy(image1, image2)
                sum += cosin
                simu[i][j] = simu[j][i] = cosin
    sum = sum / 69
    print(sum)
    if (sum < min):
        min = sum
        min1 = i
    result.append(sum)
print(result)
print(min)
print(min1)
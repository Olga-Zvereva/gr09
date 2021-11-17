from PIL import Image
import numpy as np

def createFilter(size, step):
    width = len(imageToArray)
    height = len(imageToArray[1])
    x = 0
    while x < width:
        y = 0
        while y < height:
            brightness = getBrightness(x, y, size)
            getColorPix(brightness, x, y, size, step)
            y += size
        x += size

def getBrightness(x, y, size):
    res = 0
    for x1 in range(x, x + size):
        for y1 in range(y, y + size):
            for e in imageToArray[x1][y1]:
                res += e // 3
    return res // size ** 2


def getColorPix(brightness, x, y, size, grayscale):
    for x1 in range(x, x + size):
        for y1 in range(y, y + size):
            for e in imageToArray[x1][y1]:
                e = brightness // grayscale * grayscale


print('Введите имя исходного изображения:')
nameImage = input()
print('Введите имя результирующего изображения:')
resImage = input()

size = int(input())
step = int(input())
imageToArray = np.array(Image.open(nameImage))

createFilter(size, step)

resultImage = Image.fromarray(imageToArray)
resultImage.save(resImage) 
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
    for x in range(x, x + size):
        for y in range(y, y + size):
            for e in imageToArray[x][y]:
                res += e // 3
    return res // size ** 2


def getColorPix(brightness, x, y, size, grayscale):
    for x in range(x, x + size):
        for y in range(y, y + size):
            for e in imageToArray[x][y]:
                e = brightness // grayscale * grayscale


size = int(input())
step = int(input())
imageToArray = np.array(Image.open("img2.jpg"))

createFilter(size, step)

resultImage = Image.fromarray(imageToArray)
resultImage.save('res.jpg') 
from PIL import Image
import numpy as np

image = Image.open(input("Введите полное имя изображения: "))
result_image = input("Введите имя результирующего изображения: ")
arr = np.array(image)
height = len(arr)
width = len(arr[1])
size = int(input("Введите размер: "))
step = int(255 / int(input("Введите градацию: ")))


class GreyImage:
    def __init__(self, step, height, width, size, arr):
        self.step = step
        self.height = height
        self.width = width
        self.size = size
        self.arr = arr

    def getGreyImage(self):
        i = j = 0
        while i < self.height:
            while j < self.width:
                sum_color = np.sum((self.arr[i: i + self.size, j: j + self.size]) / 3)
                average = int(sum_color // (self.size * self.size))
                self.arr[i: i + self.size, j: j + self.size] = int(average // self.step) * self.step
                j += self.size
            i += self.size
        return self.arr


newPicture = GreyImage(step, height, width, size, arr)
result = Image.fromarray(newPicture.getGreyImage())
result.save(result_image)

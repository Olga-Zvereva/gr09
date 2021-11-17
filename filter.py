from PIL import Image
import numpy as np


def filter_image(array, mosaic_size):
    a = len(array) - mosaic_size + 1
    a1 = len(array[1]) - mosaic_size + 1
    for i in range(0, a, mosaic_size):
        for j in range(0, a1, mosaic_size):
            average_brightness = get_brightness(array, mosaic_size, i, j)
            array = paint_over_pixels(array, average_brightness, step, mosaic_size, i, j)
    return array


def get_brightness(array, mosaic_size, i, j):
    sum = 0
    for x in range(i, i + mosaic_size):
        for y in range(j, j + mosaic_size):
            for num in range(3):
                sum += int(array[x][y][num])
    brightness = int(sum // (3 * mosaic_size ** 2))
    return brightness


def paint_over_pixels(array, brightness, step, mosaic_size, i, j):
    for x in range(i, i + mosaic_size):
        for y in range(j, j + mosaic_size):
            for num in range(3):
                array[x][y][num] = int(brightness // step) * step
    return array


img = Image.open("img2.jpg")
array = np.array(img)
mosaic_size = 10
step = 50
res = Image.fromarray(filter_image(array, mosaic_size))
res.save('res.jpg')

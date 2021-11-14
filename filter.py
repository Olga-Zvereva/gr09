from PIL import Image
import numpy as np
from math import ceil

def read(filename):
    img = Image.open(filename)
    return np.array(img)


def get_mean(array, px_per_brick, row_cell, col_cell):
    mean = 0
    for row in range(row_cell, row_cell + px_per_brick):
        for col in range(col_cell, col_cell + px_per_brick):
            clr_r = array[row][col][0]
            clr_g = array[row][col][1]
            clr_b = array[row][col][2]
            M = (clr_r // 3 + clr_g // 3 + clr_b // 3)
            mean += M
    return int(mean // (px_per_brick ** 2))


def update_array(array, row_cell, col_cell, px_per_brick, px_in_grade):
    mean = get_mean(array, px_per_brick, row_cell, col_cell)
    for row in range(row_cell, row_cell + px_per_brick):
        for col in range(col_cell, col_cell + px_per_brick):
            array[row][col][0] = int(mean // px_in_grade) * px_in_grade
            array[row][col][1] = int(mean // px_in_grade) * px_in_grade
            array[row][col][2] = int(mean // px_in_grade) * px_in_grade


def to_grayscale(array, px_per_brick, grades):
    rows = len(array)
    cols = len(array[1])
    px_in_grade = ceil(255 / grades)
    row_cell = 0
    
    while row_cell <= rows - px_per_brick:
        col_cell = 0
        while col_cell <= cols - px_per_brick:
            update_array(array, row_cell, col_cell, px_per_brick, px_in_grade)
            col_cell = col_cell + px_per_brick
        row_cell = row_cell + px_per_brick
    return array


def write(array, filename):
    result = Image.fromarray(array)
    result.save(filename)


if __name__ == "__main__":
    arr = read("img2.jpg")
    arr = to_grayscale(arr, 20, 6)
    write(arr, "res.jpg")


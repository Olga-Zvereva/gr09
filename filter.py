from PIL import Image
import numpy as np
from math import ceil

def read(filename):
    img = Image.open(filename)
    return np.array(img)


def get_mean(array, px_per_brick, row_cell, col_cell):
    slice = array[row_cell:row_cell + px_per_brick, col_cell:col_cell + px_per_brick]
    return np.mean(slice)


def update_array(array, row_cell, col_cell, px_per_brick, px_in_grade):
    mean = get_mean(array, px_per_brick, row_cell, col_cell)
    new_val = int(mean // px_in_grade) * px_in_grade
    new_arr = np.array(3 * [new_val])
    array[row_cell:row_cell + px_per_brick, col_cell:col_cell + px_per_brick] = new_arr


def to_grayscale(array, px_per_brick, grades):
    rows = len(array)
    cols = len(array[1])
    px_in_grade = ceil(255 / grades)

    for row_cell in range(0, rows, px_per_brick):
        for col_cell in range(0, cols, px_per_brick):
            update_array(array, row_cell, col_cell, px_per_brick, px_in_grade)

    return array


def write(array, filename):
    result = Image.fromarray(array)
    result.save(filename)


if __name__ == "__main__":
    arr = read("img2.jpg")
    arr = to_grayscale(arr, 10, 6)
    write(arr, "res.jpg")


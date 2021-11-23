from PIL import Image
import numpy as np
from math import ceil

def read(filename):
    """
    Чтение файла с изображением в массив Numpy

    :param filename: имя файла
    :return: Numpy-массив
    """
    img = Image.open(filename)
    return np.array(img)


def get_mean(array, px_per_brick, row_cell, col_cell):
    """
    Вычислить среднее значение пикселей на блоке изображения

    :param array: Numpy-массив с изоражением
    :param px_per_brick: размер блока изображения в пикселях
    :param row_cell: строка изображения, откуда начинается блок
    :param col_cell: столбец изображения, откуда начинается блок
    :return: среднее значение пикселей на блоке

    >>> get_mean(np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 2, 1, 1)
    1.0
    >>> get_mean(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 2, 0, 0)
    3.0
    """
    slice = array[row_cell:row_cell + px_per_brick, col_cell:col_cell + px_per_brick]
    return np.mean(slice)


def update_array(array, row_cell, col_cell, px_per_brick, px_in_grade):
    """
    Преобразовать блок изображения в оттенки серого

    :param array: Numpy-массив с изображением
    :param row_cell: строка изображения, откуда начинается блок
    :param col_cell: столбец изображения, откуда начинается блок
    :param px_per_brick: размер блока в пикселях
    :param px_in_grade: сколько пикселей в одной градации серого
    """
    mean = get_mean(array, px_per_brick, row_cell, col_cell)
    new_val = int(mean // px_in_grade) * px_in_grade
    new_arr = np.array(3 * [new_val])
    array[row_cell:row_cell + px_per_brick, col_cell:col_cell + px_per_brick] = new_arr


def to_grayscale(array, px_per_brick, grades):
    """
    Преобразовать все изображение в оттенки серого

    :param array: Numpy-массив с изображением
    :param px_per_brick: размер блока в пикселях
    :param grades: сколько градаций серого должно получиться
    :return: изображение в градациях серого

    """
    rows = len(array)
    cols = len(array[1])
    px_in_grade = ceil(255 / grades)

    for row_cell in range(0, rows, px_per_brick):
        for col_cell in range(0, cols, px_per_brick):
            update_array(array, row_cell, col_cell, px_per_brick, px_in_grade)

    return array


def write(array, filename):
    """
    Сохранить изображение в файл с именем filename

    :param array: Numpy-массив с изображением
    :param filename: имя файла, в который надо сохранить
    """
    result = Image.fromarray(array)
    result.save(filename)


if __name__ == "__main__":
    read_name = input()
    write_name = input()
    arr = read(read_name)
    block_size = int(input())
    grayscale = int(input())
    arr = to_grayscale(arr, block_size, grayscale)
    write(arr, write_name)


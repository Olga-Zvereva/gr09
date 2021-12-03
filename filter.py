from PIL import Image
import numpy as np


def get_average_brightness(array_of_pixels, mosaic_size, i, j):
    '''
    Метод получает среднее значение яркости пикселей выбранной прямоугольной области изображения
    Args:
        array_of_pixels: массив всех пикселей изображения
        mosaic_size: размер мозаики (размер прямоугольной области пикселей, среднее значение которых мы вычисляем)
        i: номер строки массива пикселей, с которой начинается выбранная прямоугольная область
        j: номер столбца массива пикселей, с которого начинается выбранная прямоугольная область

    Returns: целое число - значение средней яркости пикселей выбранной прямоугольной области изображения

    >>> get_average_brightness(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 2, 1, 1)
    2
    >>> get_average_brightness(np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 1, 1, 1)
    0
    >>> get_average_brightness(np.array([[5, 5, 5], [5, 5, 5], [5, 5, 5]]), 2, 0, 0)
    1
    '''
    area = array_of_pixels[i:i + mosaic_size, j:j + mosaic_size]
    total_brightness = np.sum(area)
    return int(total_brightness // 3 // mosaic_size ** 2)


def change_pixels_color(array_of_pixels, mosaic_size, grayscale, average_brightness, i, j):
    '''
    Метод изменяет значения всех пикселей выбранной прямоугольной области изображения на единое значение,
    вычисленное исходя из полученных значения средней яркости пикселей выбранной прямоугольной области изображения
    и заданного значения градации серого
    Args:
        array_of_pixels: массив всех пикселей изображения
        mosaic_size: размер мозаики (размер прямоугольной области пикселей, значение которых нужно изменить)
        grayscale: заданная величина градации серого
        average_brightness: значение средней яркости пикселей выбранной прямоугольной области изображения
        i: номер строки массива пикселей, с которой начинается выбранная прямоугольная область
        j: номер столбца массива пикселей, с которого начинается выбранная прямоугольная область

    Returns: массив всех пикселей изображения с изменёнными значениями пикселей выбранной
    прямоугольной области изображения
    '''
    pixel_value = int(average_brightness // grayscale) * grayscale
    array_of_pixels[i:i + mosaic_size, j:j + mosaic_size] = pixel_value
    return array_of_pixels


def grey_filter(image, mosaic_size, grayscale):
    '''
    Метод накладывает на изображение фильтр серого цвета
    Args:
        image: изображение, цвета которого нужно преобразовать в оттенки серого
        mosaic_size: размер мозаики (значение качества преобразованного изображения)
        grayscale: величина градации серого

    Returns: преобразованное изображение
    '''
    array_of_pixels = np.array(image)
    height = len(array_of_pixels)
    width = len(array_of_pixels[1])
    for i in range(0, height - mosaic_size + 1, mosaic_size):
        for j in range(0, width - mosaic_size + 1, mosaic_size):
            average_brightness = get_average_brightness(array_of_pixels, mosaic_size, i, j)
            array_of_pixels = change_pixels_color(array_of_pixels, mosaic_size, grayscale, average_brightness, i, j)
    return array_of_pixels


if __name__ == "__main__":
    name_of_input_image = '{}.{}'.format(input('Имя входного изображения - '), input('Формат входного изображения - '))
    mosaic_size = int(input('Размер мозаики - '))
    grayscale = int(input('Величина градации серого - '))
    name_of_output_image = '{}.{}'.format(input('Имя выходного изображения - '), input('Формат выходного изображения - '))
    input_image = Image.open(name_of_input_image)
    image_in_gray_tones = Image.fromarray(grey_filter(input_image, mosaic_size, grayscale))
    image_in_gray_tones.save(name_of_output_image)
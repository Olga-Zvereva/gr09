from PIL import Image
import numpy as np
import easygui
from collections import namedtuple
import sys

Size = namedtuple("Size", ["width", "height"])



def open_image_as_array(path=""):
    if not path:
        path = easygui.fileopenbox(
            title="Открыть изображение", filetypes=["*.jpg"])
    raw_img = Image.open(path)
    return np.array(raw_img)


def save_image(image, path=""):
    if not path:
        path = easygui.filesavebox(
            title="Сохранить изображение", filetypes=["*.png"]) + ".png"
    image.save(path, "PNG")


def get_mosaic(raw_image, mosaic_size=Size(10, 10), discrete_step=50):

    width = len(raw_image)
    height = len(raw_image[1])

    for i in range(0, width - mosaic_size.width + 1, mosaic_size.width):
        for j in range(0, height - mosaic_size.height + 1, mosaic_size.height):
            average_brightness = 0
            average_brightness = np.sum(
                raw_image[i: i + mosaic_size.width, j: j + mosaic_size.height]) / 3 // (mosaic_size.width * mosaic_size.height)

            raw_image[i: i + mosaic_size.width, j: j + mosaic_size.height:] = int(
                average_brightness // discrete_step) * discrete_step
    return Image.fromarray(raw_image)


if __name__ == "__main__":
    if "console" in sys.argv:
        raw_image = open_image_as_array(input("Введите путь: "))
        mosaic = get_mosaic(raw_image)
        save_image(mosaic, input("Введите путь и имя файла для сохранения: "))
    elif "dialog" in sys.argv or len(sys.argv) == 1:
        raw_image = open_image_as_array()
        mosaic = get_mosaic(raw_image)
        save_image(mosaic)

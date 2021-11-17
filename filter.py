from PIL import Image
import numpy as np
import easygui
from collections import namedtuple

Size = namedtuple("Size", ["width", "height"])

def open_image_as_array(path = ""):
    if not path:
        path = easygui.fileopenbox(title="Открыть изображение", filetypes=["*.jpg"])
    raw_img = Image.open(path)
    return np.array(raw_img)

def save_image(image, path = ""):
    if not path:
        path = easygui.filesavebox(title="Сохранить изображение", filetypes=["*.jpg"])
    image.save(path)

def get_mosaic(raw_image, mosaic_size = Size(10, 10), discrete_step = 50):
    
    width = len(raw_image)
    height = len(raw_image[1])

    for i in range(0, width - mosaic_size.width + 1, mosaic_size.width):
        for j in range(0, height - mosaic_size.height + 1, mosaic_size.height):
            average_brightness = 0
            for x in range(i, i + mosaic_size.width):
                for y in range(j, j + mosaic_size.height):
                    r = raw_image[x][y][0]
                    g = raw_image[x][y][1]
                    b = raw_image[x][y][2]
                    pixel_brightness = (r // 3 + g // 3 + b // 3)
                    average_brightness += pixel_brightness 
            average_brightness = int(average_brightness // (mosaic_size.width * mosaic_size.height))
            for x in range(i, i + mosaic_size.width):
                for y in range(j, j + mosaic_size.height):
                    raw_image[x][y][0] = int(average_brightness // discrete_step) * discrete_step
                    raw_image[x][y][1] = int(average_brightness // discrete_step) * discrete_step
                    raw_image[x][y][2] = int(average_brightness // discrete_step) * discrete_step

    return Image.fromarray(raw_image)



raw_image = open_image_as_array()
mosaic = get_mosaic(raw_image)
save_image(mosaic)

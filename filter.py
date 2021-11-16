from PIL import Image
import numpy as np

def pixel_art_filter(mosaic_side: int, step: int):
    img_length, img_height = len(img_arr), len(img_arr[1])
    segment_x = 0
    while segment_x < img_length:
        segment_y = 0
        while segment_y < img_height:
            avg_brightness = find_average_brightness(segment_x, segment_y, mosaic_side)
            pixel_coloring(avg_brightness, segment_x, segment_y, mosaic_side, step)
            segment_y += mosaic_side
        segment_x += mosaic_side


def find_average_brightness(segment_x, segment_y, mosaic_side):
    result = 0
    for x in range(segment_x, segment_x + mosaic_side):
        for y in range(segment_y, segment_y + mosaic_side):
            result += sum(img_arr[x][y][range(3)] / 3)
    return int(result) // (mosaic_side * mosaic_side)


def pixel_coloring(avg_brightness, segment_x, segment_y, mosaic_side, grayscale):
    for x in range(segment_x, segment_x + mosaic_side):
        for y in range(segment_y, segment_y + mosaic_side):
            img_arr[x][y][range(3)] = int(avg_brightness // grayscale) * grayscale


np.seterr(over='ignore')
img_arr = np.array(Image.open("img2.jpg"))
pixel_art_filter(int(input()), int(input()))
filtered_img = Image.fromarray(img_arr)
filtered_img.save('res.jpg')
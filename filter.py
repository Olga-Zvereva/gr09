from PIL import Image
import numpy as np
import easygui


img = Image.open(easygui.fileopenbox(title="Открыть изображение", filetypes=["*.jpg"]))
pixels = np.array(img)

width = len(pixels)
height = len(pixels[1])
i = 0
while i <= width - 10:
    j = 0
    while j <= height - 10:
        sum = 0
        for x in range(i, i + 10):
            for y in range(j, j + 10):
                r = pixels[x][y][0]
                g = pixels[x][y][1]
                b = pixels[x][y][2]
                M = (r // 3 + g // 3 + b // 3)
                sum += M
        sum = int(sum // 100)
        for x in range(i, i + 10):
            for y in range(j, j + 10):
                pixels[x][y][0] = int(sum // 50) * 50
                pixels[x][y][1] = int(sum // 50) * 50
                pixels[x][y][2] = int(sum // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(pixels)
res.save(easygui.filesavebox(title="Сохранить изображение", filetypes=["*.jpg"]))

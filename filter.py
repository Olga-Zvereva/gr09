from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
rows = len(arr)
cols = len(arr[1])
i = 0
while i <= rows - 10:
    j = 0
    while j <= cols - 10:
        s = 0
        for r in range(i, i + 10):
            for c in range(j, j + 10):
                clr_r = arr[r][c][0]
                clr_g = arr[r][c][1]
                clr_b = arr[r][c][2]
                M = (clr_r // 3 + clr_g // 3 + clr_b // 3)
                s += M
        s = int(s // 100)
        for r in range(i, i + 10):
            for c in range(j, j + 10):
                arr[r][c][0] = int(s // 50) * 50
                arr[r][c][1] = int(s // 50) * 50
                arr[r][c][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')

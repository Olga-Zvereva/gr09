from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
m_w = len(arr)
m_h = len(arr[1])
i = 0
step = None
#ПЕРЕВОД В СТИЛЬ PEP8


#ыделение функций


def find_step(n):
    return int(255 / (n - 1) - 1 if 255 % (n - 1) == 0 else 255 / (n - 1)) 


#выделение функций 
def find_av_brightness(i, j, arr, m_h, m_w, step):
   while i < a :
    j = 0
    while j < a1 :
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                n0 = arr[n][n1][0]
                n2 = arr[n][n1][1]
                n3 = arr[n][n1][2]
                M = n0 + n2 + n3
                s += M/3
        s = int(s // 100)
    return s
#выделение функций


def do_mosaic(i, j, arr, m_h, m_w, step):
    while i < a :
        j = 0
            while j < a1 :
                for n in range(i, i + 10):
                    for n1 in range(j, j + 10):
                        arr[n][n1][0] = int(s // 50) * 50
                        arr[n][n1][1] = int(s // 50) * 50
                        arr[n][n1][2] = int(s // 50) * 50
                j = j + 10
            i = i + 10
    return i


inp_sizes = input('Введите ширину и высоту мозайки (например: 100,100): ')
num_grad = int(input('Enter the number of gradations(example: 6): '))
res = Image.fromarray(arr)
res.save('res.jpg')

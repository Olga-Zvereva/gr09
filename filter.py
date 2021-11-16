from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)


def find_step(n):
    return int(255 / (n - 1) - 1 if 255 % (n - 1) == 0 else 255 / (n - 1))
#Преобразование в матричный вид

def find_av_brightness(i, j, arr, m_h, m_w, step):
    br = 0.
    br += arr[i: i + m_h, j: j + m_w, :].sum() / 3
    br //= m_h * m_w
    br -= br % step
    return br
#Преобразование в матричный вид

def do_mosaic(arr, m_h, m_w, step):
    for i in range(0, len(arr), m_h):
        for j in range(0, len(arr[1]), m_w):
            brightness = find_av_brightness(i, j, arr, m_h, m_w, step)
            arr[i: i + m_h, j: j + m_w, :] = brightness



inp_sizes = input('Введите ширину и высоту мозайки (например: 100,100): ')
num_grad = int(input('Enter the number of gradations(for example: 6): '))
e_h, e_w = map(int, inp_sizes.split(','))
do_mosaic(inp_im, e_h, e_w, find_step(num_grad)) 
res = Image.fromarray(arr)
res.save('res.jpg')

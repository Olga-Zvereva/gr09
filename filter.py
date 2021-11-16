from PIL import Image

def find_step(n):
    return int(255 / (n - 1) - 1 if 255 % (n - 1) == 0 else 255 / (n - 1))


def find_av_brightness(i, j, arr, m_h, m_w, step):
    br = 0.
    br += arr[i: i + m_h, j: j + m_w, :].sum() / 3
    br //= m_h * m_w
    br -= br % step
    return br


def do_mosaic(arr, m_h, m_w, step):
    for i in range(0, len(arr), m_h):
	@@ -23,10 +21,22 @@ def do_mosaic(arr, m_h, m_w, step):
            arr[i: i + m_h, j: j + m_w, :] = brightness


inp_im_names = input('Введите название изображение '
                     'Ввод выглядит как (например: img2,res): ') \
    .split(',')


inp_sizes = input('Введите ширину и высоту мозайки (например: 100,100): ')


num_grad = int(input('Enter the number of gradations(for example: 6): '))


e_h, e_w = map(int, inp_sizes.split(','))
do_mosaic(inp_im, e_h, e_w, find_step(num_grad))

res = Image.fromarray(inp_im)


res.save(inp_im_names[1] + ".jpg")

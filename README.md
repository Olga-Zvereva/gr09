**Учебное задание по предмету** _Технологии программирования_

Работа с матрицами

Ниже- отчет по работе

---

``filter.py``

![](screenshots/filter-result.jpg)

``old_filter.py``

![](screenshots/old-filter-result.jpg)

old-filter выполняется быстрее, так как не запрашивает
консольный ввод

---

``filter_with_filename.py``

![](screenshots/filter-with-filename-result.jpg)

filter_with_filename.py показывает самое быстрое время
выполнения, так как мы не использовали консольный ввод и 
для преобразования изображения использовали библиотеку Numpy

---

Изображение ``img2.jpg`` до преобразования:

![](img2.jpg)

и после:

![](res.jpg)

---

doc-тесты

![](screenshots/doc-tests.jpg)

---

Работа отладчика

![](screenshots/debugger.jpg)

Синим выделены сверху вниз: размер картинки (shape, 
третий параметр - кол-во цветовых каналов), 
размер ширины блока (block_size), кол-во градаций серого
(grayscale), тип и имя изображения (read_name)

from PIL import Image
import numpy as np
import matplotlib.pylab as plt
import skimage

def image (img_name, gray_img_name):
    # зчитування зображення
    img = Image.open(img_name)
    img2 = img.convert('L')
    img2.save(gray_img_name)

    # кількість пікселів
    w, h = img2.size
    s = w * h
    print("1. Загальна кількість пікселів: ", s)

    # масив пікселів
    a1 = np.asarray(img2)
    a2 = a1.ravel()
    a2 = np.sort(a2)

    # групування за інтенсивністю свічення
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    x_i = []
    for pix in range(len(a2)):
        if a2[pix] in range(1, 17):
            count[0] += 1
        elif a2[pix] in range(17, 33):
            count[1] += 1
        elif a2[pix] in range(33, 49):
            count[2] += 1
        elif a2[pix] in range(49, 65):
            count[3] += 1
        elif a2[pix] in range(65, 81):
            count[4] += 1
        elif a2[pix] in range(81, 97):
            count[5] += 1
        elif a2[pix] in range(97, 113):
            count[6] += 1
        elif a2[pix] in range(113, 129):
            count[7] += 1
        elif a2[pix] in range(129, 145):
            count[8] += 1
        elif a2[pix] in range(145, 161):
            count[9] += 1
        elif a2[pix] in range(161, 177):
            count[10] += 1
        elif a2[pix] in range(177, 193):
            count[11] += 1
        elif a2[pix] in range(193, 208):
            count[12] += 1
        elif a2[pix] in range(208, 225):
            count[13] += 1
        elif a2[pix] in range(225, 241):
            count[13] += 1
        elif a2[pix] in range(241, 255):
            count[13] += 1
    for i in range(len(count)):
        if count[i] != 0:
            x_i.append(count[i] / s)
    print("2. кількість пікселів в 16 групах за інтенсивністю свічення: \n", " ", count)
    print("3. ймовірність (частот) значень інтенсивності свічення груп пікселів у блоках: \n", " ", x_i)

    # ентропія за формулою
    h_x = - sum(x_i * np.log(x_i))
    print("4. ентропія за формулою: ", h_x)

    # функція ентропії
    ent = skimage.measure.shannon_entropy(img2)
    print("5. вбудована функція ентропії: ", ent)

    # гістограма
    plt.hist(a2, bins=32)
    plt.title(gray_img_name)
    plt.show()

print("\nРезультати для png:")
image("1.png", "2.png")
print("\nРезультати для bmp:")
image("1.bmp", "2.bmp")
print("\nРезультати для jpg:")
image("1.jpg", "2.jpg")
print("\nРезультати для tif:")
image("1.tif", "2.tif")
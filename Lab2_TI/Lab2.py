import prettytable
from PIL import Image
import numpy as np
import scipy.ndimage
import matplotlib.pylab as plt
import skimage

def image (img_name):
    # зчитування зображення
    img = Image.open(img_name).convert('L')
    img.save("gray.png")

    #Дискретизація зобраєення
    width, height = img.size
    imgd2 = img.resize((round(width/2), round(height/2)), Image.BILINEAR)
    imgd4 = img.resize((round(width / 4), round(height / 4)), Image.BILINEAR)
    ext = ".png"
    imgd2.save("d2" + ext)
    imgd4.save("d4" + ext)

    #квантування
    imgq8 = img.quantize(8)
    imgq8.save("q8" + ext)
    imgq16 = img.quantize(16)
    imgq16.save("q16" + ext)
    imgq64 = img.quantize(64)
    imgq64.save("q64" + ext)

    #відновлення
    width2, height2 = imgd2.size
    width4, height4 = imgd4.size
    imgv2b = imgd2.resize((round(width2*2), round(height2*2)), Image.BILINEAR)
    imgv2c = imgd2.resize((round(width2 * 2), round(height2 * 2)), Image.BICUBIC)
    imgv4b = imgd4.resize((round(width4 * 4), round(height4 * 4)), Image.BILINEAR)
    imgv4c = imgd4.resize((round(width4 * 4), round(height4 * 4)), Image.BICUBIC)

    # ентропія
    ent = skimage.measure.shannon_entropy(img)
    ventv2b = skimage.measure.shannon_entropy(imgv2b)
    ventv2c = skimage.measure.shannon_entropy(imgv2c)
    ventv4b = skimage.measure.shannon_entropy(imgv4b)
    ventv4c = skimage.measure.shannon_entropy(imgv4c)
    ventq8 = skimage.measure.shannon_entropy(imgq8)
    ventq16 = skimage.measure.shannon_entropy(imgq16)
    ventq64 = skimage.measure.shannon_entropy(imgq64)


    #обчислення відносної ентропії
    l, m = np.histogram(np.asarray(img).ravel(), bins=256)
    l1, m1 = np.histogram(np.asarray(imgv2b).ravel(), bins=256)
    l2, m2 = np.histogram(np.asarray(imgv2c).ravel(), bins=256)
    l3, m3 = np.histogram(np.asarray(imgv4b).ravel(), bins=256)
    l4, m4 = np.histogram(np.asarray(imgv4c).ravel(), bins=256)
    l5, m5 = np.histogram(np.asarray(imgq8).ravel(), bins=256)
    l6, m6 = np.histogram(np.asarray(imgq16).ravel(), bins=256)
    l7, m7 = np.histogram(np.asarray(imgq64).ravel(), bins=256)
    entv2b = abs(np.mean(skimage.measure.shannon_entropy(m, m1)))
    entv2c = abs(np.mean(skimage.measure.shannon_entropy(m, m2)))
    entv4b = abs(np.mean(skimage.measure.shannon_entropy(m, m3)))
    entv4c = abs(np.mean(skimage.measure.shannon_entropy(m, m4)))
    entq8  = abs(np.mean(skimage.measure.shannon_entropy(m, m5)))
    entq16 = abs(np.mean(skimage.measure.shannon_entropy(m, m6)))
    entq64 = abs(np.mean(skimage.measure.shannon_entropy(m, m7)))

    x = prettytable.PrettyTable()
    x.field_names = ["Е вихідного зображення", "відновлене/квантоване", "Е отриманого зображення", "відносна ентропія"]
    x.add_row([ent, "відновлене 2b", ventv2b, entv2b])
    x.add_row([ent, "відновлене 2c", ventv2c, entv2c])
    x.add_row([ent, "відновлене 4b", ventv4b, entv4b])
    x.add_row([ent, "відновлене 4c", ventv4c, entv4c])
    x.add_row([ent, "квантоване 8", ventq8, entq8])
    x.add_row([ent, "квантоване 16", ventq16, entq16])
    x.add_row([ent, "квантоване 64", ventq64, entq64])
    print(x)


image("3.jpg")
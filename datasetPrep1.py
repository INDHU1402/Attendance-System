from PIL import Image, ImageFilter 
import os

f = '/Desktop/Students'

for file in os.listdir(f):
    f_img = f +"/" + file 
    img = Image.open(f_img)
    img1 = img.convert("L")
    img2 = img.rotate(5)
    img3 = img.filter(ImageFilter.GaussianBlur(1.7))
    img4 = img.rotate(-5)
    r,g,b = img.split()
    img5 = img.merge("RGB", (b,g,r))
    name = f_img[:-4]
    img1.save(name + "1" + ".jpg")
    img2.save(name + "2" + ".jpg")
    img3.save(name + "3" + ".jpg")
    img4.save(name + "4" + ".jpg")
    img5.save(name + "5" + ".jpg")

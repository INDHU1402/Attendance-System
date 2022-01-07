from PIL import Image, ImageFilter
import os

dataset_path = '/Desktop/students'

for person in os.listdir(dataset_path):
    for img in os.listdir(os.path.join(dataset_path,person)):
      f_img = dataset_path + "/" + person + "/" + img  
      img = Image.open(f_img)
      img1 = img.convert("L")
      img2 = img.rotate(5)
      img3 = img.rotate(-5)
      img4 = img.filter(ImageFilter.GaussianBlur(1.7))
      img5 = img.filter(ImageFilter.BoxBlur(1.2))
      img6 = img.point(lambda i: i * 1.3)
      img7 = img.point(lambda i: i * 1.8)
      img8 = img.point(lambda i: i * 0.7)
      img9 = img.point(lambda i: i * 0.4)
      img10 = img.rotate(10)
      img11 = img.rotate(-10)
      name = f_img[:-5]
      img1.save(name + "1" + ".jpg")
      img2.save(name + "2" + ".jpg")
      img3.save(name + "3" + ".jpg")
      img4.save(name + "4" + ".jpg")
      img5.save(name + "5" + ".jpg")
      img6.save(name + "6" + ".jpg")
      img7.save(name + "7" + ".jpg")
      img8.save(name + "8" + ".jpg")
      img9.save(name + "9" + ".jpg")
      img10.save(name + "10" + ".jpg")
      img11.save(name + "11" + ".jpg")
      img.save(name + "12" + ".jpg", quality = 95)

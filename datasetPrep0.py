from PIL import Image, ImageFilter 
import os

f = '/Desktop/Students'

for file in os.listdir(f):
    f_img = f +"/" + file 
    img = Image.open(f_img)
    s = f_img.replace(" ", "_")
    if s[-5:].lower() == ".jpeg":
      name = s[:-5] + ".jpg"
    else:
      name = s[:-4] + ".jpg"
    print(name)
    if name != f_img:
      os.remove(f_img)
    img.thumbnail((224,224))
    img.save(name)

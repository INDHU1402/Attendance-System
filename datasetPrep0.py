from PIL import Image, ImageFilter 
import os

dataset_path = '/Desktop/students'

for person in os.listdir(dataset_path):
    f_img = dataset_path + "/" + person 
    img = Image.open(f_img)
    s = person.replace(" ", "_")
    s = s.replace(".", "_")
    if s[-5:].lower() == ".jpeg":
      name = s[:-5] + "0.jpg"
    else:
      name = s[:-4] + "0.jpg"
    os.mkdir(dataset_path + "/" + name[:-5])
    print(name)
    img.thumbnail((224,224))
    img.save(dataset_path + "/" + name[:-5] + "/" + name)
    os.remove(f_img)

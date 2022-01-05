import cv2
import face_recognition
import os

path = 'students'

images = []
classNames = []
mylist = os.listdir(path)

for p in mylist:
    curImg = cv2.imread(f'{path}/{p}')
    images.append(curImg)
    classNames.append(os.path.splitext(p)[0])

encodeList = []
for img in images:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encoded_face = face_recognition.face_encodings(img)
    if encoded_face != []:
        encodeList.append(list(encoded_face[0]))

encodings = open('train.csv', 'w')
for e in encodeList:
    for i in e:
        if i != e[-1]:
            encodings.writelines(f'{i},')
        else:
            encodings.writelines(f'{i}')
    encodings.writelines("\n")
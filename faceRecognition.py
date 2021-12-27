import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import pickle

path = 'images'

images = []
classNames = []
mylist = os.listdir(path)

for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)
        if encoded_face != []:
            encodeList.append(list(encoded_face[0]))
    return encodeList
    
encoded_face_train = findEncodings(images)
cap  = cv2.VideoCapture(0)
success, img = cap.read()
img1 = cv2.resize(img, (0,0), None, 0.25,0.25)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
faces_in_frame = face_recognition.face_locations(img1)
encoded_face = face_recognition.face_encodings(imgS, faces_in_frame)
matches = face_recognition.compare_faces(encoded_face_train, encoded_face[0])
faceDist = face_recognition.face_distance(encoded_face_train, encoded_face[0])
matchIndex = np.argmin(faceDist)

cv2.imshow('webcam', img)
if matches[matchIndex]:
    name = classNames[matchIndex].lower()
    y1,x2,y2,x1 = faces_in_frame[0]
    y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
    cv2.putText(img,name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    print(name)

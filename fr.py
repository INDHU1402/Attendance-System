import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import time

path = 'images'

images = []
classNames = []
mylist = os.listdir(path)

for p in mylist:
    curImg = cv2.imread(f'{path}/{p}')
    images.append(curImg)
    classNames.append(os.path.splitext(p)[0])

def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'{name}, {time}, {date}')
            f.writelines("\n")
        if name in nameList:
            print("Already given Attendance")
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.writelines(f'{name}, {time}, {date}')
            f.writelines("\n")

with open('train.csv','r+') as f:
    trainData = f.readlines()
    trainList = []
    for line in trainData:
        xs = [eval(i) for i in line.split(',')]
        trainList.append(xs)
        
encoded_face_train = trainList
cap  = cv2.VideoCapture(0)
success, img = cap.read()
img1 = cv2.resize(img, (0,0), None, 0.25,0.25)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
face = face_recognition.face_locations(img1)
encoded_face = face_recognition.face_encodings(img1, face)
matches = face_recognition.compare_faces(encoded_face_train, encoded_face[0])
faceDist = face_recognition.face_distance(encoded_face_train, encoded_face[0])
xs = list(zip(classNames, matches, faceDist))
ys = sorted(xs, key=lambda x:x[2])
for i in ys:
    print(str(i[0]) + " | " + str(i[1]) + " | " + str(i[2]) + "\n")
matchIndex = np.argmin(faceDist)
print(matchIndex)
status = "unknown"
if matches[matchIndex]:
    name = classNames[matchIndex].lower()
    y1,x2,y2,x1 = face[0]
    y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
    cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
    cv2.putText(img,name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    markAttendance(name)
    status = "Your attendance has been marked " + name    
print(status)
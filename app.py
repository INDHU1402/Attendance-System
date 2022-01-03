from flask import Flask, render_template
import cv2
import os
import numpy as np
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    flg = True
    return render_template('home.html', name = 'Mr. abcd', flg=flg)

@app.route("/attendance")
def face_recognition():
    flg = False
    file = open(r'cam.py', 'r').read()
    exec(file)
    file1 = open(r'fr.py', 'r').read()
    exec(file1)
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
    pth = "url_for('static', filename=" + "images/" + nameList[-1] + ".jpg')"
    return render_template('home.html', name = 'Mr.abcd', flg=flg, status=nameList[-1], pth=pth)
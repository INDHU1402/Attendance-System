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
    file = open(r'fr.py', 'r').read()
    exec(file)
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
    return render_template('home.html', name = 'Mr.abcd', flg=flg, status=nameList[-1])
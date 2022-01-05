from flask import Flask, render_template, request
import cv2
import os
import numpy as np
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def home():
    flg = True
    return render_template('home.html', name = 'Mr. abcd', flg=flg)

@app.route("/login")
def login():
    return render_template('login.html',flg=True)

@app.route("/logout")
def logout():
    file = open(r'train.py', 'r').read()
    exec(file)
    return render_template('home.html', name = 'Mr. abcd', flg=True)

@app.route("/signup")
def signup():
    return render_template('register.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    nm = request.form["username"]
    ps1 = request.form["password1"]
    ps2 = request.form["password2"]
    if ps1 == ps2:
        with open('admins.csv','r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if nm not in nameList:
                f.writelines("\n")
                f.writelines(f'{nm},{ps1}')
            else:
                return "Already Registered"
    else:
        return "Password doesn't match"
    return render_template('login.html')

@app.route('/delete', methods=["GET", "POST"])
def delete():
    fn = request.form["file"]
    file_name = os.path.join('/home/indhu/Desktop/AttendanceSystem/images/', secure_filename(fn))
    os.remove(file_name) 
    folder = 'images'
    images = []
    for filename in os.listdir(folder):
        images.append(filename)
    return render_template('admin.html',images=images)

@app.route('/update', methods=["GET", "POST"])
def update():
    fn = request.form["oldfile"]
    file = request.files["file"]
    file_name = os.path.join('/home/indhu/Desktop/AttendanceSystem/images/', secure_filename(file.filename))
    file.save(file_name)
    fn1 = os.path.join('/home/indhu/Desktop/AttendanceSystem/images/', secure_filename(fn))
    os.remove(fn1)
    folder = 'images'
    images = []
    for filename in os.listdir(folder):
        images.append(filename)
    return render_template('admin.html',images=images)

@app.route('/insert', methods=["GET", "POST"])
def insert():
    file = request.files["file"]
    file_name = os.path.join('/home/indhu/Desktop/AttendanceSystem/images/', secure_filename(file.filename))
    file.save(file_name)
    folder = 'images'
    images = []
    for filename in os.listdir(folder):
        images.append(filename)
    return render_template('admin.html',images=images)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    nm = request.form["username"]
    ps = request.form["password"]
    print(nm, ps)
    with open('admins.csv','r+') as f:
        myDataList = f.readlines()
        nameList, pswList = [], []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            pswList.append(entry[1])
    adminsList = list(zip(nameList, pswList))
    print(adminsList)
    for admin in adminsList:
        if admin != adminsList[-1]:
            psw = (admin[1])[:-1]
        else:
            psw = admin[1]
        print(admin[0], psw)
        if admin[0] == nm and psw == ps:
            folder = 'students'
            images = []
            for filename in os.listdir(folder):
                images.append(filename)
            return render_template('admin.html', images=images)
    return "Invalid Credentials!"

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
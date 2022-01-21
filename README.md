## Title
Facial Recognition based Attendance System
## Objective
To build a robust and stable system to record attendance Which can overcome the below drawbracks.<br>
#### Existing Methods and their drawbacks:
1. Taking attendance manually with a sheet of paper by calling names during lecture hours. <br>
  - Time consuming
  - Involves Manual work
2. Adopted biometrics system such as fingerprint, RFID card reader to mark the attendance.<br>
  - There is a chance of card loss or an unauthorized person may misuse the card for fake attendance.
  - In biometrics such as fingerprints are not recommended due to COVID-19.
## Description
A facial recognition based attendance system is a software designed to solve the issues of existing manual systems by marking the attendance through recognizing faces and automatically generating attendance reports.
## Modules used
- MTCNN
- pillow
- keras
- tensorflow
- sklearn
## Getting Started
- Clone the repository
- Place the dataset folder parallel to app.py file 
- Run the application with the command "flask run"
## Using the application
Once the application opens, a student mark his / her attendance for a particular class or an admin can login with admin credentials
<br/> An admin can do the following operations : 
1. Add - click on add, choose image and add an image in dataset when new student joins the class
2. Delete - delete an image in dataset when a student leaves the class
3. Update - click on update, choose image and update an image in dataset to update the face
<br/> On doing these operations, the train dataset gets modified and the model can recognize faces from the updated dataset
## Results
#### Home Page 
<img src="/screenshots/homepage.png" width="750" height="450"> <br/><br/>
#### Login 
<img src="/screenshots/login.png" width="750" height="450"> <br/><br/>
#### Admin Dashboard 
<img src="/screenshots/dashboard.png" width="750" height="450"> <br/><br/>

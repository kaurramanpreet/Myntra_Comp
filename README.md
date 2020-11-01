<img src="https://user-images.githubusercontent.com/29287671/97078166-ba3bde80-1607-11eb-9a4e-7d5e223e7d58.png" width="140">

# Myntra HackerRamp
## :bulb: Problem Statement
```
An effective way to implement social distancing for On-Site Service employees working at places like warehouses, malls etc
where the employees cannot be shifted to work from home.
```
## :warning: TechStack/framework used
* Python
* OpenCV
* Keras
* Tensorflow
* Yolov3
* Nodejs
* express
## **STEPS IN OUR PROJECT**
:file_folder: *PARTS(FOLDERS) OF THIS REPOSITORY*
---
* Code for counting the number of people entered and exited the area has been added in **ENTRY_EXIT COUNT** folder.
* Code for detecting nose and mask i.e. mask has been worn, not worn and not properly worn has been added in **MASK AND NOSE DETECTION.**
* Code for measuring the distance between 2 people is implemented which keeps a check on the social distancing rules and had been added in **distance** folder.
* Code for hosting the full project as a web application is implemented in **WebServer** folder.
---
## :star: *WebServer folder*

* currently the work includes to run all the features of our project from a web application.
* it is based on MVC structure.
```  
for running just run the server using the command npm start from the root directory. 
```
## :hourglass: **Project Demo**

![WebApp](Outputs/Webapp.png)

## :star: *ENTRY_EXIT COUNT folder*

* counter.py :- The file that contains the implementation logic of people counter
* people_capture.mp4 :- The input video file used to test the code 
```  
for checking this code just run the counter.py file and you would be able to see the count of number of people entered in a store(room) and the count of people exited from the store(room) 
```
## :hourglass: **Project Demo**

![counter](Outputs/counter.gif)
---
## :star: *MASK AND NOSE DETECTION*
* Initially the work includes to check whether the person is wearing the mask or not
> * So we have tried to include the other part as well in which even if the person is wearing the mask , our code will check whether the mask is worn properly or not by detecting the nose(nostrils) or if the person is using hands instead of mask.
* code_mask.py :-The file that contains the implementation logic of Mask Detection.
* haarcascade_frontalface_alt2.xml :- Pre-trained haarcascade model to detect face.
* haarcascade_mcs_nose.xml :- Pre-trained haarcascade model to detect nose.
* mask_v1.mp4 :- The input file used to check the code for the validity in the above 3 cases.
* mask_v2.mp4 :- The input file used to check the code by using hands instead of mask.
* model.h5 :- Pre-trained MobileNet-V2 model based on ImageNet Database
``` 
for checking the code just go to this folder and run the code_mask.py file and the results would be shown as
```
## :hourglass: **Project Demo**

![mask](Outputs/mask.gif)
---
## :star: *distance folder*
* it is used to find the distance between 2 persons and generated an red alarm when the people are not following the social distancing rule 
* SocialDistancingDetector.py :- The file that contains the implementation logic of checking the social distance between people.
* vtest.avi :- The input file used to check the code.
``` 
for checking the code just go to this folder and run the SocialDistancingDetector.py file and the results would be shown as 
```
## :hourglass: **Project Demo**

![social distancing](Outputs/social-dist.gif)

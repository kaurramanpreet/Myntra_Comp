<img src="https://user-images.githubusercontent.com/29287671/97078166-ba3bde80-1607-11eb-9a4e-7d5e223e7d58.png" width="140">

# Myntra HackerRamp
## Problem Statement
```
An effective way to implement social distancing for On-Site Service employees working at places like warehouses, malls etc
where the employees cannot be shifted to work from home.
```
## TechStack/framework used
* OpenCV
* Keras
* Tensorflow
* Yolov3
## **STEPS IN OUR PROJECT**
*PARTS(FOLDERS) OF THIS REPOSITORY*
---
* code for counting the number of people entered and exited the area has been added in ENTRY_EXIT COUNT folder
* code for detecting nose and mask i.e. mask has been worn, not worn and not properly worn all the cases are detected properly
* code for measuring the distance between 2 people is implemented and it reflects if someone is not following social distancing rules
---
## *ENTRY_EXIT COUNT folder*

* it has 2 files one is py file and the other one is the video on which we can run that file and check whether the counter file is working properly or not
* ``` for checking this code just run the counter.py file and you would be able to see the count of number of people entered in a store(room) and the count of people exited from the store(room) ```
---
## *MASK AND NOSE DETECTION*
* currently the work includes to check whether the person is wearing the mask or not
> * so we have tried to include the other part as well in which even if the person is wearing the mask our code will check whether the mask is worn properly or not by detecting the nose(nostrils) or if the person is using hands instead of mask....all these things are taken care in our code 
* ``` for checking the code just go to this folder and run the code_mask.py file ```
---
## *distance folder*
* it is used to find the distance between 2 persons and generated an red alarm when the people are not following the social distancing rule
* ``` for checking the code just go to this folder and run the SocialDistancingDetector.py file and you would be able to see the results ```


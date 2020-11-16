import numpy as np
import cv2
import imutils
import os
import os
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
import shlex, subprocess
p = subprocess.Popen('Python counter.py')
if p.poll() != None:
    print("killed")
    p.kill()
# print("raman")
import scipy.io
import scipy.misc
import numpy as n
import pandas as pd
import PIL
import struct
import cv2
from numpy import expand_dims
import tensorflow as tf
from skimage.transform import resize
from keras import backend as K
from keras.layers import Input, Lambda, Conv2D, BatchNormalization, LeakyReLU, ZeroPadding2D, UpSampling2D
from keras.models import load_model, Model
from keras.layers.merge import add, concatenate
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from matplotlib.patches import Rectangle
import time

def Check(a,  b):
    dist = ((a[0] - b[0]) ** 2 + 550 / ((a[1] + b[1]) / 2) * (a[1] - b[1]) ** 2) ** 0.5
    calibration = (a[1] + b[1]) / 2       
    if 0 < dist < 0.25 * calibration:
        return True
    else:
        return False

def Setup(yolo):
    global net, ln, LABELS
    net_h, net_w = 416, 416
    obj_thresh, nms_thresh = 0.5, 0.45
    anchors = [[116,90,  156,198,  373,326],  [30,61, 62,45,  59,119], [10,13,  16,30,  33,23]]
    labels = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", \
                  "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", \
                  "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", \
                  "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", \
                  "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", \
                  "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", \
                  "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", \
                  "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse", \
                  "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", \
                  "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]

    # make the yolov3 model to predict 80 classes on COCO

    weights=os.path.sep.join([yolo, "yolov3.weights"])
    config = os.path.sep.join([yolo, "yolov3.cfg"])
    labelsPath = os.path.sep.join([yolo, "coco.names"])
    LABELS = open(labelsPath).read().strip().split("\n")  
    net = cv2.dnn.readNetFromDarknet(config, weights)
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

def ImageProcess(image):
    global processedImg
    (H, W) = (None, None)
    frame = image.copy()
    if W is None or H is None:
        (H, W) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    starttime = time.time()
    layerOutputs = net.forward(ln)
    stoptime = time.time()
    print("Video is Getting Processed at {:.4f} seconds per frame".format((stoptime-starttime))) 
    confidences = []
    outline = []
    
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            maxi_class = np.argmax(scores)
            confidence = scores[maxi_class]
            if LABELS[maxi_class] == "person":
                if confidence > 0.5:
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    outline.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))

    box_line = cv2.dnn.NMSBoxes(outline, confidences, 0.5, 0.3)

    if len(box_line) > 0:
        flat_box = box_line.flatten()
        pairs = []
        center = []
        status = [] 
        for i in flat_box:
            (x, y) = (outline[i][0], outline[i][1])
            (w, h) = (outline[i][2], outline[i][3])
            center.append([int(x + w / 2), int(y + h / 2)])
            status.append(False)

        for i in range(len(center)):
            for j in range(len(center)):
                close = Check(center[i], center[j])

                if close:
                    pairs.append([center[i], center[j]])
                    status[i] = True
                    status[j] = True
        index = 0

        for i in flat_box:
            (x, y) = (outline[i][0], outline[i][1])
            (w, h) = (outline[i][2], outline[i][3])
            if status[index] == True:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 150), 2)
            elif status[index] == False:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            index += 1
        for h in pairs:
            cv2.line(frame, tuple(h[0]), tuple(h[1]), (0, 0, 255), 2)
    cv2.imshow('video',frame)
    processedImg = frame.copy()


# define a video capture object
fourcc=cv2.VideoWriter_fourcc(*'XVID')

out=cv2.VideoWriter('output.avi',fourcc,20.0,(1280,720))
     
create = None
frameno = 0
filename = "./vtest.AVI"
yolo = "yolo/"
opname = "output_videos/output_of_" + filename.split('/')[1][:-4] + '.mp4'
cap = cv2.VideoCapture(filename)

time1 = time.time()
while(True):

    ret, frame = cap.read()
    if not ret:
        break
    
    current_img = frame.copy()
    current_img = imutils.resize(current_img, width=480)
    video = current_img.shape
    frameno += 1

    if(frameno%2 == 0 or frameno == 1):
        Setup(yolo)
        ImageProcess(current_img)
        Frame = processedImg

        if create is None:
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            create = cv2.VideoWriter(opname, fourcc, 30, (Frame.shape[1], Frame.shape[0]), True)
    create.write(Frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
    out.write(Frame)
    
time2 = time.time()
print("Completed. Total Time Taken: {} minutes".format((time2-time1)/60))
      
out.release()

cap.release()
cv2.destroyAllWindows()

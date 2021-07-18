import cv2
import os
from tensorflow.keras.models import load_model
import numpy as np
import time
from playsound import playsound


face = cv2.CascadeClassifier('haar cascade files\haarcascade_frontalface_alt.xml')
leye = cv2.CascadeClassifier('haar cascade files\haarcascade_lefteye_2splits.xml')
reye = cv2.CascadeClassifier('haar cascade files\haarcascade_righteye_2splits.xml')



lbl=['Close','Open']

model = load_model('models/drowsinessModel.h5')
path = os.getcwd()
cap = cv2.VideoCapture(0)
cap.set(1, 300)
cap.set(1, 200)
# Min Height and Width for the  window size to be recognized as a face
minW = 0.1 * cap.get(3)
minH = 0.1 * cap.get(4)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
count=0
score=0
thicc=2
rpred=[99]
lpred=[99]

while(True):
    ret, frame = cap.read()
    height,width = frame.shape[:2]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(int(minW), int(minH)))
    left_eye = leye.detectMultiScale(gray)
    right_eye =  reye.detectMultiScale(gray)

    cv2.rectangle(frame, (0,height-50) , (300,height) , (255,0,0) , thickness=cv2.FILLED )
    

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y) , (x+w,y+h) , (198,43,231) , 2)

    for (x,y,w,h) in right_eye:
        r_eye=frame[y:y+h,x:x+w]
        count=count+1
        r_eye = cv2.cvtColor(r_eye,cv2.COLOR_BGR2GRAY)
        r_eye = cv2.resize(r_eye,(35,35)) # Note: change this number same as the imageH and imageW of training model, if you change size in that.
        r_eye= r_eye/255
        r_eye=  r_eye.reshape(35,35,-1) # Note: change this number same as the imageH and imageW of training model, if you change size in that.
        r_eye = np.expand_dims(r_eye,axis=0)
        rpred = model.predict_classes(r_eye)
        if(rpred[0]==1):
            lbl='Open' 
        if(rpred[0]==0):
            lbl='Closed'
        break

    for (x,y,w,h) in left_eye:
        l_eye=frame[y:y+h,x:x+w]
        count=count+1
        l_eye = cv2.cvtColor(l_eye,cv2.COLOR_BGR2GRAY)  
        l_eye = cv2.resize(l_eye,(35,35))# Note: change this number same as the imageH and imageW of training model, if you change size in that.
        l_eye= l_eye/255
        l_eye=l_eye.reshape(35,35,-1)# Note: change this number same as the imageH and imageW of training model, if you change size in that.
        l_eye = np.expand_dims(l_eye,axis=0)
        lpred = model.predict_classes(l_eye)
        if(lpred[0]==1):
            lbl='Open'   
        if(lpred[0]==0):
            lbl='Closed'
        break

    if(rpred[0]==0 and lpred[0]==0):
        score=score+1
        cv2.putText(frame,"Closed",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
    # if(rpred[0]==1 or lpred[0]==1):
    else:
        score=score-1
        cv2.putText(frame,"Open",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
    
        
    if(score<0):
        score=0   
    cv2.putText(frame,'Time: '+str(score)+' second',(100,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
    if(score>10):
        #person is feeling sleepy so we beep the alarm
        try:
            playsound('alarm.wav')
                 
        except:  # isplaying = False
            pass
        if(thicc<16):
            thicc= thicc+2
        else:
            thicc=thicc-2
            if(thicc<2):
                thicc=2
        cv2.rectangle(frame,(0,0),(width,height),(255,255,255),thicc) 
    cv2.imshow('Drowsiness_Detection',frame)
    if cv2.waitKey(1) & 0xFF == ord('b'):
        break
cap.release()
cv2.destroyAllWindows()

# Written by: Hemaraj Dhakal
# Github username: Hemraj183

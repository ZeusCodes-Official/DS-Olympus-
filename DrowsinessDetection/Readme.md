# Drowsiness Detection

## Introduction
This project detects whether the person has slept or not. Can be implemented onthe highway to finds the driver is sleeping or not while driving to avoid any accidents.
This project plays the beep sound if the person's eyes are closed for 10 seconds.

## Tech Stack
Python
Tensorflow/Keras
Opencv
numpy
playsound

## Apporach
First I have collect the dataset from the kaggle which has eyes closed, open, yawn and not yawn dataset, so i remove the yawn and not yawn data after that make neural network using 
keras. I compress the picture as 35*35 and get around 97% accuracy within 5 epochs. I used keras callback model to so while training the model, it will save the best model and you can choose any one in detection.
You can increase and decrease the image size, epochs and batch size to for getting good result.Play around with numbers for better result.
For the model i used 30 epochs and gets the best accuracy in 24 epochs of 0.922 and around 98% validation accuracy due to callback the best epchos has been saved.
The accuracy only doesnot matter the best validation accuracy model has been used.



## Images
#### Accuracy with 35X35 image size.
![image](https://user-images.githubusercontent.com/65659902/125934094-9fc59786-d4cb-40c3-bb2c-b28b667690f8.png)

#### Some Best accuarcy screenshot
![image](https://user-images.githubusercontent.com/65659902/125935276-b5ff45ce-a7b8-46f6-9e4d-9e22c3be847f.png)

#### Testing

![image](https://user-images.githubusercontent.com/65659902/125936419-2b217a88-96be-4dab-9fe4-c62993902d99.png)

![image](https://user-images.githubusercontent.com/65659902/125936761-4b8bc112-2ad5-4807-9f19-3c1c55c2f5c4.png)

![image](https://user-images.githubusercontent.com/65659902/125936877-9010051c-c46d-468a-b62c-386df8880a71.png)

![image](https://user-images.githubusercontent.com/65659902/125936507-bc425586-9db8-4dc0-ac31-2a37b63c2485.png)

#### Beep Sound

<a href=alarm.wav”>Alarm Sound</a>




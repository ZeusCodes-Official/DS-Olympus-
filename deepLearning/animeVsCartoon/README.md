# Anime vs Cartoon

### <i> Try it yourself - https://animevscartoon.herokuapp.com/ </i>
### <i> Demonstration Video - https://www.youtube.com/watch?v=BlhWdVGG0Hw/ </i>
<br>

[![Cover Image](https://github.com/kanakmi/Anime-vs-Cartoon/blob/main/Cover.png?raw=True)](https://animevscartoon.herokuapp.com/)

## Tech Stack

![Python](https://img.shields.io/badge/Python-v3.8-red?style=flat-square&logo=python&logoColor=red)
![Tensorflow](https://img.shields.io/badge/tensorflow-v2.3.0-orange?style=flat-square&logo=tensorflow)
![Flask](https://img.shields.io/badge/Flask-v2.0.1-brightgreen?style=flat-square&logo=flask&logoColor=brightgreen)
![HTML](https://img.shields.io/badge/HTML-5-blueviolet?style=flat-square&logo=html5&logoColor=blueviolet)
![CSS](https://img.shields.io/badge/CSS-3-blue?style=flat-square&logo=css3&logoColor=blue)
![JS](https://img.shields.io/badge/JAVASCRIPT--black?style=flat-square&logo=javascript)

## Overview

Is Anime and Cartoon the same? There is always a confusion around this.<br>
To solve this never ending debate question, I've created a classifier that can distinguish between the images of Anime and a Cartoon. <br>
I've created a Convolutional Neural Network that uses 9148 images (4451 of Anime and 4697 of Cartoon) for the classification task.<br>
I scrapped the Dataset myself and uploaded it on drive for others to use and the link for the same is - https://drive.google.com/drive/folders/1NkQK7SrPRvbmdgMTEsJQ5-i-oY4kzVLL?usp=sharing <br>
For testing the best model, 1830 images are used out of which 50% (915) images form the Validation Set. 
The model with the least Validation Loss is saved for future predictions.<br>
The best saved model gives an Accuracy of 87% with a good balance between Precision and Recall.
<br>

## About the Model

The Model contains 5 layers of Convolutional Neural Networks with different hyperparameters. Each CNN layer is followed by a MaxPooling2D layer. The second convolutional layer also uses padding to give importance to the features lying in the corners of the images. The dropout layers are added for regularization (to prevent the model from overfitting the training data).<br>
The output from the last Convolutional layer is then Flattened and passed over to a dense Artificial Neural Network containing 3 hidden layers (also some dropout layers) and finally an output layer.<br>
The model has over 1 Million trainable parameters.<br>

### Libraries Required for running the code inside Jupyter Notebook

1. tensorflow 2.3.0 (or above)
2. opencv-python 4.5.2.54
3. scikit-learn 0.24.2
4. matplotlib 3.4.2 (only for visualization)
5. seaborn 0.11.1 (only for visualization)

## UI for the APP

<i>The basic UI for the app is taken from Sports Classifier project made by Dhaval Patel. I have made multiple changes in his code but the html and css file are essentially the same. Link to his Youtube Channel - https://www.youtube.com/channel/UCh9nVJoWXmFb7sLApWGcLPQ</i><br><br>
The <b>app.py</b> file contains the Flask server required to run this app on the system.<br>
The <b>util.py</b> file contains the steps that are performed once the user uploads an image to the app. The saved model is loaded from the memory and input image is preprocessed, predictions are made and the result is routed to the <b>app.js</b> file which maps the output onto the Webpage.<br>

### Libraries Required for GUI & Server -

The required libraries are mentioned in the <b>requirements.txt</b> file inside UI folder and can be simply installed using command <i>pip install requirements.txt</i>

## Steps to Run UI on your system -

1. Download the UI and Trained_Model folder from the repository.
2. Install the required libraries.
3. Run the app.py file and you are ready to go.
{"mode":"full","isActive":false}

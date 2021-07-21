# Dogs vs Cat Classification 
The following file uses concept of transfer learning to achive 98% accuracy on test data for classification.


**Dataset Link-** https://www.kaggle.com/chetankv/dogs-cats-images

**Model Used-** <b><i>[MobileNet V2](https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4)</i></b> is a family of neural network architectures for efficient on-device image classification and related tasks.Mobilenets come in various sizes controlled by a multiplier for the depth (number of features) in the convolutional layers. They can also be trained for various sizes of input images to control inference speed.

This TF-Hub module uses the TF-Slim implementation of mobilenet_v2 with a depth multiplier of 1.0 and an input size of 224x224 pixels.

The module contains a trained instance of the network, packaged to get feature vectors from images. 
If you want the full model including the classification it was originally trained for, use [`module google/tf2-preview/mobilenet_v2/classification/4`](https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4) instead.

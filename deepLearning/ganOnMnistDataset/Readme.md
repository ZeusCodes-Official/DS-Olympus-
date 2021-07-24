# GAN On MNIST Dataset

A generative adversarial network (GAN) is a class of machine learning frameworks designed by Ian Goodfellow and his colleagues in 2014. Two neural networks contest with each other in a game (in the form of a zero-sum game, where one agent's gain is another agent's loss).

Given a training set, this technique learns to generate new data with the same statistics as the training set. For example, a GAN trained on photographs can generate new photographs that look at least superficially authentic to human observers, having many realistic characteristics. Though originally proposed as a form of generative model for unsupervised learning, GANs have also proven useful for semi-supervised learning, fully supervised learning, and reinforcement learning.

The MNIST database (Modified National Institute of Standards and Technology database) is a large database of handwritten digits that is commonly used for training various image processing systems. The database is also widely used for training and testing in the field of machine learning. It was created by "re-mixing" the samples from NIST's original datasets. The creators felt that since NIST's training dataset was taken from American Census Bureau employees, while the testing dataset was taken from American high school students, it was not well-suited for machine learning experiments. Furthermore, the black and white images from NIST were normalized to fit into a 28x28 pixel bounding box and anti-aliased, which introduced grayscale levels.
![image](https://user-images.githubusercontent.com/65659902/126862336-9f439559-23ce-4b23-8054-4828e27c831d.png)

The MNIST database contains 60,000 training images and 10,000 testing images. Half of the training set and half of the test set were taken from NIST's training dataset, while the other half of the training set and the other half of the test set were taken from NIST's testing dataset. The original creators of the database keep a list of some of the methods tested on it. In their original paper, they use a support-vector machine to get an error rate of 0.8%. An extended dataset similar to MNIST called EMNIST has been published in 2017, which contains 240,000 training images, and 40,000 testing images of handwritten digits and characters.

## Model Summery
![image](https://user-images.githubusercontent.com/65659902/126861955-7853bfb2-81f7-4458-ba76-4c24ad53ac95.png)

## discriminator_plot
![image](https://github.com/Hemraj183/DS-Olympus-/blob/main/deepLearning/ganOnMnistDataset/discriminator_plot.png)

## Output on Diffrent Epochs
### 10Epochs
![image](https://github.com/Hemraj183/DS-Olympus-/blob/main/deepLearning/ganOnMnistDataset/generated_plot_e010.png)

### 30Epochs
![image](https://github.com/Hemraj183/DS-Olympus-/blob/main/deepLearning/ganOnMnistDataset/generated_plot_e030.png)

### 50Epochs
![image](https://github.com/Hemraj183/DS-Olympus-/blob/main/deepLearning/ganOnMnistDataset/generated_plot_e050.png)

### 80Epochs
![image](https://github.com/Hemraj183/DS-Olympus-/blob/main/deepLearning/ganOnMnistDataset/generated_plot_e080.png)

### 90Epochs
![image](https://github.com/Hemraj183/DS-Olympus-/blob/main/deepLearning/ganOnMnistDataset/generated_plot_e090.png)

### 100Epochs
![image](https://github.com/Hemraj183/DS-Olympus-/blob/main/deepLearning/ganOnMnistDataset/generated_plot_e100.png)

### Result
![image](https://user-images.githubusercontent.com/65659902/126862415-28c6b759-64f8-4a68-a898-ef8a6602d7a2.png)

### Colab Link
(https://colab.research.google.com/drive/1OGAsYdcyXFN0Vc85CbwVtmgjUGVc7eAx?usp=sharing)

# Thank You -By Hemaraj Dhakal

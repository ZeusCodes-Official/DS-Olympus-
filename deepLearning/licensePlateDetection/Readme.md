## License Plate Detection Using CNN

* WorkFlow
  
  * Data Preparation

       * Importing Dependencies

       * Loading the dataset

       * Image Resizing

       * Feature Extraction

  * Splitting the Dataset

  * Model Creation

       * Creating Sequential CNN layers(Dense,Flatten,VGG16)
 
  * Accuracy Evaluation

  * Running the model on our test data

  * Prediction

I have applied Canny Edge Detection and Threshold to draw contours and attemped to recognise the numbers from the license plate. For that purpose, I used pytesseract module(you can also use third party software called Tesseract OCR)

  

Download the dataset folder from <a href="https://www.kaggle.com/andrewmvd/car-plate-detection"> here </a>

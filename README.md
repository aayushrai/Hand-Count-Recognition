# Hand-Count-Recognition

Design to recognition Hand Count using **Convolutional Neural Network**.CNN used for classification of images for different hand count.A Convolutional Neural Network (ConvNet/CNN) is a Deep Learning algorithm which can take in an input image, assign importance (learnable weights and biases) to various aspects/objects in the image and be able to differentiate one from the other. The pre-processing required in a ConvNet is much lower as compared to other classification algorithms. While in primitive methods filters are hand-engineered, with enough training, ConvNets have the ability to learn these filters/characteristics.In this project **Keras API** used for building a CNN.

## Details

For image processing and data collection **Opencv Python3 Module** used. Apply different image **Thresholding** technique to remove the unnecessary information from the image which is not required for hand count recognization and after thresholding only those information remains which is required.Thresholding is a technique in OpenCV, which is the assignment of pixel values in relation to the threshold value provided. In thresholding, each pixel value is compared with the threshold value. If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a maximum value (generally 255).

### Threshold image
![](https://answers.opencv.org/upfiles/13506303131033303.png)

# Project images

### Prediction
![](https://github.com/aayushrai/Hand-Count-Recognition/blob/master/prediction_gif.gif)

### Training
![](https://github.com/aayushrai/Hand-Count-Recognition/blob/master/T_image.jpg)


### Installing

A step by step series of examples that tell you how to get a development env running:-

First install python3 

```
https://www.python.org/downloads/this 
```

Then install opencv module in python3 

```
https://pypi.org/project/opencv-python/
pip install opencv-python
```

Then install numpy module in python3

```
https://pypi.org/project/numpy/
pip install numpy
```
And then install keras python3 deep learning library

```
https://pypi.org/project/Keras/
pip install Keras
```
## Authors

* **Aayush rai** - *Initial work* - [aayushrai](https://github.com/aayushrai)

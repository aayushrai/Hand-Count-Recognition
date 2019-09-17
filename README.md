# Hand-Count-Recognition

Design to recognition Hand Count using **Deep learning CNN Model**.

# Hand Count Example

![image](https://github.com/aayushrai/Automated_attendence/blob/master/images/1.PNG)

## Details

This project has four files KerasModel.py ,Prediction.py ,Training_data_collection.py ,hand.h5, Training_data_collection.py file contains code for collection of training data. Training data refer collection of hand image which use to train CNN keras model.

**Opencv Python3 Module** for collection of image data and image processing. KerasModel.py file contain code for **CNN Deep Learning Model** which use create weight, with the help of this weight we can recognize hand count. 

Prediction.py file use to predict hand count by showing hand in camera, prediction file use weight for prediction. weight save in hand.h5 file.

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

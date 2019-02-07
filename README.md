# Hand-Count-Recognition

This project recognition number of fingers, which you are showing in camera with help of **Deep learning CNN Model**.

## Details

This project has four files KerasModel.py ,Prediction.py ,Training_data_collection.py ,hand.h5. Training_data_collection.py file contain 
code for collection of training data for keras model. Training data refer collection of hand image which use to train CNN keras model.

For collection of image data and image processing i use **Opencv Python3 Module**. KerasModel.py file contain code for **CNN Deep Learning Model** which use create weight, with the help of this weight we can recognize hand count. 

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

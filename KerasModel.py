from keras.models import Sequential
from keras.layers import Dense,Conv2D,MaxPooling2D,Flatten,Activation,Dropout
from keras.preprocessing.image import ImageDataGenerator

img_gen = ImageDataGenerator(width_shift_range=.1,height_shift_range=.1,rescale=1/255,shear_range=.2,horizontal_flip=True,fill_mode="nearest")


model = Sequential()
model.add(Conv2D(filters=32,kernel_size=(3,3),input_shape=(250,230,3),activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(filters=64,kernel_size=(3,3),input_shape=(250,230,3),activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(filters=64,kernel_size=(3,3),input_shape=(250,230,3),activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(128))
model.add(Activation("relu"))
model.add(Dropout(.5))
model.add(Dense(6))
model.add(Activation("sigmoid"))

model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=["accuracy"])

train_image_gen = img_gen.flow_from_directory("hand",target_size=(250,230),batch_size= 5)
print(train_image_gen.class_indices)
results = model.fit_generator(train_image_gen,epochs=50,steps_per_epoch=100)
model.save("hand2.h5")

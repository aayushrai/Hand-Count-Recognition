from keras.models import load_model
from keras.preprocessing import image
import cv2
import numpy as np

model = load_model("hand.h5")
prediction = [0]
camera = cv2.VideoCapture(0)

def Ablock(frame):
    block = frame[165:415,365:595]
    block = cv2.medianBlur(block,3)
    block = cv2.adaptiveThreshold(block,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,199,8)
    cv2.imshow("Ablock", block)
    return block

while True:

    ret,frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret:
        cv2.putText(frame,str(prediction[0]), (10,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.rectangle(frame,(360,160),(600,420),(0,0,255),5)
        cv2.imshow("Video",frame)
    else:
        print("camera not found")
        break

    Ablock2 = Ablock(frame)

    cv2.imwrite("img.jpeg", Ablock2)
    img = cv2.imread("img.jpeg")
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / img.max()

    prediction = model.predict_classes(img)
    print(model.predict_classes(img))    print(model.predict(img))

    if cv2.waitKey(20) & 0xFF == 27:
           break
cv2.destroyAllWindows()
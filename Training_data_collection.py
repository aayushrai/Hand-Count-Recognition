import cv2,random
import os

camera = cv2.VideoCapture(0)
def block(frame):
    block = frame[165:415,365:595]
    block = cv2.medianBlur(block,7)
    ret,block = cv2.threshold(block,127,255,cv2.THRESH_BINARY)
    cv2.imshow("block", block)
    return block
def Ablock(frame):
    block = frame[165:415,365:595]
    block = cv2.medianBlur(block,3)
    block = cv2.adaptiveThreshold(block,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,199,8)
    cv2.imshow("Ablock", block)
    return block
def create_folder(lis):
    os.getcwd()
    for i in lis:
        if not os.path.exists("hand"):
            os.mkdir("hand")
        if not os.path.exists("hand\\"+str(i)):
            os.mkdir("hand\\"+ str(i))

create_folder([0,1,2,3,4,5])

while True:
    rand = random.randint(0,10000)
    file = []
    for i in range(len(os.listdir("hand\\"))):
        file.append(len(os.listdir("hand\\"+ str(i))))


    ret,frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret:
        cv2.putText(frame,"zero:"+str(file[0]), (10,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "one:" + str(file[1]), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,cv2.LINE_AA)
        cv2.putText(frame, "two:" + str(file[2]), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,cv2.LINE_AA)
        cv2.putText(frame, "three:" + str(file[3]), (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,cv2.LINE_AA)
        cv2.putText(frame, "four:" + str(file[4]), (10, 160), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,cv2.LINE_AA)
        cv2.putText(frame, "five:" + str(file[5]), (10, 190), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,cv2.LINE_AA)

        cv2.rectangle(frame,(360,160),(600,420),(0,0,255),5)
        cv2.imshow("Video",frame)
    else:
        print("camera not found")
        break
    Ablock2 = Ablock(frame)
    if cv2.waitKey(20) & 0xFF == 27:
        break

    if cv2.waitKey(30) & 0xFF == ord("0"):
         print("hand\\0\\{}.jpeg".format(file[0]+rand))
         cv2.imwrite("hand\\0\\{}.jpeg".format(file[0]+rand),Ablock2)
    if cv2.waitKey(30) & 0xFF == ord("1"):
         print("hand\\1\\{}.jpeg".format(file[1]+rand))
         cv2.imwrite("hand\\1\\{}.jpeg".format(file[1]+rand),Ablock2)
    if cv2.waitKey(30) & 0xFF == ord("2"):
         print("hand\\2\\{}.jpeg".format(file[2]+rand))
         cv2.imwrite("hand\\2\\{}.jpeg".format(file[2]+rand),Ablock2)
    if cv2.waitKey(30) & 0xFF == ord("3"):
         print("hand\\3\\{}.jpeg".format(file[3]+rand))
         cv2.imwrite("hand\\3\\{}.jpeg".format(file[3]+rand),Ablock2)
    if cv2.waitKey(30) & 0xFF == ord("4"):
        print("hand\\4\\{}.jpeg".format(file[4]+rand))
        cv2.imwrite("hand\\4\\{}.jpeg".format(file[4]+rand), Ablock2)
    if cv2.waitKey(30) & 0xFF == ord("5"):
         print("hand\\5\\{}.jpeg".format(file[5]+rand))
         cv2.imwrite("hand\\5\\{}.jpeg".format(file[5]+rand),Ablock2)


cv2.destroyAllWindows()
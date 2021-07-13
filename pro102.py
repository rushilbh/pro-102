import cv2
import time
import random

start_time = time.time()

def take_task():
    number = random.randint(0,100)
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        task_name = "task"+str(number)+".png"
        cv2.imwrite(task_name, frame)
        start_time = time.time
        result = False

    print("task noted")

    videoCaptureObject.release()

    cv2.destroyAllWindows()
    return task_name

def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_task()


main() 

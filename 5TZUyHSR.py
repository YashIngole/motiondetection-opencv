import numpy as np
import serial
import time
import sys
import cv2

arduino = serial.Serial('COM3', 9600) # remember to change the COM port to your arduino port
time.sleep(2)
print("Connection to arduino...")


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    if ret == True:
        cv2.namedWindow("img", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('img', 500, 500)
        cv2.line(img, (500, 250), (0, 250), (0, 255, 0), 1)
        cv2.line(img, (250, 0), (250, 500), (0, 255, 0), 1)
        cv2.circle(img, (250, 250), 5, (255, 255, 255), -1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            arr = {y: y+h, x: x+w}
            print(arr)

            print('X :' + str(x))
            print('Y :'+str(y))
            print('x+w :' + str(x+w))
            print('y+h :' + str(y+h))

            xx = int(x+(x+h))/2
            yy = int(y+(y+w))/2

            print(xx)
            print(yy)

            center = (xx, yy)

            print("Center of Rectangle is :", center)
            data = "X{0:d}Y{1:d}Z".format( int(xx), int(yy))
            print(f'output = {data } ')
            arduino.write(data.encode('utf-8'))

        cv2.imshow('img', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break

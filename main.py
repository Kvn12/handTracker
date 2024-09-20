import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller
import time

video = cv2.VideoCapture(0)

video.set(3,1280)
video.set(4,720)

kb = Controller()

detector = HandDetector(detectionCon=0.8)
estadoAtual = [0,0,0,0,0]

while True:
    _,img = video.read()
    hands,img = detector.findHands(img)

    if hands:
        estado = detector.fingersUp(hands[0])
        # print("estado: ")
        # print(estado)

        if estado!=estadoAtual and estado == [0,1,0,0,0]:   
            print('Volume Up')
            # with kb.pressed(Key.ctrl):
            kb.press(Key.media_volume_up)
            time.sleep(0.5)
            kb.release(Key.media_volume_up)

        if estado!=estadoAtual and estado == [0,0,0,0,1]:   
            print('Volume Down')
            kb.press(Key.media_volume_down)
            time.sleep(0.5)
            kb.release(Key.media_volume_down)

        if estado!=estadoAtual and estado == [1,1,1,1,1]:   
            print('Play/Pause')
            kb.press(Key.media_play_pause)
            # time.sleep(0.2)
            kb.release(Key.media_play_pause)


            # kb.press(Key.left)
            # kb.release(Key.left)

        # if estado == estadoAtual and estado == [0, 0, 0, 0, 1]:
        #     img[50:216, 984:1230] = setaDir
        # if estado == estadoAtual and estado == [1, 0, 0, 0, 0]:
        #     img[50:216, 50:296] = setaEsq

        estadoAtual = estado

    cv2.imshow('img',cv2.resize(img,(640,420)))
    cv2.waitKey(1)

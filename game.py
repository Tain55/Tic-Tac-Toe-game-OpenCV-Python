import cv2
import mediapipe as mp
from numpy import *

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
index_x = 100
index_y = 1000

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0

circle_or_cross = True

aa = None
bb = None
cc = None
dd = None
ee = None
ff = None
gg = None
hh = None
ii = None

aaa = False
bbb = False
ccc = False
ddd = False
eee = False
fff = False
ggg = False
hhh = False
iii = False

array_value = array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
])

win = False
win11 = False
win21 = False
win31 = False
win41 = False
win51 = False
win61 = False
win71 = False
win81 = False

win12 = False
win22 = False
win32 = False
win42 = False
win52 = False
win62 = False
win72 = False
win82 = False
close = 0


# ekhon ekhane ekta 2d array lagbe..jekhane direct X / O value asbe and seita alada kore print kora hobe

def playing():
    global aa
    global bb
    global cc
    global dd
    global ee
    global ff
    global gg
    global hh
    global ii

    global aaa
    global bbb
    global ccc
    global ddd
    global eee
    global fff
    global ggg
    global hhh
    global iii

    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i

    global win

    global circle_or_cross

    global win11
    global win21
    global win31
    global win41
    global win51
    global win61
    global win71
    global win81

    global win12
    global win22
    global win32
    global win42
    global win52
    global win62
    global win72
    global win82

    global index_x
    global index_y

    global close

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_height, frame_width, _ = frame.shape
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x * frame_width)
                    y = int(landmark.y * frame_height)
                    if id == 8:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        index_x = x
                        index_y = y
                    if id == 4:
                        cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                        thumb_x = x

                        print(abs(index_x - thumb_x))
                        if abs(index_x - thumb_x) < 1:
                            print('clicked')
                            if 0<index_x<50 and 0<index_y<50:
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                f = 0
                                g = 0
                                h = 0
                                i = 0

                                circle_or_cross = True

                                aa = None
                                bb = None
                                cc = None
                                dd = None
                                ee = None
                                ff = None
                                gg = None
                                hh = None
                                ii = None

                                aaa = False
                                bbb = False
                                ccc = False
                                ddd = False
                                eee = False
                                fff = False
                                ggg = False
                                hhh = False
                                iii = False

                                array_value[0][0] = 0
                                array_value[0][1] = 0
                                array_value[0][2] = 0
                                array_value[1][0] = 0
                                array_value[1][1] = 0
                                array_value[1][2] = 0
                                array_value[2][0] = 0
                                array_value[2][1] = 0
                                array_value[2][2] = 0

                                win = False
                                win11 = False
                                win21 = False
                                win31 = False
                                win41 = False
                                win51 = False
                                win61 = False
                                win71 = False
                                win81 = False

                                win12 = False
                                win22 = False
                                win32 = False
                                win42 = False
                                win52 = False
                                win62 = False
                                win72 = False
                                win82 = False
                                close = 1

                            if 0 < index_x < 213 and 0 < index_y < 160:
                                a = 1

                            if 0 < index_x < 213 and 160 < index_y < 320:
                                d = 1

                            if 0 < index_x < 213 and 320 < index_y < 480:
                                g = 1

                            if 213 < index_x < 427 and 0 < index_y < 160:
                                b = 1

                            if 213 < index_x < 427 and 160 < index_y < 320:
                                e = 1

                            if 213 < index_x < 427 and 320 < index_y < 480:
                                h = 1

                            if 427 < index_x < 640 and 0 < index_y < 160:
                                c = 1

                            if 427 < index_x < 640 and 160 < index_y < 320:
                                f = 1

                            if 427 < index_x < 640 and 320 < index_y < 480:
                                i = 1

        cv2.line(frame, (213, 0), (213, 480), (60, 205, 120), 5)
        cv2.line(frame, (427, 0), (427, 480), (60, 205, 120), 5)
        cv2.line(frame, (0, 320), (640, 320), (60, 205, 120), 5)
        cv2.line(frame, (0, 160), (640, 160), (60, 205, 120), 5)


        # Here the main logic part is hidden. You need to fill the 'array_value' with the value '1'
        # for 'O' and '2' for 'X'. If the first one is 'O' than the next one should be 'X' and the
        # next one will be 'O' and it will continuee like this. If a value is taken in the 'array_value'
        # it will not take value again. This is how it can fill all the values without any repeatation.

        

        if array_value[0][0] == 1:
            cv2.putText(frame, "O", (107 - 40, 80 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 141, 47), 9,
                        cv2.LINE_AA)
        if array_value[0][0] == 2:
            cv2.putText(frame, "X", (107 - 40, 80 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (127, 0, 255), 9,
                        cv2.LINE_AA)
        if array_value[0][1] == 1:
            cv2.putText(frame, "O", (320 - 40, 80 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 141, 47), 9,
                        cv2.LINE_AA)
        if array_value[0][1] == 2:
            cv2.putText(frame, "X", (320 - 40, 80 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (127, 0, 255), 9,
                        cv2.LINE_AA)
        if array_value[0][2] == 1:
            cv2.putText(frame, "O", (534 - 40, 80 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 141, 47), 9,
                        cv2.LINE_AA)
        if array_value[0][2] == 2:
            cv2.putText(frame, "X", (534 - 40, 80 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (127, 0, 255), 9,
                        cv2.LINE_AA)
        if array_value[1][0] == 1:
            cv2.putText(frame, "O", (107 - 40, 240 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 141, 47), 9,
                        cv2.LINE_AA)
        if array_value[1][0] == 2:
            cv2.putText(frame, "X", (107 - 40, 240 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (127, 0, 255), 9,
                        cv2.LINE_AA)

        if array_value[1][1] == 1:
            cv2.putText(frame, "O", (320 - 40, 240 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 141, 47), 9,
                        cv2.LINE_AA)
        if array_value[1][1] == 2:
            cv2.putText(frame, "X", (320 - 40, 240 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (127, 0, 255), 9,
                        cv2.LINE_AA)

        if array_value[1][2] == 1:
            cv2.putText(frame, "O", (534 - 40, 240 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 141, 47), 9,
                        cv2.LINE_AA)
        if array_value[1][2] == 2:
            cv2.putText(frame, "X", (534 - 40, 240 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (127, 0, 255), 9,
                        cv2.LINE_AA)

        if array_value[2][0] == 1:
            cv2.putText(frame, "O", (107 - 40, 400 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 141, 47), 9,
                        cv2.LINE_AA)
        if array_value[2][0] == 2:
            cv2.putText(frame, "X", (107 - 40, 400 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (127, 0, 255), 9,
                        cv2.LINE_AA)

        if array_value[2][1] == 1:
            cv2.putText(frame, "O", (320 - 40, 400 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 141, 47), 9,
                        cv2.LINE_AA)
        if array_value[2][1] == 2:
            cv2.putText(frame, "X", (320 - 40, 400 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (127, 0, 255), 9,
                        cv2.LINE_AA)

        if array_value[2][2] == 1:
            cv2.putText(frame, "O", (534 - 40, 400 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 141, 47), 9,
                        cv2.LINE_AA)
        if array_value[2][2] == 2:
            cv2.putText(frame, "X", (534 - 40, 400 + 40), cv2.FONT_HERSHEY_SIMPLEX, 4, (127, 0, 255), 9,
                        cv2.LINE_AA)

        if not win:
            if array_value[0][0] == array_value[0][1] == array_value[0][2]:
                if array_value[0][0] == 1:
                    win11 = True
                    win = True
                if array_value[0][0] == 2:
                    win12 = True
                    win = True

            if array_value[1][0] == array_value[1][1] == array_value[1][2]:
                if array_value[1][0] == 1:
                    win21 = True
                    win = True
                if array_value[1][0] == 2:
                    win22 = True
                    win = True

            if array_value[2][0] == array_value[2][1] == array_value[2][2]:
                if array_value[2][0] == 1:
                    win31 = True
                    win = True
                if array_value[2][0] == 2:
                    win32 = True
                    win = True

            if array_value[0][0] == array_value[1][0] == array_value[2][0]:
                if array_value[0][0] == 1:
                    win41 = True
                    win = True
                if array_value[0][0] == 2:
                    win42 = True
                    win = True

            if array_value[0][1] == array_value[1][1] == array_value[2][1]:
                if array_value[0][1] == 1:
                    win51 = True
                    win = True
                if array_value[0][1] == 2:
                    win52 = True
                    win = True

            if array_value[0][2] == array_value[1][2] == array_value[2][2]:
                if array_value[0][2] == 1:
                    win61 = True
                    win = True
                if array_value[0][2] == 2:
                    win62 = True
                    win = True

            if array_value[0][0] == array_value[1][1] == array_value[2][2]:
                if array_value[0][0] == 1:
                    win71 = True
                    win = True
                if array_value[0][0] == 2:
                    win72 = True
                    win = True

            if array_value[0][2] == array_value[1][1] == array_value[2][0]:
                if array_value[0][2] == 1:
                    win81 = True
                    win = True
                if array_value[0][2] == 2:
                    win82 = True
                    win = True
    ############

        if win11:
            cv2.line(frame, (107, 80), (543, 80), (181, 128, 1), 13)
            cv2.putText(frame, "-|- 0 has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 3, cv2.LINE_AA)

        if win21:
            cv2.line(frame, (107, 240), (543, 240), (213, 169, 75), 13)
            cv2.putText(frame, "-|- 0 has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 3, cv2.LINE_AA)

        if win31:
            cv2.line(frame, (107, 400), (543, 400), (213, 169, 75), 13)
            cv2.putText(frame, "-|- 0 has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 3, cv2.LINE_AA)

        if win41:
            cv2.line(frame, (107, 80), (107, 400), (213, 169, 75), 13)
            cv2.putText(frame, "-|- 0 has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 3, cv2.LINE_AA)

        if win51:
            cv2.line(frame, (320, 80), (320, 400), (213, 169, 75), 13)
            cv2.putText(frame, "-|- 0 has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 3, cv2.LINE_AA)

        if win61:
            cv2.line(frame, (534, 80), (543, 400), (213, 169, 75), 13)
            cv2.putText(frame, "-|- 0 has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 3, cv2.LINE_AA)

        if win71:
            cv2.line(frame, (107, 80), (534, 400), (213, 169, 75), 13)
            cv2.putText(frame, "-|- 0 has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 3, cv2.LINE_AA)


        if win81:
            cv2.line(frame, (534, 80), (107, 400), (213, 169, 75), 13)
            cv2.putText(frame, "-|- 0 has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 3, cv2.LINE_AA)

        #cv2.putText(frame, "||- ' X ' has won the game!! -||", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
        #           (0, 223, 255), 3, cv2.LINE_AA)
    #############
        if win12:
            cv2.line(frame, (107, 80), (543, 80), (112, 62, 234), 13)
            cv2.putText(frame, "-|- X has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 2, cv2.LINE_AA)
        if win22:
            cv2.line(frame, (107, 240), (543, 240), (112, 62, 234), 13)
            cv2.putText(frame, "-|- X has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 3, cv2.LINE_AA)
        if win32:
            cv2.line(frame, (107, 400), (543, 400), (112, 62, 234), 13)
            cv2.putText(frame, "-|- X has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 3, cv2.LINE_AA)
        if win42:
            cv2.line(frame, (107, 80), (107, 400), (112, 62, 234), 13)
            cv2.putText(frame, "-|- X has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 3, cv2.LINE_AA)
        if win52:
            cv2.line(frame, (320, 80), (320, 400), (112, 62, 234), 13)
            cv2.putText(frame, "-|- X has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 3, cv2.LINE_AA)
        if win62:
            cv2.line(frame, (534, 80), (543, 400), (112, 62, 234), 13)
            cv2.putText(frame, "-|- X has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 3, cv2.LINE_AA)
        if win72:
            cv2.line(frame, (107, 80), (534, 400), (112, 62, 234), 13)
            cv2.putText(frame, "-|- X has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 3, cv2.LINE_AA)
        if win82:
            cv2.line(frame, (534, 80), (107, 400), (112, 62, 234), 13)
            cv2.putText(frame, "-|- X has won the game -|-", (70, 213 + 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 140, 255), 3, cv2.LINE_AA)

        cv2.putText(frame, "Close", (0, 15), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 1,
                    cv2.LINE_AA)

        if cv2.waitKey(1) & close == 1:
            close = 0
            break
        cv2.imshow('Tic Tac Toe', frame)



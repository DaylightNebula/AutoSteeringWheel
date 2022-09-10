# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
import os

track_high = (200, 200, 200)
track_low = (120, 120, 120)


def processFrame(frame, show):
    mask = cv2.inRange(frame, track_low, track_high)
    mask = cv2.erode(mask, None, iterations=5)
    mask = cv2.dilate(mask, None, iterations=2)
    displayFrames([frame, mask], show)


def displayFrames(frames, show):
    if show:
        counter = 0
        for frame in frames:
            counter += 1
            resizedFrame = cv2.resize(frame, (1280, 720))
            cv2.imshow("image_" + str(counter), resizedFrame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


# test code, loop through each image in assets\images and process it
for filename in os.listdir("assets\\images"):
    f = os.path.join("assets\\images", filename)
    # checking if it is a file
    if os.path.isfile(f):
        img = cv2.imread(f, cv2.IMREAD_COLOR)
        processFrame(img, True)

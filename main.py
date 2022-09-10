# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
import os


def processFrame(frame, show):
    displayFrames([img], show)


def displayFrames(frames, show):
    if show:
        for frame in frames:
            resizedFrame = cv2.resize(frame, (1280, 720))
            cv2.imshow("image", resizedFrame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


# test code
for filename in os.listdir("assets\\images"):
    f = os.path.join("assets\\images", filename)
    # checking if it is a file
    if os.path.isfile(f):
        img = cv2.imread(f, cv2.IMREAD_COLOR)
        processFrame(img, True)

from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np
from collections import deque

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    faces = face_cascade.detectMultiScale(frame_gray)
    palms = palm_cascade.detectMultiScale(frame_gray)
    mustache = cv.imread('images/mustache.png', -1)
    
    for (x,y,w,h) in faces:
        corner = (x, y)
        corner2 = (x + w, y + h)
        pts.append((x + w // 2, y + h // 2))
        frame = cv.rectangle(frame, corner, corner2, (0, 0, 255), 1)
    cv.imshow('Capture - Face detection', frame)

#-- 1. Load the cascades
face_cascade = cv.CascadeClassifier()
if not face_cascade.load(cv.samples.findFile('haarcascades/haarcascade_frontalface_alt.xml')):
    print('--(!)Error loading face cascade')
    exit(0)

palm_cascade = cv.CascadeClassifier()
if not palm_cascade.load(cv.samples.findFile('haarcascades/rpalm.xml')):
    print('--(!)Error loading smile cascade')
    exit(0)
camera_device = 1

pts = deque(maxlen=64)

#-- 2. Read the video stream
cap = cv.VideoCapture(0)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame)
    if cv.waitKey(10) == 27:
        break

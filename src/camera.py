import os
import cv2
from cv2 import VideoCapture, imshow, waitKey
import time
import random

cam = VideoCapture(0) # init camera, 0 is built-in cam

## function to get one frame
def get_frame():

    if not cam.isOpened():
        print("Error: Could not open camera")
        return None
    
    for i in range(3): # warm up the camera 
         cam.read()

    # read the current frame from the camera
    ret, frame = cam.read()

    #cam.release() 

    if ret:        
        print("Frame captured successfully")
        return frame
    else:
        print("Failed to capture frame from camera")
        return None
    
## function to countdown between frames
def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Capturing frame in {i} seconds...")
        time.sleep(1)

## function to capture the three frames
def capture_frames():

    # delete all previously saved jpg files in directory
    for filename in os.listdir("."): # for each file in current directory
        if filename.endswith(".jpg"):
            os.remove(filename)

    frames = []

    for i in range(3):
        countdown(5)
        frame = get_frame()
        
        if frame is not None:
            frames.append(frame)
            capture_name = f"capture_{i}.jpg" # generate a random name for the captured image
            cv2.imwrite(capture_name, frame) # save the captured frame as an image file
            
        else:
            print("Error: Could not capture frame")
    
    cam.release()
    return frames
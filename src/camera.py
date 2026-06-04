import cv2
from cv2 import VideoCapture

def get_frame():
    # initialize default camera
    cam = VideoCapture(0) # 0 is built-in cam

    if not cam.isOpened():
        print("Error: Could not open camera")
        return None
    
    for i in range(10):
         cam.read()

    # read the current frame from the camera
    ret, frame = cam.read()

    cam.release() 

    if ret:
        print("Frame captured successfully")
        return frame
    else:
        print("Failed to capture frame from camera")
        return None
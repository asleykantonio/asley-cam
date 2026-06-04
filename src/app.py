import camera, layout, printer
import cv2
from cv2 import imshow, waitKey

from flask import Flask
app = Flask(__name__)

@app.route("/")
def asley_cam():
    return "Hello, World!"

frame = camera.get_frame()
imshow("Camera Frame", frame)
cv2.waitKey(0)
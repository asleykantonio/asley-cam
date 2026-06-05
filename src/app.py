import os
from time import time
import re

import camera, layout, printer
import cv2
from cv2 import imshow, waitKey

from flask import Flask, render_template
app = Flask(__name__)

## index
@app.route("/")
def asley_cam():
    return render_template("index.html")

## ready to take pics page
@app.route("/capture", methods=["POST"])
def capture():
    return render_template("capture.html")

## used to display step by step photostrip
@app.route("/photostrip/<int:index>", methods=["POST"])
def photostrip(index):
    photo = layout.get_photostrip(index)
    return render_template("capture.html", photo=photo)

## take pics and display photostrip
@app.route("/take_pics", methods=["POST"])
def take_pics():
    # get the frames and store in array frames + frames_names
    frames = []
    frames = camera.capture_frames()

    # grab file names in order (0, 1, 2)
    frames_names = sorted(
        [f for f in os.listdir(".") if f.endswith(".jpg")],
        key=lambda f: int(re.search(r'\d+', f).group())
    )

    # format the photostrip
    strip = layout.strip_layout(frames_names)

    # display the photostrip
    strip.show()


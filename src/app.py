import os
from time import time
import re

import camera, layout, printer
import cv2
from cv2 import imshow, waitKey

from flask import Flask
app = Flask(__name__)

@app.route("/")
def asley_cam():
    return "Hello, World!"

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
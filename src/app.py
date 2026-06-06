import json
import os
from time import time
import re

import camera, layout, printer
from camera import cam
import cv2
from cv2 import imshow, waitKey

from flask import Flask, render_template, Response, send_file
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
@app.route("/photostrip")
def photostrip():
    return send_file("photostrip.jpg", mimetype="image/jpeg")

## used for rendering the photostrip
@app.route("/photo/<int:index>")
def get_photo(index):
    return send_file(f"photo_{index}.jpg", mimetype="image/jpeg")

## used for the live webcam feed
@app.route("/video_feed")
def video_feed():
    def generate():
        #cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cam.read()
            if not ret:
                break
            _, buffer = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

## take pics and display photostrip
@app.route("/stream")
def stream():
    def generate():
        # get the frames and store in array frames + frames_names
        frames = []
        frames = camera.capture_frames()

        # grab file names in order (0, 1, 2)
        frames_names = sorted(
            [f for f in os.listdir(".") if f.endswith(".jpg")],
            key=lambda f: int(re.search(r'\d+', f).group())
        )

        layout.strip_layout(frames_names) 

        yield f"data: {json.dumps({'url': '/photostrip'})}\n\n"

    return Response(generate(), mimetype="text/event-stream")


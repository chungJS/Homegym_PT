from flask import Flask, render_template, Response
from picamera import PiCamera
from io import BytesIO
import threading

app = Flask(__name__)
camera = PiCamera()
camera_lock = threading.Lock()

@app.route('/')
def index():
    return render_template('index.html')

def gen_frames():
    with camera_lock:
        stream = BytesIO()
        for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            stream.seek(0)
            frame = stream.read()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            stream.seek(0)
            stream.truncate()

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    camera.resolution = (640, 480)
    camera.framerate = 24
    app.run(host='0.0.0.0', port=5000)
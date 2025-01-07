from flask import Flask, render_template, Response, jsonify, request
import cv2
from ultralytics import YOLO, solutions
from datetime import datetime

app = Flask(__name__)

# Initialize YOLO model
model = YOLO("yolov8n-pose.pt")

# Initializing AIGym with default exercise type
gym_object = solutions.AIGym(
    line_thickness=2,
    view_img=True,
    pose_type="pushup",
    kpts_to_check=[6, 8, 10],
)

count = 0  # count 변수를 전역으로 이동
target_count = 0  # Target count set by the user
start_time = None  # Variable to track when counting started
cap = None  # Global video capture object

def change_pose_type(pose_type):
    global gym_object
    gym_object.pose_type = pose_type

def generate_frames():
    global count, target_count, cap
    frame_count = 0
    while True:
        try :
            success, im0 = cap.read()
            if not success:
                print("Video frame is empty or video processing has been successfully completed.")
                break
            frame_count += 1
            results = model.track(im0, verbose=False)  # Tracking recommended
            im0, count = gym_object.start_counting(im0, results, frame_count)
            ret, buffer = cv2.imencode('.jpg', im0)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            if count[0] >= target_count:
                break
        except Exception as e:
            print(f"Error: {e}. Continuing with the next frame...")
            continue


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    global cap, start_time
    cap = cv2.VideoCapture("http://192.168.0.102:5000/video_feed")
    if not cap.isOpened():
        return "Error opening video stream or file"
    start_time = datetime.now()  # Set the start time when video feed starts
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/set_target', methods=['POST'])
def set_target():
    global target_count, count, start_time
    target_count, count, start_time = 0, 0, None  # Reset count when a new target is set
    start_time = datetime.now()  # Reset start time
    exercise_type = request.form.get('exercise_type')
    change_pose_type(exercise_type)
    print(request.form.get('target_count'))
    target_count = int(request.form.get('target_count'))
    return jsonify(success=True)

@app.route('/refresh')
def get_count():
    elapsed_time = datetime.now() - start_time
    minutes, seconds = divmod(elapsed_time.total_seconds(), 60)
    time_str = '{:02}:{:02}'.format(int(minutes), int(seconds))
    return jsonify(count=count, time=time_str)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

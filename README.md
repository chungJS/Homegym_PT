# HOMEGYM PT

HOMEGYM PT is a program that helps users maintain proper posture and count repetitions during workouts using a Raspberry Pi camera.

Having a partner to ensure correct posture and count repetitions is [crucial](https://journals.lww.com/nsca-jscr/fulltext/2019/07000/presence_of_spotters_improves_bench_press.3.aspx) for motivation and effective workouts. HOMEGYM PT serves as this partner by using a Raspberry Pi camera to capture the user’s movements. With the help of a YOLO model, it evaluates the user’s posture and counts repetitions, improving workout efficiency for those exercising alone at home.

- [Diagram](#Diagram)
- [Features](#features)
- [Reference](#Reference)

## Diagram

![diagram](https://github.com/chungJS/HOMEGYM_PT/raw/main/img/diagram.png)

## Features

### Capture workout

Records the user’s workout and streams the video using the Raspberry Pi camera.

![picam](https://github.com/chungJS/HOMEGYM_PT/raw/main/img/picam.png)

### Recognition and Counting

Modifies the original YOLO’s ai_gym.py function to not only return image frames but also count repetitions after object recognition in each frame.

![edit](https://github.com/chungJS/HOMEGYM_PT/raw/main/img/edit.png)

### Result

Streams the video and displays repetition counts using Flask for real-time feedback.

![result](https://github.com/chungJS/HOMEGYM_PT/raw/main/img/result.png)

## Reference

[Sheridan, Andrew1; Marchant, David C.1; Williams, Emily L.2; Jones, Hollie S.3; Hewitt, Phil A.4; Sparks, Andy1. Presence of Spotters Improves Bench Press Performance: A Deception Study. Journal of Strength and Conditioning Research 33(7):p 1755-1761, July 2019. | DOI: 10.1519/JSC.0000000000002285](https://journals.lww.com/nsca-jscr/fulltext/2019/07000/presence_of_spotters_improves_bench_press.3.aspx)

[ultralytics documentation](https://docs.ultralytics.com/ko/tasks/pose/)

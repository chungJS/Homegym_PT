# HOMEGYM PT

HOMEGYM PT is a program that helps users maintain proper posture and count repetitions during workouts using a Raspberry Pi camera.

Having a partner to ensure correct posture and count repetitions is [crucial](https://journals.lww.com/nsca-jscr/fulltext/2019/07000/presence_of_spotters_improves_bench_press.3.aspx) for motivation and effective workouts. HOMEGYM PT serves as this partner by using a Raspberry Pi camera to capture the user’s movements. With the help of a YOLO model, it evaluates the user’s posture and counts repetitions, improving workout efficiency for those exercising alone at home.

<!-- vim-markdown-toc GFM -->

- [Diagram](#Diagram)
- [Features](#features)
- [Reference](#Reference)

<!-- vim-markdown-toc -->

## Diagram

![diagram](https://github.com/chungJS/HOMEGYM_PT/raw/main/img/diagram.png)

## Features

### Capture workout

Record User's workout and stream the video Using Pi Camera

![picam](https://github.com/chungJS/HOMEGYM_PT/raw/main/img/picam.png)

### Recognition and Counting

Original YOLO's ai_gym.py function only returns image frame.

Edit to Return not only the image but also the count after object recognition in each frame.

![edit](https://github.com/chungJS/HOMEGYM_PT/raw/main/img/edit.png)

### Result

Stream video and show counting using Flask

![ui](https://github.com/chungJS/HOMEGYM_PT/raw/main/img/ui.png)
![test](https://github.com/chungJS/HOMEGYM_PT/raw/main/img/test.png)

## Reference

[Sheridan, Andrew1; Marchant, David C.1; Williams, Emily L.2; Jones, Hollie S.3; Hewitt, Phil A.4; Sparks, Andy1. Presence of Spotters Improves Bench Press Performance: A Deception Study. Journal of Strength and Conditioning Research 33(7):p 1755-1761, July 2019. | DOI: 10.1519/JSC.0000000000002285](https://journals.lww.com/nsca-jscr/fulltext/2019/07000/presence_of_spotters_improves_bench_press.3.aspx)

[ultralytics documentation](https://docs.ultralytics.com/ko/tasks/pose/)

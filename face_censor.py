import cv2
import dlib
import time

video = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

flag = True

cap = cv2.VideoCapture("Blur.gif")
count = 0

pt = time.time()

while True:

    ret, image = cap.read()

    count += 1
    
    if ret and count<149: 
        pass
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        count = 0

    _,frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = detector(gray)

    for f in face:
        x1 = f.left()
        y1 = f.top()
        x2 = f.right()
        y2 = f.bottom()

        if flag:
            blurred = cv2.resize(image, (x2-x1,y2-y1))
            frame[y1:y2, x1:x2] = blurred

    ct = time.time()
    fps = int(1/(ct-pt))
    pt = ct
    cv2.putText(frame, "FPS: "+str(fps), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Video", frame)
    key = cv2.waitKey(1)

    # Press Esc to quit
    if key == 27:
        break
    
    # Press P to Switch off the censor
    if key == 112:
        flag = False

    # Press B to Switch on the censor
    if key == 98:
        flag = True
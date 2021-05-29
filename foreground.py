import numpy as np, cv2

cap = cv2.VideoCapture('src/video1.mp4')
fps = cap.get(cv2.CAP_PROP_FPS) 
delay = int(1000/fps)

fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, dsize=(640,480), interpolation=cv2.INTER_AREA)

    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('bgsub',fgmask)
    
    if cv2.waitKey(1) & 0xff == 27:
        break

cap.release()
cv2.destroyAllWindows()
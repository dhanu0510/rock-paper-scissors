import cv2
import sys
import os
try:
    label = sys.argv[1]
    sample_num = sys.argv[2]
except:
    print("Please pass Arguments.")
    print("for example if you want to collect 100 rock images then")
    print("python collect_image.py rock 100")
    print("types => rock paper scissors none")
    exit(-1)
sample_num = int(sample_num)
IMG_SAVE_PATH = 'images'
IMG_LABEL_PATH = os.path.join(IMG_SAVE_PATH,label)
try:
    os.mkdir(IMG_SAVE_PATH)
except:
    pass
try:
    os.mkdir(IMG_LABEL_PATH)
except:
    pass


cap = cv2.VideoCapture(0)
start = False
count = 0


while True:
    _, frame = cap.read()
    if not _:
        continue
    if count == sample_num:
        break
    frame = cv2.flip(frame, 1)
    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)

    if start:
        fig = frame[100:500,100:500]
        path = os.path.join(IMG_LABEL_PATH,f'{count+1}.jpg') 
        cv2.imwrite(path, fig)
        count += 1

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f"Collecting {count}",(5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.namedWindow("Press A for start collectin Images and Q for quit", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Press A for start collectin Images and Q for quit",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Press A for start collectin Images and Q for quit",frame)
    wait = cv2.waitKey(10)
    if wait == ord('a'):
        start = True
    if wait == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()        
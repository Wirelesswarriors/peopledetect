import cv2

cars_cascade = cv2.CascadeClassifier("C:\Users\1921875\OneDrive - Dundee and Angus College\Documents\Python\iot\haarcascade_fullbody.xml")
def detect_pedestrian(frame):
    from espeak import espeak
    import time
    cars = cars_cascade.detectMultiScale(frame, 1.15, 4)
    for (x, y, w, h) in pedestrian:
        cv2.rectangle(frame, (x, y), (x+w, y+h), color=(0, 255, 255), thickness=2)
        time.sleep(1)
    
    return frame

def main():
    import time
    import numpy as np
    from picamera2 import Picamera2

    cam = Picamera2()
    height = 480
    width = 640
    middle = (int(width / 2), int(height / 2))
    cam.configure(cam.create_video_configuration(main={"format": "RGB888", "size": (width, height)}))
    cam.start()
    while True:
        frame = cam.capture_array()
        controlkey = cv2.waitKey(1)
        if ret:
            oframe = detect_pedestrian(frame)
            cv2.imshow("frame", oframe)
        else:
            break
        if controlkey == ord("q"):
            break
    oframe.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
 
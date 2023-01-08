from pickle import TRUE
import cv2
import numpy as np
import face_recognition
import os
import time
import datetime
from pushbullet import PushBullet

cap = cv2.VideoCapture(0)

API_KEY = "o.ASdCcRfpsLEabwyPowDFQvfGYFu0kQEY"

pb = PushBullet(API_KEY)

detect = 0

path = 'faces'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

# Opencv DNN
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
# net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)


# Load class lists
classes = []
with open("dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)
print(classes)

detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)
print('Encoding Complete')

# used to record the time when we processed last frame
prev_frame_time = 0
 
# used to record the time at which we processed current frame
new_frame_time = 0

while True:
    ret, frame = cap.read()

    # time when we finish processing for this frame
    new_frame_time = time.time()
 
    # Calculating the fps

    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
 
    # converting the fps into integer
    fps = int(fps)
 
    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps = str(fps)
 
    # putting the FPS count on the frame
    cv2.putText(frame, fps, (7, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 0), 2, cv2.LINE_AA)
    
    class_id = None
    
    (class_ids, scores, bboxes) = model.detect(frame, confThreshold=0.3, nmsThreshold=.4)
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        class_name = classes[class_id]
    #if human is detected then draw a bounding box
    if class_id == 0:
        cv2.putText(frame, class_name.upper(), (x, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 1)
        cv2.putText(frame,str(round(score*100,2))+'%',(x + 100, y - 10),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0), 2)
        print(class_name)
        class_id = 1
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%b-%m-%Y-%H-%M-%S")
            detect_time = datetime.datetime.now().strftime("%I:%M %p")
            rec = cv2.VideoWriter(
                f"{current_time}.mp4", fourcc, 20, frame_size)
            print("Started Recording!")
            #push = pb.push_note(f" ALERT on {detect_time}",class_name.upper() + " DETECTED")
            # #send notification
            # with open("snapshot-{detect_time}.jpg", "rb") as pic:
            #     file_data = pb.upload_file(pic, "snapshot-{detect_time}.jpg")
            #     push = pb.push_file(**file_data)
        #---------------------end of human detection --------------------
            
    #Records and save video into mp4 file when there is a detection               
    elif detection:
        print(class_id)
        print(score)
        print(detection)
        if timer_started:
            print(time.time(),detection_stopped_time, SECONDS_TO_RECORD_AFTER_DETECTION)
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                rec.release()
                print('Stop Recording!')
                #Send video to user
                # with open(f"{current_time}.mp4", "rb") as vid:
                #     file_data = pb.upload_file(vid, f"{current_time}.mp4")

                # push = pb.push_file(**file_data)
        
        else:
            timer_started = True
            detection_stopped_time = time.time()
    if detection:
        rec.write(frame)
    #------------------end of recording----------------------------------------

    #Face detection(for testing only. remove if not needed)--------------------------------
    imgS = cv2.resize(frame,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)
    
        if faceDis[matchIndex]< 0.50:
            detect_time = datetime.datetime.now().strftime("%I:%M%p")
            name = classNames[matchIndex].upper()
            #Take snapshot
            push = pb.push_note("Familar face detected",name.upper() + " IS ON CAMERA")
            img_name = f"{name.upper()} IS DETECTED.jpg"
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            with open(f"{name.upper()} IS DETECTED.jpg", "rb") as pic:
                file_data = pb.upload_file(pic, "KNOWN-{detect_time}.jpg")
                push = pb.push_file(**file_data)
        else: 
            name = 'Unknown'
            #print(name)
        y1,x2,y2,x1 = faceLoc
        y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
        cv2.putText(frame,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    #-------End of face detection --------------------------------

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

rec.release()
cap.release()
cv2.destroyAllWindows()
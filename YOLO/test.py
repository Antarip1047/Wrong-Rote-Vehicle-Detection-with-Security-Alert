import cv2
import pandas as pd
from ultralytics import YOLO
from tracker import*
import cvzone
import numpy as np
model=YOLO('yolov8s.pt')



def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap=cv2.VideoCapture('8.mp4')


my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n") 
#print(class_list)

count=0
tracker=Tracker()
#area1=[(320,240),(700,240),(700,245),(320,245)]
#area2=[(400,197),(642,197),(642,202),(400,202)]

area1=[(120,410),(1000,410),(1000,415),(120,415)]
area2=[(200,400),(1000,400),(1000,405),(200,405)]



wup={}
wrongway=[]
while True:    
    ret,frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 2 != 0:
        continue
    frame=cv2.resize(frame,(1020,500))
   

    results=model.predict(frame)
 #   print(results)
    a=results[0].boxes.data
    px=pd.DataFrame(a).astype("float")
#    print(px)
    list=[]
             
    for index,row in px.iterrows():
#        print(row)
 
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]
        if 'car' or 'motorcycle' or 'bus' or 'train' or 'truck' or 'ricksaw' or 'bike' in c:
           list.append([x1,y1,x2,y2])
    bbox_idx=tracker.update(list)
    for bbox in bbox_idx:
        x3,y3,x4,y4,id=bbox
        cx=x3
        cy=y4
        cv2.circle(frame,(cx,cy),2,(255,0,0),-1)
        cv2.rectangle(frame,(x3,y3),(x4,y4),(255,0,255),2)
        cvzone.putTextRect(frame,f'{id}',(x3,y3),1,1)
        result=cv2.pointPolygonTest(np.array(area1,np.int32),((cx,cy)),False)
        if result>=0:
            wup[id]=(cx,cy)
        if id in wup:
            result1=cv2.pointPolygonTest(np.array(area2,np.int32),((cx,cy)),False)
            if result1>=0:
                cv2.circle(frame,(cx+10,cy-10),10,(0,0,255),-1)
                cv2.rectangle(frame,(x3,y3),(x4,y4),(0,0,255),2)
                cvzone.putTextRect(frame,f'{id}',(x3,y3),1,1)
                if wrongway.count(id)==0:
                    wrongway.append(id)
        
    w=len(wrongway)         
    cv2.polylines(frame,[np.array(area1,np.int32)],True,(255,255,255),2)
    cv2.polylines(frame,[np.array(area2,np.int32)],True,(255,255,255),2)
    cvzone.putTextRect(frame,f'WRONGWAY:-{w}',(60,100),2,2)
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()

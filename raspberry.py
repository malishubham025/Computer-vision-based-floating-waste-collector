from smbus import SMBus

addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1

import cv2

cap=cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_PLAIN

# file=cv2.CascadeClassifier("C:\\Users\\malis\\Downloads\\face.xml")
file=cv2.CascadeClassifier("//home//pi//Desktop//test_codes//cascade.xml")
A=0
B=0
x=0
while (cap.isOpened()):
    ret,frame=cap.read()
    # frame=cv2.resize(frame,(600,400))
    frame=cv2.flip(frame,1)
    face=file.detectMultiScale(frame,1.1,10)
    for (x,y,h,w) in face:
        A=x
        B=y
        cv2.rectangle(img=frame,pt1=(A,B),pt2=(x+h,y+w),color=(1,255,255),thickness=2)
        x=int(((-0.1*w)+38)*2.54)
        if(x<40):
            #print("low")
            bus.write_byte(addr, 0x1)
        else :
            bus.write_byte(addr, 0x0)
            
    cv2.putText(img=frame,text=str(x)+"cm",org=(A,B),fontFace=font,fontScale=2,color=(0,255,255),thickness=2) 
    cv2.imshow("img",frame)
    if cv2.waitKey(1) & 0xFF==27:
        #print(A,h)
        break
cv2.destroyAllWindows()
cap.release()
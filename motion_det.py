import cv2

def find_diff(t0,t1,t2):
    

    fr0=cv2.absdiff(t0,t1)
    fr1=cv2.absdiff(t1,t2)
    fr2=cv2.bitwise_and(fr0,fr1)
    return fr2

cap=cv2.VideoCapture(0)
frame0=cap.read()[1]
frame1=cap.read()[1]
frame2=cap.read()[1]
frame0=cv2.cvtColor(frame0,cv2.COLOR_BGR2GRAY)
frame1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
frame2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

while True:
    image=find_diff(frame0,frame1,frame2)
    
    cv2.imshow("Detector",image)     
    ret,img=cap.read()
    frame0=frame1
    frame1=frame2
    frame2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
cv2.destroyAllWindows()

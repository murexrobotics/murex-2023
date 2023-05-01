import cv2 as cv
import numpy as np
import math

pic = None
frame = None
dot = (0,0)
screenshot = None
new_sc = False

def position(event,a,b,flag,param):
    if event == cv.EVENT_LBUTTONDOWN:
        global dot, screenshot, new_sc
        dot = (a,b)
        print(dot)
        if 0.65*x<a and a<x and 0.85*y<b and b<y:
            screenshot = frame
            new_sc = True
            print("screenshot taken")

def nothing(x):
    pass

vid = cv.VideoCapture("udp://192.168.1.1:1234")
vid.set(cv.CAP_PROP_FPS, 30)

cv.namedWindow('interface')
cv.setMouseCallback('interface',position)
cv.createTrackbar('Screenshot','interface',0,3,nothing)

#Initial reading
ret,frame = vid.read()
frame = cv.resize(frame, (800,500))
y = frame.shape[0]
x = frame.shape[1]
#overlay = np.full((y, x, 3), 200, dtype = np.uint8)
sc=[np.zeros([y, x, 3], dtype = np.uint8),
    np.zeros([y, x, 3], dtype = np.uint8),
    np.zeros([y, x, 3], dtype = np.uint8),
    np.zeros([y, x, 3], dtype = np.uint8)]
sc[1][:, :] = [0,0,255]
sc[2][:, :] = [0,255,0]
sc[3][:, :] = [255,0,0]

while(True):
    ret, frame = vid.read()
    if ret:
        #cv2.imshow('Frame', frame)
        #out.write(frame)
        img_str = cv.imencode('.jpg', frame)[1].tobytes()
        #print(img_str)
        if cv.waitKey(25) & 0xFF == ord('q'):
           break
    else:
        break
    image = np.asarray(bytearray(img_str), dtype="uint8")
    image = cv.imdecode(image, cv.IMREAD_COLOR)
    image = cv.resize(image, (800,500))
    
    s = cv.getTrackbarPos('Screenshot','interface')

    if s>0:
        if new_sc == True:
            sc[s] = screenshot
            new_sc = False
        #else:
            #sc[s] = cv.addWeighted(sc[s],0.4,overlay,0.1,0)

    #Combining screenshot interfaces
    comb1 = np.hstack((frame, sc[1]))
    comb2 = np.hstack((sc[2], sc[3]))
    comb3 = np.vstack((comb1, comb2))
    cv.putText(comb3, "Screenshot", (int(0.7*x),int(0.9*y)), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3, cv.LINE_AA)
    cv.imshow('interface',comb3)
    #Quit Program
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
  
vid.release()
cv.destroyAllWindows()
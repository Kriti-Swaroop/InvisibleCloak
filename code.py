import cv2
import numpy as np
vdo=cv2.VideoCapture(0) #0 signifies that the video will be captured directly from the camera
for i in range(60):
    ret,bg=vdo.read()
    if ret==0:
        continue
while(vdo.isOpened()):
    ret,img=vdo.read()  #ret returns true if vdo reads something
    if ret==0:
        break
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #SEPARATING COLOUR RED
    #hue=0 to 60 and 340 to 360 for red colour
    #since max value for hsv in opencv in 255,we halve these values
    l=np.array([0,110,70]) 
    u=np.array([10,255,255]) 
    m1=cv2.inRange(hsv,l,u)
    l=np.array([170,110,70])
    u=np.array([180,255,255])
    m2=cv2.inRange(hsv,l,u)
    m1+=m2
	#noise removal
    m1 = cv2.morphologyEx(m1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2) 
    m1 = cv2.dilate(m1, np.ones((3, 3), np.uint8), iterations = 1) 
    
    red=cv2.bitwise_and(bg,bg,mask=m1)   #replacing red with the background
    m2=cv2.bitwise_not(m1)   #everything except red w/o background
    notred=cv2.bitwise_and(img,img,mask=m2)   #everything except red with background
    cv2.imshow("cloak",cv2.addWeighted(red,1,notred,1,0))  
    if cv2.waitKey(10)==ord('q'):
        break
vdo.release()
cv2.destroyAllWindows()
import numpy as np
import cv2
import time
import pafy

min_color_values = np.array([0, 150, 150], dtype=np.uint8)
max_color_values = np.array([45, 200, 255], dtype=np.uint8) 

# odkomentować w celu testów pliku wideo na dysku
#video = cv2.VideoCapture("../flame2.mp4")
# odkomentować w celu testów z kamerki w laptopie
#video = cv2.VideoCapture(0)
# https://www.youtube.com/watch?v=5hghT1W33cY
url = "https://www.youtube.com/watch?v=5hghT1W33cY"

videoPafy = pafy.new(url)
best = videoPafy.getbest(preftype="mp4")
video = cv2.VideoCapture(best.url)
# video = cv2.VideoCapture(0)
print('Press q to quit')

i=0
while True:  
    grabbed, image_frame = video.read()  
    # cv2.imshow('Og', image_frame) 
    hsv = cv2.cvtColor(image_frame, cv2.COLOR_BGR2HSV)  
    mask = cv2.inRange(hsv, min_color_values, max_color_values) 
    (contours,hierachy)=cv2.findContours(mask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # (image2, countours, hierarchy) = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  

    for contour_field in contours:  
        if cv2.contourArea(contour_field) < 1000:  
            continue  

        (x, y, w, h) = cv2.boundingRect(contour_field)  
        cv2.rectangle(image_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  

        rect = cv2.minAreaRect(contour_field)  
        box = np.int0(cv2.boxPoints(rect))  
        box = np.int0(box)  
        cv2.drawContours(image_frame, [box], 0, (0, 191, 255), 2)  
        cv2.imshow('Color', image_frame) 
        i += 1
        #time.sleep(0.05)
    if cv2.waitKey(1) & 0xFF == ord('q'): break  
video.release()  
cv2.destroyAllWindows() 
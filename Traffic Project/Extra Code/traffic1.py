import cv2
import numpy as np
from time import sleep
import traffic2 as t2

def Vehicle():
    width=80 
    height=80 
    
    offset=6  
    
    line=500 
    
    delay= 60 #FPS do vídeo
    
    detec = []
    count= 0
    
    	
    def handle_centre(x, y, w, h):
        x1 = int(w / 2)
        y1 = int(h / 2)
        cx = x + x1
        cy = y + y1
        return cx,cy
    
    
    cap = cv2.VideoCapture('video1.mp4')
    subtracao = cv2.createBackgroundSubtractorMOG2(	history = 5,varThreshold = 25,detectShadows = True )
    
    while True:
        ret , frame1 = cap.read()
        tempo = float(1/delay)
        sleep(tempo)
        grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(grey,(3,3),5)
        img_sub = subtracao.apply(blur)
        dilat = cv2.dilate(img_sub,np.ones((5,5)))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
        dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
            
        img,contorno,h = cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.line(frame1, (30, line), (650, line), (255,127,0), 3) 
        cv2.line(frame1, (30, line), (650, line), (255,127,0), 3) 
        for(i,c) in enumerate(contorno):
            (x,y,w,h) = cv2.boundingRect(c)
            validar_contorno = (w >= width) and (h >= height)
            if not validar_contorno:
                  continue
        
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)        
        centro = handle_centre(x, y, w, h)
        detec.append(centro)
        cv2.circle(frame1, centro, 4, (0, 0,255), -1)
        
        for (x,y) in detec:
            if y<(line+offset) and y>(line-offset):
                count+=1
                cv2.line(frame1, (25, line), (550, line), (0,127,255), 3)  
                detec.remove((x,y))
                print("cars detected a moment: "+str(count))                    
                if count == 10:
                    t2.Vehicle()
                     
            cv2.putText(frame1, "Vehicle: "+str(count), (300, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
            cv2.putText(frame1, "Road_no-1 ",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),4)
            cv2.imshow("Video Original" , frame1)
            cv2.imshow("Detectar",dilatada)

    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    
        
    cv2.destroyAllWindows()
    cap.release()
Vehicle()

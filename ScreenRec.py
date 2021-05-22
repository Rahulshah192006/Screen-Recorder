import cv2
import numpy as np
from PIL import ImageGrab


def screenRecorder():

    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    fps = 50


    out = cv2.VideoWriter('output.mp4', fourcc, fps, (1920,1080))

    while(True):

        
        img = ImageGrab.grab()

      
        img_np = np.array(img)


        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

       
        win_title = "Screen Recorder Made By Rahul"
        cv2.imshow(win_title, frame)

        out.write(frame)

        
        if(cv2.waitKey(1) & 0XFF == ord('q')):
            break

 
    out.release()

    cv2.destroyAllWindows()



screenRecorder()
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Definimos el codec con el que vamos a grabar y el objeto.
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('cursoPython.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
    	#Captura inversa
        #frame = cv2.flip(frame,0)
        # write the flipped frame
        out.write(frame)
        cv2.imshow('cursoPythonSemestral',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
#Cerramos la ventana
cv2.destroyAllWindows()
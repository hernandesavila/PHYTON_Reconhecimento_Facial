import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Não foi possível abrir a câmera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Não foi possível ler o quadro da câmera")
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    negative = cv2.bitwise_not(gray)

    cv2.imshow("Câmera", negative)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
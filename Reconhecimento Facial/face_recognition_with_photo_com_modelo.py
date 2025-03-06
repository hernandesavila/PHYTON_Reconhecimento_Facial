import os
import cv2
import numpy as np
from PIL import Image

# Carrega o classificador de faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

nomes = {
    1: "Pessoa 1",
    2: "Pessoa 2",
    3: "Pessoa 3"
}

faces = []
labels = []

caminho_pasta = "./imagens"

# Carrega a imagem de referência
for arquivo in os.listdir(caminho_pasta):
    if any(ext in arquivo.lower() for ext in [".jpg", ".jpeg", ".png"]):
        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
        #img = cv2.imread(os.path.join(caminho_pasta, arquivo))
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faceImg = Image.open(os.path.join(caminho_pasta, arquivo)).convert('L')
        faceNp= np.array(faceImg,'uint8')
        faces.append(faceNp)
        labels.append(int(nome_arquivo))

# Cria o objeto de reconhecimento facial com o algoritmo Eigenfaces
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array([labels]))

# Inicializa a câmera
cap = cv2.VideoCapture(0)

while True:
    # Lê a imagem da câmera
    ret, img = cap.read()
    
    test_image =  Image.fromarray(img)
    img = np.array(test_image.convert('RGB'))
    
    # Converte a imagem para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecta faces na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Para cada rosto encontrado, tenta reconhecê-lo usando a imagem de referência
    for (x, y, w, h) in faces:
        try:
            label, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            #print(f"ID reconhecido: {label}")
            #print(f"Confiança: {confidence}")

            # Se a imagem for reconhecida, desenha um retângulo verde ao redor do rosto
            if confidence < 53:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
                cv2.putText(img, nomes.get(label, "Desconhecido"), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)
                cv2.putText(img, format(confidence, ".2f"), (x+w-50, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
            else:
                # Se a imagem não for reconhecida, desenha um retângulo vermelho ao redor do rosto
                cv2.putText(img, "Desconhecido", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 1)

        except Exception as erro:
            print("Ocorreu um erro:", erro)

    # Exibe a imagem na tela
    cv2.imshow('Reconhecimento facial em tempo real', img)

    # Verifica se a tecla 'q' foi pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha a janela
cap.release()
cv2.destroyAllWindows()
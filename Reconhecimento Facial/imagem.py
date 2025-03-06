import cv2

# cria um objeto para capturar vídeo da câmera
cap = cv2.VideoCapture(0)

# verifica se o objeto de captura de vídeo foi inicializado corretamente
if not cap.isOpened():
    print("Não foi possível abrir a câmera")
    exit()

# loop principal do programa
while True:
    # lê um quadro da câmera
    ret, frame = cap.read()

    # verifica se o quadro foi lido corretamente
    if not ret:
        print("Não foi possível ler o quadro da câmera")
        break

    # exibe o quadro na tela
    cv2.imshow("Câmera", frame)

    # aguarda 1 milissegundo para o usuário pressionar a tecla 'q' para sair
    if cv2.waitKey(1) == ord('q'):
        break

# libera o objeto de captura de vídeo e fecha a janela de exibição
cap.release()
cv2.destroyAllWindows()
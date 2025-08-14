import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Lemos um único quadro apenas para inspecioná-lo
    ret, frame = cap.read()

    if ret and frame is not None:
        print("Sucesso! O OpenCV leu um quadro da câmera.")
        # --- ESSA É A LINHA DO DETETIVE ---
        print("As dimensões do quadro são:", frame.shape)
        # ------------------------------------

        # Agora iniciamos o loop para exibir
        while True:
            # Reutilizamos o primeiro frame e depois lemos os próximos
            cv2.imshow('Teste da Webcam', frame)

            if cv2.waitKey(1) == 27: # ESC para sair
                break
            
            # Lê o próximo frame para a próxima iteração
            ret, frame = cap.read()
            if not ret:
                print("Perda de sinal da câmera.")
                break
    else:
        print("ERRO: A câmera abriu, mas falhou em enviar o primeiro quadro.")

else:
    print("ERRO: Câmera não pôde ser aberta.")

print("Encerrando o programa.")
cap.release()
cv2.destroyAllWindows()
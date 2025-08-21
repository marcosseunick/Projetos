import cv2
import mediapipe as mp

def main():
    # Inicializa a webcam com backend DSHOW (específico para Windows)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    if not cap.isOpened():
        print("Erro: Não foi possível abrir a câmera!")
        return
    
    # Configurações do MediaPipe
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils
    
    # Configurações da janela
    cv2.namedWindow('Detecção Facial', cv2.WINDOW_NORMAL)
    
    try:
        with mp_face_detection.FaceDetection(
            min_detection_confidence=0.5
        ) as face_detection:
            
            while True:
                # Captura do frame
                ret, frame = cap.read()
                
                if not ret:
                    print("Erro: Frame não capturado corretamente")
                    break
                
                # Conversão de cores e detecção
                image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = face_detection.process(image_rgb)
                
                # Desenho das detecções
                if results.detections:
                    for detection in results.detections:
                        mp_drawing.draw_detection(frame, detection)
                
                # Exibição do frame
                cv2.imshow('Detecção Facial', frame)
                
                # Verificação de fechamento da janela
                if cv2.getWindowProperty('Detecção Facial', cv2.WND_PROP_VISIBLE) < 1:
                    break
                
                # Saída com ESC
                if cv2.waitKey(1) & 0xFF == 27:
                    break
    
    except Exception as e:
        print(f"Erro durante a execução: {str(e)}")
    
    finally:
        # Liberação de recursos
        cap.release()
        cv2.destroyAllWindows()
        # Garante que todas as janelas são fechadas
        for i in range(5):
            cv2.waitKey(1)

if __name__ == "__main__":
    main()
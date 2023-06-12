import cv2
import numpy as np
import tensorflow as tf

# Cargar el modelo entrenado
model = tf.keras.models.load_model('/home/rishard/Documents/IAproyect/model/')

# Función de preprocesamiento de imágenes
def preprocess_image(image):
    # Preprocesamiento específico del modelo (redimensionar, normalizar, etc.)
    preprocessed_image = ...  # Aplica las transformaciones necesarias a la imagen
    return preprocessed_image

# Función para aplicar el modelo a una imagen
def apply_model(image):
    preprocessed_image = preprocess_image(image)
    predictions = model.predict(np.expand_dims(preprocessed_image, axis=0))
    # Realiza el procesamiento posterior de las predicciones si es necesario
    return predictions

# Cargar el video
video_path = 'aeropuerto.mp4'
video = cv2.VideoCapture(video_path)

# Obtener el tamaño del video y definir el codec y el objeto VideoWriter para el video de salida
frame_width = int(video.get(3))
frame_height = int(video.get(4))
output_video = cv2.VideoWriter('salida.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

# Procesar cada fotograma del video
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    # Aplicar el modelo al fotograma actual
    predictions = apply_model(frame)

    # Realizar acciones según las predicciones obtenidas
    # Por ejemplo, dibujar cuadros delimitadores alrededor de objetos detectados

    # Mostrar el video resultante con las predicciones superpuestas
    cv2.imshow('Video', frame)
    output_video.write(frame)

    # Presiona 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos utilizados
video.release()
output_video.release()
cv2.destroyAllWindows()
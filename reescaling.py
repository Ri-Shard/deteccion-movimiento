from PIL import Image
import os

def resize_images(input_folder, output_folder, size):
    # Verificar si la carpeta de salida existe, de lo contrario, crearla
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Obtener una lista de todas las imágenes en la carpeta de entrada
    image_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg') or f.endswith('.png')]

    # Iterar sobre cada imagen y reescalarla
    for image_file in image_files:
        # Abrir la imagen
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)

        # Reescalar la imagen a 300x300 píxeles
        resized_image = image.resize(size)

        # Guardar la imagen reescalada en la carpeta de salida
        output_path = os.path.join(output_folder, image_file)
        resized_image.save(output_path)

        # Cerrar la imagen
        image.close()

    print('¡Reescalado completado!')

# Ruta de la carpeta de entrada
input_folder = '/home/rishard/Documents/0'

# Ruta de la carpeta de salida
output_folder = '/home/rishard/Documents/background'

# Tamaño deseado para las imágenes reescaladas
size = (300, 300)

# Llamar a la función para reescalar las imágenes
resize_images(input_folder, output_folder, size)
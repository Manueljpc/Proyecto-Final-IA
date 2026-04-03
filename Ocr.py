import easyocr
import numpy as np
from PIL import Image

#para cargar la imagen
image = Image.open("prueba_ocr/prueba_ocr.png")

#para convertir en array
image_np = np.array(image)


#cargar modelo
reader = easyocr.Reader(['es', 'en'], gpu= False)

#detectar texto
result = reader.readtext(image_np)

#mostrar texto

text = " ".join([r[1] for r in result])
print("texto detectado")
print(text)
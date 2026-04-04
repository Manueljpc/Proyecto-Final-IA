import pytesseract
import cv2
from PIL import Image


try: 
    
    #para cargar la imagen
    image = cv2.imread("prueba_ocr/prueba_ocr1.png")
    
    if image is None:
        raise Exception("no se pudo cargar la imagen")
    
    
    #para convertir a gris 
    gray = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
    
    

    #mejora el ocr
    
    _, thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
    
    image_pil = Image.fromarray(thresh)
    

    #cargar modelo
    text = pytesseract.image_to_string(thresh, lang = 'spa', config='--psm 6')

    #mostrar texto

    print("texto detectado:")
    print(text)

except Exception as e:
    print("error",e)
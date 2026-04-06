import pytesseract
import cv2
from PIL import Image

def extraer_texto(ruta_imagen):
    try: 
        #para cargar la imagen
        image = cv2.imread(ruta_imagen)
    
        if image is None:
            raise Exception("no se pudo cargar la imagen")
    
        #para convertir a gris 
        gray = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
        #mejora el ocr separando las letras del fondo
        _, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
        image_pil = Image.fromarray(thresh)
    
        #cargar modelo
        text = pytesseract.image_to_string(image_pil, lang = 'spa', config='--psm 6')
        return text
        

       
    except Exception as e:
        return f"Error OCR : {e}"
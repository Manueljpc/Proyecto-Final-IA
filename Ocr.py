import pytesseract
from PIL import Image


try: 
    
    #para cargar la imagen
    image = Image.open("prueba_ocr/prueba_ocr.png")


    #cargar modelo
    text = pytesseract.image_to_string(image, lang = 'spa')

    #mostrar texto

    print("texto detectado:")
    print(text)

except Exception as e:
    print("error",e)
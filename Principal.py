from Ocr import extraer_texto
from Resumen import resumir_texto

try :
    ruta = "prueba_ocr/prueba_ocr1.png"
    
    #OCR
    texto = extraer_texto(ruta)
    
    print("texto detectado: \n")
    print(texto)
    
    #resumidor
    
    resumen = resumir_texto(texto)
    print("\n resumen:\n")
    print (resumen)
    
except Exception as e:
    print("Error:",e)    
import gradio as gr
from Ocr import extraer_texto
from Resumen import resumir_texto

def procesar_imagenes(imagen_ruta):
    
    if imagen_ruta is None:
        return "Error: no se ha subido ninguna imagen"
    
    #aqui se llama al Ocr
    print("iniciando extraccion del texto")
    texto_extraido = extraer_texto(imagen_ruta)
    
    # aqui se verifica si el Ocr dio algun error
    if "Error Ocr" in texto_extraido or not texto_extraido.strip():
        return texto_extraido, "no se pudo generar un resumen debido a errores en el texto."
    
    #para llamar al sesumidor
    print("generando resumen")
    resultado_resumen = resumir_texto(texto_extraido)
    return texto_extraido , resultado_resumen
    
    

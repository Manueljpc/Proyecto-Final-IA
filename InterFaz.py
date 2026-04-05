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
    
    
# interfaz grafica

with gr.Blocks(titulo = "SmartNote AI") as interfaz:
    gr.Markdown("sube una foto o imagen de tus apuntes para resumirlos")
    
    #entrada de imagen
with gr.Row.Column():
    subir_imagen = gr.Image(type="filepath", label="foto de tus apuntes")
    boton_ejecutar = gr.Button("procesar imagenes", variant="primary")    
    #SALIDA DE texto
with gr.Column():
    salida_texto = gr.Textbox(label = "texto identificado", lines=8)
    salida_resumen = gr.Textbox(label="resumen", lines=5)
    
    # accion al hacer click al boton   
    boton_ejecutar.click(
        fn=procesar_imagenes,
        inputs=subir_imagen,
        outputs=[salida_texto,salida_resumen]
    )
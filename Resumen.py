from transformers import pipeline
import gc

#para cargar el modelo
resumidor = pipeline("summarization", model = "t5-small")

def resumir_texto(texto):
    if not texto or len(texto.strip()) < 30:
        return "el texto es demasiado corto"
    
    
    try:
        #para que el modelo entienda lo que tiene que hacer
        entrada_texto = "summarize:" + texto
        
    #para generar el resumen
        resumen = resumidor(
        
        entrada_texto,
        max_length = 150,
        min_length = 40,
        do_sample = False,    
        )
    
        gc.collect()
        
        
        return resumen[0]['summary_text']
    
    except Exception as e:
        return f"error al resumir:{e}"
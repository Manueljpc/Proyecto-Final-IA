from transformers import pipeline

#para cargar el modelo
resumidor = pipeline("summarization", model = "t5-small")

def resumir_texto(texto):
    try:
    
        resumen = resumidor(
        
        texto,
        max_length = 100,
        min_length = 30,
        do_sample = False
        
        )
    
        return resumen[0]['summary_text']
    
    except exception as e:
        return f"error al resumir:{e}"
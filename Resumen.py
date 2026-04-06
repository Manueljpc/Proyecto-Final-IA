from transformers import pipeline

#para cargar el modelo
resumidor = pipeline("summarization", model = "google/mt5-small")

def resumir_texto(texto):
    if not texto or len(texto) < 50:
        return "el texto es demasiado corto"
    
    
    try:
        
        entrada_texto = "summarize:" + texto
        
    #para generar el resumen
        resumen = resumidor(
        
        entrada_texto,
        max_length = 300,
        min_length = 80,
        do_sample = True,
        top_k = 50,
        top_p = 0.90, 
        punctuation_penalty = 1.0,
    
        
        )
    
        return resumen[0]['summary_text']
    
    except Exception as e:
        return f"error al resumir:{e}"
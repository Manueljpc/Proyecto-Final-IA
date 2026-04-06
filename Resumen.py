from transformers import pipeline

#para cargar el modelo
resumidor = pipeline("summarization", model = "google/mt5-small")

def resumir_texto(texto):
    
    
    
    try:
        
        entrada_texto = "summarize:" + texto
        
    #para generar el resumen
        resumen = resumidor(
        
        entrada_texto,
        max_length = 250,
        min_length = 80,
        do_sample = False,
        num_beams = 4, # permie que la ia piense en varias opciones antes de escribir
        length_penalty = 2.0, # con un valor mayor a 1.0 hace que la ia escriba frases mas largas
        early_stopping = True # para cuando la frase tiene sentido
        
        )
    
        return resumen[0]['summary_text']
    
    except Exception as e:
        return f"error al resumir:{e}"
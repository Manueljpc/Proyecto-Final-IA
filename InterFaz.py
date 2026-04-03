import gradio as gr

def saludar(nombre):
    return f"Hola {nombre}, Gradio está funcionando correctamente "

app = gr.Interface(
    fn=saludar,
    inputs="text",
    outputs="text",
    title="Prueba de Gradio"
)

app.launch()
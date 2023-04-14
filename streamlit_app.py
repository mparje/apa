import openai
import streamlit as st
from docx import Document
import os

# Establecer la clave API de GPT-4 desde la variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")


# Definir el modelo de OpenAI
model_engine = "text-davinci-003"

# Función para generar texto con OpenAI
def generate_text(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message

# Definir la aplicación de streamlit
def app():
    st.title("Editor de Referencias Bibliográficas")

    # Obtener la entrada del usuario
    option = st.selectbox("Seleccione una opción", ["Pegar el texto", "Subir archivo .docx"])

    if option == "Pegar el texto":
        prompt = st.text_area("Introduzca el texto que desea editar", value="Eres un editor que tiene la tarea de editar papers para una revista científica. Tu haz pedido que usean el sistema APA para las referencias, pero muchos usan otra forma de referenciar. Tu labor es cambiar las referencias bibliográficas al sistema APA más actual.")

        if prompt:
            # Generar el texto con OpenAI
            message = generate_text(prompt)

            # Mostrar el texto generado en la página
            st.header("Texto Editado")
            st.write(message)

    elif option == "Subir archivo .docx":
        uploaded_file = st.file_uploader("Subir archivo .docx", type="docx")

        if uploaded_file is not None:
            # Leer el archivo .docx
            doc = Document(uploaded_file)
            text = "\n".join([p.text for p in doc.paragraphs])

            # Generar el texto con OpenAI
            message = generate_text(text)

            # Mostrar el texto generado en la página
            st.header("Texto Editado")
            st.write(message)

# Ejecutar la aplicación de streamlit
if __name__ == "__main__":
    app()

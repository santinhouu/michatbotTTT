import streamlit as st
import groq

# Modelos disponibles
MODELOS = 'llama3-8b-8192', 'llama3-70b-8192', 'mixtral-8x7b-32768'

# Configurar la página
def configurar_pagina():
    st.set_page_config(page_title="MI PRIMERA PAGINA CON PYTHON", page_icon="🫡")
    st.title("Bienvenidos a mi chatbot")

# Mostrar el sidebar con la selección de modelos
def mostrar_sidebar():
    st.sidebar.title("ELEGÍ TU MODELO DE IA FAVORITO")
    modelo = st.sidebar.selectbox("¿Cuál elegís?", MODELOS, index=0)
    st.write(f"**ELEGISTE EL MODELO:** {modelo}")
    return modelo

# Crear cliente Groq
def crear_cliente_groq():
    groq_api_key = st.secrets["GROQ_API_KEY"]
    return groq.Groq(api_key=groq_api_key)

# Inicializar el estado del chat
def inicializar_estado_chat():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = [
            {"role": "system", "content": "Soy un asistente IA muy útil."}
        ]

# Mostrar historial del chat
def mostrar_historial_chat():
    for mensaje in st.session_state.mensajes:
        with st.chat_message(mensaje["role"]):
            st.markdown(mensaje["content"])

# Obtener mensaje del usuario
def obtener_mensaje_usuario():
    return st.chat_input("Enviá un mensaje")

# Ejecutar la aplicación
def ejecutar_app():
    configurar_pagina()
    modelo_elegido = mostrar_sidebar()
    cliente = crear_cliente_groq()
    inicializar_estado_chat()
    mostrar_historial_chat()

    # Obtener mensaje del usuario
    mensaje_usuario = obtener_mensaje_usuario()
    if mensaje_usuario:
        # Mostrar en la app y guardar en historial
        st.chat_message("user").markdown(mensaje_usuario)
        st.session_state.mensajes.append({"role": "user", "content": mensaje_usuario})

        # Mostrar en la terminal
        print("Mensaje del usuario:", mensaje_usuario)

        # Crear el chat con el modelo elegido
        chat = cliente.chat.completions.create(
            model=modelo_elegido,
            messages=st.session_state.mensajes
        )

        respuesta = chat.choices[0].message.content
        st.chat_message("assistant").markdown(respuesta)
        st.session_state.mensajes.append({"role": "assistant", "content": respuesta})

# Ejecutar la app principal
if __name__ == '__main__':
    ejecutar_app()

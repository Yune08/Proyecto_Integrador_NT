import streamlit as st
import numpy as np
import cv2 

st.header("Aplicación 2")



def contar_objetos(imagen):
    # Convertir la imagen a escala de grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Aplicar umbralización (binarización)
    _, binarizada = cv2.threshold(imagen_gris, 128, 255, cv2.THRESH_BINARY)

    # Encontrar contornos en la imagen binarizada
    contornos, _ = cv2.findContours(binarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Contar el número de objetos
    return len(contornos)

def main():
    st.title("Contador de objetos de una imagen")
    
    # Subida de archivo
    uploaded_file = st.file_uploader("Elije una imagen...", type="jpg")
    
    if uploaded_file is not None:
        # Leer la imagen subida
        imagen = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        
        # Mostrar la imagen
        st.image(imagen, caption="Imagen Original", use_column_width=True)
        
        # Contar objetos
        num_objetos = contar_objetos(imagen)
        
        # Mostrar el resultado
        st.write(f"Número de objetos detectados: {num_objetos}")

if __name__ == "__main__":
    main()
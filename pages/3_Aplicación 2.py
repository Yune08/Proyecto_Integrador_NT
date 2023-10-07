import streamlit as st
import numpy as np
import cv2 

st.header("Aplicación 2")



def contar_objetos(imagen):
    
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    _, binarizada = cv2.threshold(imagen_gris, 128, 255, cv2.THRESH_BINARY)

    contornos, _ = cv2.findContours(binarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  
    return len(contornos)

def main():
    st.title("Contador de objetos de una imagen")
    
  
    uploaded_file = st.file_uploader("Elije una imagen...", type="jpg")
    
    if uploaded_file is not None:
     
        imagen = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        
       
        st.image(imagen, caption="Imagen Original", use_column_width=True)
        
       
        num_objetos = contar_objetos(imagen)
        
       
        st.write(f"Número de objetos detectados: {num_objetos}")

if __name__ == "__main__":
    main()
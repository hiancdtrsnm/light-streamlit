import streamlit as st
import qrcode

st.title("Generador de códigos QR")

url = st.text_input("Introduce la URL que quieres codificar en el código QR")

if url:
    img = qrcode.make(url)
    st.image(img._img, caption="QR Code")
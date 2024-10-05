import streamlit as st

st.title("Calculando el iva")
st.write("Este programa calcula el iva de un producto. El iva es un impuesto indirecto que se aplica a la venta de bienes y servicios.")

tipo_de_iva = {
    "normal": 0.21,
    "reducido": 0.10,
    "superreducido": 0.04,
}

precio = st.number_input("Precio original", min_value=0.0, step=0.01, placeholder="Introduce el precio original del producto del producto")

tipo = st.selectbox("Tipo de iva", list(tipo_de_iva.keys()))


if precio != 0:
    iva = precio * tipo_de_iva[tipo]

    f"El iva es de {iva} €"
    f"El precio final es de {precio + iva} €"



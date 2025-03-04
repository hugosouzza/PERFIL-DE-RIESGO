import streamlit as st
from docx import Document
import os

# Título de la aplicación
st.title("Generación de KYC")

# Selección de persona física o jurídica
persona = st.radio("Selecciona tipo de cliente", ("Persona Física", "Persona Jurídica"))

if persona == "Persona Física":
    # Formulario para persona física
    nombre = st.text_input("Nombre completo")
    numero_ficha = st.text_input("Número de ficha")
    fecha = st.date_input("Fecha")
    domicilio = st.text_input("Domicilio")
    telefono = st.text_input("Teléfono")
    email = st.text_input("Correo electrónico")
    profesion = st.text_input("Profesión")
    origen_fondos = st.text_input("Origen de fondos")
    patrimonio = st.text_input("Patrimonio")
    ingresos_anuales = st.text_input("Ingresos anuales")
    capacidad_patrimonio = st.text_input("Capacidad de patrimonio")
    tipo_poder = st.text_input("Tipo de poder")
    identificado = st.text_input("Identificado")
    estructura_propiedad = st.text_input("Estructura de propiedad")
    falsedad_datos = st.text_input("Falsedad de datos")
    pais_riesgo = st.text_input("País de riesgo")
    actividades_riesgo = st.text_input("Actividades de riesgo")
    operaciones_riesgo = st.text_input("Operaciones de riesgo")
    responsabilidades_publicas = st.text_input("Responsabilidades públicas")
    operacion_inusual = st.text_input("Operación inusual")
    precios_fuera_mercado = st.text_input("Precios fuera de mercado")
    responsable = st.text_input("Responsable")
    fecha_firma = st.date_input("Fecha de firma")

    if st.button("Generar KYC"):
        # Recopilación de datos
        datos_cliente = {
            "nombre": nombre,
            "numero_ficha": numero_ficha,
            "fecha": str(fecha),
            "domicilio": domicilio,
            "telefono": telefono,
            "email": email,
            "profesion": profesion,
            "origen_fondos": origen_fondos,
            "patrimonio": patrimonio,
            "ingresos_anuales": ingresos_anuales,
            "capacidad_patrimonio": capacidad_patrimonio,
            "tipo_poder": tipo_poder,
            "identificado": identificado,
            "estructura_propiedad": estructura_propiedad,
            "falsedad_datos": falsedad_datos,
            "pais_riesgo": pais_riesgo,
            "actividades_riesgo": actividades_riesgo,
            "operaciones_riesgo": operaciones_riesgo,
            "responsabilidades_publicas": responsabilidades_publicas,
            "operacion_inusual": operacion_inusual,
            "precios_fuera_mercado": precios_fuera_mercado,
            "responsable": responsable,
            "fecha_firma": str(fecha_firma)
        }

        # Generar el documento KYC (Word)
        doc = Document("KYC_PS.docx")  # Asegúrate de que la ruta es correcta
        for parrafo in doc.paragraphs:
            for clave, valor in datos_cliente.items():
                if f"{{{{{clave}}}}}" in parrafo.text:
                    parrafo.text = parrafo.text.replace(f"{{{{{clave}}}}}", valor)

        # Guardar el documento generado
        doc.save("KYC_PS_generated.docx")

        # Crear un botón de descarga
        with open("KYC_PS_generated.docx", "rb") as f:
            st.download_button(
                label="Descargar documento KYC",
                data=f,
                file_name="KYC_PS_generated.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        
        # Mensaje de confirmación
        st.success("Documento generado con éxito! Puedes descargarlo utilizando el botón.")

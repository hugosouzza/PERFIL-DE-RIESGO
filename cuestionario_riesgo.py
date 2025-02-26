# ============================================
#               PERSONAL PROJECT
#          Clasificación de riesgo para el cliente
# ============================================

# Importación de librerías
import streamlit as st

# ============================================
#          Función para clasificar el perfil
# ============================================
def clasificar_perfil(puntaje_total):
    if 10 <= puntaje_total <= 17:
        return "Conservador"
    elif 18 <= puntaje_total <= 25:
        return "Moderado"
    elif 26 <= puntaje_total <= 33:
        return "Agresivo"
    elif 34 <= puntaje_total <= 40:
        return "Muy Agresivo"
    else:
        return "Error en la clasificación"

# ============================================
#          Definición de preguntas
# ============================================
preguntas = {
    "Objetivos de inversión": [
        "Preservar el capital y proteger mi inversión",
        "Crecimiento medio asumiendo fluctuaciones moderadas",
        "Aprovechar oportunidades asumiendo fluctuaciones elevadas",
        "Crecimiento fuerte asumiendo fluctuaciones muy elevadas y altos riesgos de pérdida"
    ],
    "Nivel de pérdidas potenciales": [
        "Máximo 5%",
        "Máximo 15%",
        "Máximo 35%",
        "Máximo 55%"
    ],
    "Reacción ante pérdidas": [
        "Vender todo para evitar más pérdidas",
        "Vender una parte para limitar las pérdidas",
        "Mantener la inversión esperando recuperación",
        "Comprar más aprovechando el precio bajo"
    ],
    "Expectativas de rendimiento": [
        "Menos del 3% (muy bajo riesgo)",
        "Entre 3% y 6% (moderado)",
        "Entre 6% y 10% (elevado)",
        "Más del 10% (muy alto)"
    ],
    "Comodidad con la volatilidad": [
        "Muy incómodo, preferiría estabilidad",
        "Algo incómodo, pero dispuesto a asumir cierta volatilidad",
        "Cómodo, entiendo que es parte de invertir a largo plazo",
        "Muy cómodo, buscaría aprovechar la volatilidad"
    ],
    "Conocimiento financiero": [
        "Nulo",
        "Bajo",
        "Medio",
        "Elevado o Muy elevado"
    ],
    "Horizonte temporal": [
        "Menos de 1 año",
        "Entre 1 y 3 años",
        "Entre 3 y 5 años",
        "Más de 5 años"
    ],
    "Porcentaje de patrimonio invertido": [
        "Menos del 5%",
        "Entre el 5% y el 25%",
        "Entre el 25% y el 50%",
        "Más del 50%"
    ],
    "Ingresos anuales": [
        "Menos de 25,000€",
        "Entre 25,000€ y 50,000€",
        "Entre 50,000€ y 100,000€",
        "Más de 100,000€"
    ],
    "Necesidades de liquidez": [
        "Más del 75%",
        "Entre el 50% y el 75%",
        "Entre el 25% y el 50%",
        "Ninguna"
    ]
}

# ============================================
#          Formulario de preguntas
# ============================================
respuestas = []
st.write("## Cuestionario")
for pregunta, opciones in preguntas.items():
    respuesta = st.radio(pregunta, opciones, index=-1)  # Radio buttons sin opción preseleccionada
    if respuesta:  # Verifica que se seleccionó una respuesta
        respuestas.append(opciones.index(respuesta) + 1)  # Guardar índice como respuesta (1 a 4)

# ============================================
#          Cálculo del puntaje total
# ============================================
if st.button('Enviar'):  # Botón para enviar respuestas
    if len(respuestas) == len(preguntas):  # Verifica que se respondieron todas
        puntaje_total = sum(respuestas) * 2.5  # Ajuste de escala al rango 10-40
        puntaje_total = round(puntaje_total)  # Redondeo
        perfil = clasificar_perfil(puntaje_total)  # Clasificación del perfil
        st.write("### Resultado")
        st.write(f"Perfil de riesgo: {perfil}")
    else:
        st.write("Por favor, responde todas las preguntas antes de enviar.")

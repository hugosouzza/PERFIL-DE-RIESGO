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
#          Definición de preguntas con pesos
# ============================================
preguntas = {
    "Objetivos de inversión": {
        "opciones": [
            "Preservar el capital y proteger mi inversión",
            "Crecimiento medio asumiendo fluctuaciones moderadas",
            "Aprovechar oportunidades asumiendo fluctuaciones elevadas",
            "Crecimiento fuerte asumiendo fluctuaciones muy elevadas y altos riesgos de pérdida"
        ],
        "peso": 0.25  # Alta relevancia
    },
    "Nivel de pérdidas potenciales": {
        "opciones": [
            "Máximo 5%",
            "Máximo 15%",
            "Máximo 35%",
            "Máximo 55%"
        ],
        "peso": 0.25  # Alta relevancia
    },
    "Reacción ante pérdidas": {
        "opciones": [
            "Vender todo para evitar más pérdidas",
            "Vender una parte para limitar las pérdidas",
            "Mantener la inversión esperando recuperación",
            "Comprar más aprovechando el precio bajo"
        ],
        "peso": 0.15  # Alta relevancia
    },
    "Expectativas de rendimiento": {
        "opciones": [
            "Menos del 3% (muy bajo riesgo)",
            "Entre 3% y 6% (moderado)",
            "Entre 6% y 10% (elevado)",
            "Más del 10% (muy alto)"
        ],
        "peso": 0.15  # Alta relevancia
    },
    "Comodidad con la volatilidad": {
        "opciones": [
            "Muy incómodo, preferiría estabilidad",
            "Algo incómodo, pero dispuesto a asumir cierta volatilidad",
            "Cómodo, entiendo que es parte de invertir a largo plazo",
            "Muy cómodo, buscaría aprovechar la volatilidad"
        ],
        "peso": 0.10  # Alta relevancia
    },
    "Conocimiento financiero": {
        "opciones": [
            "Nulo",
            "Bajo",
            "Medio",
            "Elevado o Muy elevado"
        ],
        "peso": 0.02  # Baja relevancia
    },
    "Horizonte temporal": {
        "opciones": [
            "Menos de 1 año",
            "Entre 1 y 3 años",
            "Entre 3 y 5 años",
            "Más de 5 años"
        ],
        "peso": 0.02  # Baja relevancia
    },
    "Porcentaje de patrimonio invertido": {
        "opciones": [
            "Menos del 5%",
            "Entre el 5% y el 25%",
            "Entre el 25% y el 50%",
            "Más del 50%"
        ],
        "peso": 0.02  # Baja relevancia
    },
    "Ingresos anuales": {
        "opciones": [
            "Menos de 25,000€",
            "Entre 25,000€ y 50,000€",
            "Entre 50,000€ y 100,000€",
            "Más de 100,000€"
        ],
        "peso": 0.02  # Baja relevancia
    },
    "Necesidades de liquidez": {
        "opciones": [
            "Más del 75%",
            "Entre el 50% y el 75%",
            "Entre el 25% y el 50%",
            "Ninguna"
        ],
        "peso": 0.02  # Baja relevancia
    }
}

# ============================================
#          Formulario de preguntas
# ============================================
respuestas = []
st.write("## Cuestionario")
for pregunta, detalles in preguntas.items():
    respuesta = st.radio(pregunta, detalles["opciones"])  # Radio buttons sin opción preseleccionada
    if respuesta:  # Verifica que se seleccionó una respuesta
        puntaje = (detalles["opciones"].index(respuesta) + 1) * detalles["peso"]  # Multiplica por peso
        respuestas.append(puntaje)  # Guarda el puntaje ponderado

# ============================================
#          Cálculo del puntaje total
# ============================================
if st.button('Enviar'):  # Botón para enviar respuestas
    if len(respuestas) == len(preguntas):  # Verifica que se respondieron todas
        puntaje_total = sum(respuestas) * 10  # Ajuste de escala al rango 10-40
        puntaje_total = round(puntaje_total)  # Redondeo
        perfil = clasificar_perfil(puntaje_total)  # Clasificación del perfil
        st.write("### Resultado")
        st.write(f"Puntaje total: {puntaje_total}")  # Mostramos el puntaje total
        st.write(f"Perfil de riesgo: {perfil}")
    else:
        st.write("Por favor, responde todas las preguntas antes de enviar.")


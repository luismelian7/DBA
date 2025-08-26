import streamlit as st
import pandas as pd
import numpy as np

# Título de la aplicación
st.title("DBA: Plataforma de Inteligencia Empresarial")

# Cargar datos (puedes conectar a una base de datos o usar un CSV)
data = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Ventas': [20000, 25000, 30000, 28000],
    'Gastos': [15000, 17000, 16000, 18000]
})

# Mostrar datos
st.write("Datos de Ventas y Gastos")
st.dataframe(data)

# Visualización
st.write("Gráfico de Ventas vs Gastos")
st.line_chart(data.set_index('Mes')[['Ventas', 'Gastos']])

# Predicción simple (ejemplo)
st.write("Predicción de Ventas para el Próximo Mes")
prediccion = data['Ventas'].mean() * 1.1  # Ejemplo: aumento del 10%
st.write(f"Ventas estimadas: ${prediccion:.2f}")
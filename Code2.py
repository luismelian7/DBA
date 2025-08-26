import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("DBA - Análisis de Ventas para Pymes")

# Subir archivo CSV
uploaded_file = st.file_uploader("Sube tu archivo de ventas (CSV)", type="csv")

if uploaded_file is not None:
    # Leer datos
    df = pd.read_csv(uploaded_file)
    
    # Análisis básico
    total_ventas = df["Ingresos"].sum()
    top_producto = df.groupby("Producto")["Ingresos"].sum().idxmax()
    
    # Mostrar resultados
    st.write(f"Total de ventas: ${total_ventas:,.2f}")
    st.write(f"Producto más vendido: {top_producto}")
    
    # Gráfico de tendencias
    df["Fecha"] = pd.to_datetime(df["Fecha"])
    ventas_por_mes = df.groupby(df["Fecha"].dt.to_period("M"))["Ingresos"].sum()
    
    fig, ax = plt.subplots()
    ventas_por_mes.plot(kind="line", ax=ax)
    ax.set_title("Tendencia de Ventas")
    st.pyplot(fig)

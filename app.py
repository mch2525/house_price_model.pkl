import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Simulador de Precio de Vivienda")

st.title("Estimador de Precio de Vivienda")

# Cargar modelo y pipeline
model = joblib.load("house_price_model.pkl")

# Entradas del usuario
size = st.number_input("Tamaño construido (m²)", min_value=20.0, max_value=1000.0, value=100.0, step=1.0)
bedrooms = st.slider("Número de habitaciones", 1, 10, 3)
location = st.selectbox("Nivel socioeconómico (1‑5)", [1, 2, 3, 4, 5])
age = st.number_input("Antigüedad (años)", min_value=0, max_value=100, value=10)
income = st.number_input("Ingreso promedio de la zona (MXN)", min_value=5000, max_value=100000, value=30000, step=1000)
distance = st.number_input("Distancia al centro (km)", min_value=0.0, max_value=50.0, value=5.0, step=0.5)
parking = st.selectbox("¿Cuenta con estacionamiento?", ["Sí", "No"])
parking_bin = 1 if parking == "Sí" else 0

# Predicción
if st.button("Calcular precio estimado"):
    X = np.array([[size, bedrooms, location, age, income, distance, parking_bin]])
    price = model.predict(X)[0]
    st.subheader(f"Precio estimado: ${price:,.0f} MXN")

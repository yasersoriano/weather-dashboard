import requests
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Weather Dashboard", layout="wide")

st.title("🌦️ Weather Dashboard (API + Streamlit)")
st.write("Dashboard que consume **Open-Meteo API** y visualiza clima por hora.")

city = st.text_input("Ciudad (ej: Guadalajara)", "Guadalajara")
lat = st.number_input("Latitud", value=20.6597, format="%.6f")
lon = st.number_input("Longitud", value=-103.3496, format="%.6f")

if st.button("Cargar clima"):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&hourly=temperature_2m,precipitation_probability,windspeed_10m"
        "&timezone=auto"
    )

    r = requests.get(url, timeout=30)
    r.raise_for_status()
    data = r.json()

    df = pd.DataFrame({
        "time": pd.to_datetime(data["hourly"]["time"]),
        "temperature_2m": data["hourly"]["temperature_2m"],
        "precipitation_probability": data["hourly"]["precipitation_probability"],
        "windspeed_10m": data["hourly"]["windspeed_10m"],
    })

    st.subheader(f"📍 {city}")

    c1, c2, c3 = st.columns(3)
    c1.metric("Temp promedio (°C)", f"{df['temperature_2m'].mean():.1f}")
    c2.metric("Prob. lluvia promedio (%)", f"{df['precipitation_probability'].mean():.1f}")
    c3.metric("Viento promedio (km/h)", f"{df['windspeed_10m'].mean():.1f}")

    left, right = st.columns(2)
    with left:
        fig1 = px.line(df, x="time", y="temperature_2m", title="Temperatura por hora")
        st.plotly_chart(fig1, use_container_width=True)

        fig2 = px.line(df, x="time", y="windspeed_10m", title="Viento por hora")
        st.plotly_chart(fig2, use_container_width=True)

    with right:
        fig3 = px.bar(df, x="time", y="precipitation_probability", title="Probabilidad de lluvia por hora")
        st.plotly_chart(fig3, use_container_width=True)

        st.write("Vista rápida de datos:")
        st.dataframe(df.head(24))

    out_path = "data/sample_weather.csv"
    df.to_csv(out_path, index=False)
    st.success(f"Datos guardados en {out_path}")


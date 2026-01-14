# 🌦️ Weather Dashboard (API + Streamlit)

## Live Demo
https://weather-dashboard-2nghxqxopuwkmgxr2w7bfb.streamlit.app/


Interactive dashboard that consumes the **Open-Meteo API** and visualizes hourly weather metrics.

## What this project does
- Fetches hourly weather data from an API
- Builds a clean DataFrame for analysis
- Visualizes temperature, rain probability, and wind speed
- Saves a small sample CSV output for reproducibility

## Tech Stack
- Python
- pandas
- requests
- plotly
- Streamlit

## How to run locally
```bash
git clone https://github.com/yasersoriano/weather-dashboard.git
cd weather-dashboard
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

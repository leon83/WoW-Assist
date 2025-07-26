import streamlit as st
import numpy as np

st.set_page_config(page_title="WoWs Vorhalte-Rechner", layout="centered")

st.title("🔫 World of Warships – Vorhalte-Rechner")

st.markdown("""
Gib die Werte unten ein, um zu berechnen, wie viele Schiffslängen du vorhalten musst, um dein Ziel zu treffen.
""")

# Eingaben
entfernung_km = st.slider("Entfernung zum Ziel (in km)", 1.0, 25.0, 12.0, step=0.5)
geschwindigkeit_knoten = st.slider("Zielgeschwindigkeit (in Knoten)", 0, 50, 30)
winkel_grad = st.slider("Winkel zum Ziel (0° = frontal, 90° = quer)", 0, 90, 90)

# Berechnung
def berechne_vorhalt(entfernung_km, geschwindigkeit_knoten, winkel_grad):
    geschwindigkeit_mps = geschwindigkeit_knoten * 0.51444
    winkel_rad = np.deg2rad(winkel_grad)
    effektive_geschwindigkeit = geschwindigkeit_mps * np.sin(winkel_rad)
    flugzeit_s = entfernung_km * 0.7  # grobe Näherung
    vorhalt_meter = effektive_geschwindigkeit * flugzeit_s
    schiff_laenge = 180
    vorhalt_schiff = vorhalt_meter / schiff_laenge
    return round(vorhalt_schiff, 2)

# Ergebnis
vorhalten = berechne_vorhalt(entfernung_km, geschwindigkeit_knoten, winkel_grad)

st.success(f"👉 Empfohlenes Vorhalten: **{vorhalten} Schiffslängen**")

st.caption("Hinweis: Dies ist eine Näherung. Werte können je nach Schiff und Munition variieren.")

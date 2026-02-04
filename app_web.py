import streamlit as st
from app.analyseur_classe import AnalyseurStatistique
import pandas as pd

st.title("📊 Mon Analyseur de Données Pro")
st.write("Bienvenue ! Chargez votre fichier CSV pour obtenir une analyse instantanée.")

# 1. Zone de chargement de fichier
fichier_uploade = st.file_uploader("Choisissez un fichier CSV", type="csv")

if fichier_uploade is not None:
    # 2. On utilise ton moteur (la classe)
    # On sauvegarde temporairement le fichier pour l'Analyseur
    with open("temp.csv", "wb") as f:
        f.write(fichier_uploade.getbuffer())
    
    analyseur = AnalyseurStatistique("temp.csv")
    analyseur.charger_donnees()

    # 3. Interface interactive
    colonne = st.selectbox("Quelle colonne voulez-vous analyser ?", analyseur.df.columns)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Moyenne", f"{analyseur.donner_moyenne(colonne):.2f}")
    with col2:
        st.metric("Maximum", f"{analyseur.donner_max(colonne)}")

    # 4. Un petit graphique bonus (Pandas + Streamlit)
    st.line_chart(analyseur.df[colonne])
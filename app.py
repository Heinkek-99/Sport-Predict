import streamlit as st
import pandas as pd
import joblib

# Titre de l'application
st.title("Application de Prédiction")

# Charger le modèle
model = joblib.load('best_ridge_model.pkl')

# Formulaire pour saisir les variables
st.sidebar.header("Saisissez les valeurs des variables")

# Variables numériques
age = st.sidebar.number_input("Âge", min_value=0, max_value=120, value=30)
weight = st.sidebar.number_input("Poids (kg)", min_value=0.0, max_value=300.0, value=70.0)
height = st.sidebar.number_input("Taille (m)", min_value=0.0, max_value=3.0, value=1.75)
max_bpm = st.sidebar.number_input("BPM Maximum", min_value=0, max_value=300, value=180)
avg_bpm = st.sidebar.number_input("BPM Moyen", min_value=0, max_value=300, value=70)
resting_bpm = st.sidebar.number_input("BPM au repos", min_value=0, max_value=300, value=60)
session_duration = st.sidebar.number_input("Durée de la session (heures)", min_value=0.0, max_value=24.0, value=1.0)
fat_percentage = st.sidebar.number_input("Pourcentage de graisse", min_value=0.0, max_value=100.0, value=20.0)
water_intake = st.sidebar.number_input("Consommation d'eau (litres)", min_value=0.0, max_value=20.0, value=2.0)
workout_frequency = st.sidebar.number_input("Fréquence d'entraînement (jours/semaine)", min_value=0.0, max_value=7.0, value=3.0)
experience_level = st.sidebar.number_input("Niveau d'expérience", min_value=0.0, max_value=10.0, value=5.0)
bmi = st.sidebar.number_input("IMC", min_value=0.0, max_value=100.0, value=22.0)

# Variables catégorielles
gender_male = st.sidebar.selectbox("Genre (Homme = 1, Femme = 0)", [1, 0])
workout_type = st.sidebar.selectbox("Type d'entraînement", ["HIIT", "Strength", "Yoga"])

# Encodage du type d'entraînement
workout_type_hiit = 1 if workout_type == "HIIT" else 0
workout_type_strength = 1 if workout_type == "Strength" else 0
workout_type_yoga = 1 if workout_type == "Yoga" else 0

# Créer un DataFrame avec les valeurs saisies
input_data = pd.DataFrame({
    'Age': [age],
    'Weight (kg)': [weight],
    'Height (m)': [height],
    'Max_BPM': [max_bpm],
    'Avg_BPM': [avg_bpm],
    'Resting_BPM': [resting_bpm],
    'Session_Duration (hours)': [session_duration],
    'Fat_Percentage': [fat_percentage],
    'Water_Intake (liters)': [water_intake],
    'Workout_Frequency (days/week)': [workout_frequency],
    'Experience_Level': [experience_level],
    'BMI': [bmi],
    'Gender_Male': [gender_male],
    'Workout_Type_HIIT': [workout_type_hiit],
    'Workout_Type_Strength': [workout_type_strength],
    'Workout_Type_Yoga': [workout_type_yoga]
})

# Bouton pour lancer la prédiction
if st.sidebar.button("Prédire"):
    
    try:

    # Faire la prédiction
        prediction = model.predict(input_data)

    # Affichage du résultat
        st.success(f"🔥 **Dépense calorique estimée :** {prediction[0]:.2f} kcal")
    #st.success(f"La prédiction est : {prediction[0]}")
    
    except Exception as e:
        st.error(f"❌ Une erreur s'est produite : {str(e)}")

# Section d'information
with st.expander("ℹ️ Comment utiliser cette application"):
    st.write("""
        Cette application prédit la dépense calorique en fonction de vos données personnelles et de votre session sportive.
        - **Âge** : Votre âge en années.
        - **Poids** : Votre poids en kilogrammes.
        - **Taille** : Votre taille en centimètres.
        - **Durée** : La durée de votre session sportive en minutes.
        - **BPM** : Votre fréquence cardiaque moyenne pendant l'entraînement.
        - **Température** : La température ambiante en degrés Celsius.
        - **Hydratation** : Cochez si vous étiez bien hydraté pendant l'entraînement.
        - **% Graisse corporelle** : Votre pourcentage de graisse corporelle.
    """)
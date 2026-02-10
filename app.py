
import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("carmodel.pkl")

st.title("🚗 Car Price Prediction")

with st.form("car_price_form"):

    # -------- CATEGORICAL INPUTS --------
    brand = st.selectbox("Brand", ["Toyota", "BMW", "Audi", "Honda", "Hyundai"])

    fuel_type = st.selectbox(
        "Fuel Type", ["Petrol", "Diesel", "Electric", "Hybrid"]
    )

    body_type = st.selectbox(
        "Body Type", ["Sedan", "SUV", "Hatchback", "Coupe"]
    )

    transmission = st.selectbox(
        "Transmission", ["Manual", "Automatic"]
    )

    country = st.selectbox(
        "Manufacturing Country", ["Japan", "Germany", "USA", "India"]
    )

    # -------- NUMERIC INPUTS --------
    manufacture_year = st.number_input(
        "Manufacture Year", min_value=1990, max_value=2025, value=2018
    )

    engine_cc = st.number_input(
        "Engine CC", min_value=500, max_value=6000, value=1500
    )

    horsepower = st.number_input(
        "Horsepower", min_value=50, max_value=1000, value=150
    )

    mileage = st.number_input(
        "Mileage (km per liter)", min_value=1, max_value=50, value=15
    )

    car_age = st.number_input(
        "Car Age (years)", min_value=0, max_value=40, value=5
    )

    hp_per_cc = st.number_input(
        "HP per CC", min_value=0.01, max_value=2.0, value=0.1
    )

    efficiency_score = st.number_input(
        "Efficiency Score", min_value=0.0, max_value=10.0, value=6.0
    )

    submit = st.form_submit_button("Predict Price")

# -------- PREDICTION --------
if submit:
    input_df = pd.DataFrame([{
        "Brand": brand,
        "Fuel_Type": fuel_type,
        "Body_Type": body_type,
        "Transmission": transmission,
        "Manufacturing_Country": country,
        "Manufacture_Year": manufacture_year,
        "Engine_CC": engine_cc,
        "Horsepower": horsepower,
        "Mileage_km_per_l": mileage,
        "Car_Age": car_age,
        "HP_per_CC": hp_per_cc,
        "Efficiency_Score": efficiency_score
    }])

    prediction = model.predict(input_df)

    st.success(f"Predicted Price (USD): ${prediction[0]:,.2f}")
    st.balloons()

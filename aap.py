import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("🚗 Car Selling Price Predictor")
st.write("Enter car details to predict selling price")

# Input fields
year = st.number_input("Year of Purchase", min_value=1990, max_value=2025, value=2018)
present_price = st.number_input("Present Showroom Price (in Lakhs)", min_value=0.0, step=0.1)
kms_driven = st.number_input("Kilometers Driven", min_value=0)
owner = st.selectbox("Owner Type", [0, 1, 2])

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])

# Encoding
fuel_petrol = 1 if fuel_type == "Petrol" else 0
fuel_diesel = 1 if fuel_type == "Diesel" else 0
seller_individual = 1 if seller_type == "Individual" else 0
transmission_manual = 1 if transmission == "Manual" else 0

# Predict button
if st.button("Predict Price"):
    input_data = np.array([[year, present_price, kms_driven, owner,
                             fuel_diesel, fuel_petrol,
                             seller_individual, transmission_manual]])
    
    prediction = model.predict(input_data)
    
    st.success(f"💰 Estimated Selling Price: ₹ {round(prediction[0], 2)} Lakhs")

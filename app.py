# Import required libraries
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Show that app started successfully
st.write("✅ Streamlit app started!")

# Title and description
st.set_page_config(page_title="Water Pollutants Predictor", layout="centered")
st.title("💧 Water Pollutants Predictor")
st.write("🔬 Predict water pollutant levels based on Year and Station ID.")

# Try to load model and columns
try:
    model = joblib.load("pollution_model.pkl")
    model_cols = joblib.load("model_columns.pkl")
    model_loaded = True
except Exception as e:
    st.error(f"❌ Error loading model or columns: {e}")
    st.info("Using random simulated values instead.")
    model_loaded = False

# Input fields
year_input = st.number_input("📅 Enter Year", min_value=2000, max_value=2100, value=2022)
station_id = st.text_input("🏷️ Enter Station ID", value='1')

# On button click
if st.button("🔍 Predict"):
    if not station_id:
        st.warning("⚠️ Please enter a valid Station ID.")
    else:
        # Define pollutants
        pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']

        # Show header
        st.subheader(f"🧪 Predicted pollutant levels for Station '{station_id}' in {year_input}:")

        # If model is loaded, use it
        if model_loaded:
            try:
                # Prepare input
                input_df = pd.DataFrame({'year': [year_input], 'id': [station_id]})
                input_encoded = pd.get_dummies(input_df, columns=['id'])

                # Align columns
                for col in model_cols:
                    if col not in input_encoded.columns:
                        input_encoded[col] = 0
                input_encoded = input_encoded[model_cols]

                # Predict
                predicted_pollutants = model.predict(input_encoded)[0]

                # Show results
                for p, val in zip(pollutants, predicted_pollutants):
                    st.write(f"• **{p}**: {val:.2f}")
            except Exception as err:
                st.error(f"❌ Prediction failed: {err}")
        else:
            # Fallback dummy prediction
            for p in pollutants:
                st.write(f"• **{p}**: {np.random.uniform(0, 10):.2f} (simulated)")

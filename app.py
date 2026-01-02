import streamlit as st
import joblib
import pandas as pd

# 1. LOAD THE TRAINED MODEL
# This tells the app to use the "brain" you built in Jupyter
model = joblib.load('soil_erosion_model.pkl')

# 2. CREATE THE INTERFACE
st.title("Soil Erosion Predictor")
st.write("Adjust the sliders to see how the erosion rate changes.")

# 3. SETUP INPUTS
# These create sliders so your friend/lecturer can change the numbers
rain = st.slider("Rainfall (mm)", 50, 300, 150)
slope = st.slider("Slope (%)", 0, 30, 15)
veg = st.slider("Vegetation Cover (%)", 0, 100, 50)
moist = st.slider("Moisture (%)", 5, 40, 20)
soil = st.selectbox("Soil Type", [1, 2, 3]) # 1=Sandy, 2=Loamy, 3=Clay

# 4. MAKE THE PREDICTION
# When the user clicks the button, the model calculates the result
if st.button("Predict"):
    # We put the inputs in the same order the model learned them
    features = pd.DataFrame([[rain, slope, soil, veg, moist]], 
                            columns=['rainfall', 'slope', 'soil_type', 'vegetation', 'moisture'])
    
    result = model.predict(features)
    st.success(f"Predicted Erosion Rate: {result[0]:.2f}")
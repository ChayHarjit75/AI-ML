import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Personality Predictor", layout="centered")
st.header(" Introvert or Extrovert Personality Prediction")

# Load and preprocess dataset
df = pd.read_csv("personality_dataset.csv")
df = pd.get_dummies(df, columns=['Stage_fear', 'Drained_after_socializing', 'Personality']).dropna()

# Features and target
x = df.drop(columns=['Personality_Extrovert', 'Personality_Introvert'])
y = df[['Personality_Extrovert', 'Personality_Introvert']]

# Train the model
model = LinearRegression()
model.fit(x, y)

# Input fields
time_spend = st.text_input(" Enter your time spent alone (per day in hours):")
stage_fear = st.selectbox(" Do you have stage fear?", ("Yes", "No"))
social = st.text_input(" Social event attendance (per month):")
outside = st.text_input(" How many times do you go outside weekly?")
drained = st.selectbox(" Do you feel drained after socializing?", ("Yes", "No"))
friend = st.text_input(" Size of your friend circle:")
post = st.text_input(" Time spent online (per day in hours):")

# Convert categorical inputs
sf_yes, sf_no = (1, 0) if stage_fear == 'Yes' else (0, 1)
d_yes, d_no = (1, 0) if drained == 'Yes' else (0, 1)

# When user clicks submit
if st.button("Submit"):
    # Build new input data
    new_data = {
        'Spending_time_lonely': float(time_spend),
        'Social_Event_Attendance': float(social),
        'Going_outside': float(outside),
        'Friend_circle': float(friend),
        'Time_spend_online': float(post),
        'Stage_fear_No': sf_no,
        'Stage_fear_Yes': sf_yes,
        'Drained_after_socializing_Yes': d_yes,
        'Drained_after_socializing_No': d_no
    }

    # Ensure it matches model input columns
    input_df = pd.DataFrame([new_data])
    input_df = input_df.reindex(columns=x.columns, fill_value=0)

    # Prediction
    prediction = model.predict(input_df)[0]  # [0.47, 0.52]
    labels = ['Extrovert', 'Introvert']
    predicted_label = labels[np.argmax(prediction)]

    st.success(f" **Predicted Personality:** {predicted_label}")

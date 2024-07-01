import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained model and label encoder
model = joblib.load('restaurant_cuisine_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Adding a default label for unseen cities
unseen_label = 'Unknown'
if unseen_label not in label_encoder.classes_:
    label_encoder.classes_ = list(label_encoder.classes_) + [unseen_label]

# Streamlit UI
st.title("Restaurant Cuisine Classifier")
city = st.text_input("City")
price_range = st.number_input("Price Range", min_value=1, max_value=5, value=3)
aggregate_rating = st.number_input("Aggregate Rating", min_value=0.0, max_value=5.0, value=4.0)
votes = st.number_input("Votes", min_value=0, value=100)

if st.button("Classify"):
    if city in label_encoder.classes_:
        city_encoded = label_encoder.transform([city])[0]
    else:
        city_encoded = label_encoder.transform([unseen_label])[0]

    input_data = pd.DataFrame({
        'City': [city_encoded],
        'Price range': [price_range],
        'Aggregate rating': [aggregate_rating],
        'Votes': [votes]
    })
    prediction = model.predict(input_data)[0]
    cuisine = label_encoder.inverse_transform([prediction])[0]
    st.write(f"The predicted cuisine is: {cuisine}")

import streamlit as st
import joblib

from src.predict import detect_urgency


# Load trained model and TF-IDF vectorizer
model = joblib.load("models/ticket_classifier.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


# Page configuration
st.set_page_config(
    page_title="Support Ticket Classifier",
    page_icon="🎫"
)


# Title
st.title("🎫 Support Ticket Classifier")

st.write(
    "Enter a customer support ticket below to predict its category "
    "and urgency."
)


# Ticket input
ticket_text = st.text_area(
    "Enter your support ticket:",
    placeholder="Example: I am unable to access my account and need help immediately."
)


# Predict button
if st.button("Predict"):

    if ticket_text.strip() == "":
        st.warning("Please enter a support ticket.")

    else:
        # Convert ticket text into TF-IDF features
        ticket_tfidf = vectorizer.transform([ticket_text])

        # Predict ticket category
        predicted_category = model.predict(ticket_tfidf)[0]

        # Detect urgency
        predicted_urgency = detect_urgency(ticket_text)

        # Display results
        st.subheader("Prediction")

        st.write("**Ticket Category:**", predicted_category)
        st.write("**Urgency:**", predicted_urgency)
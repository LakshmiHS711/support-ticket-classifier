# Support Ticket Classifier

A simple NLP-based support ticket classification system that predicts the category of a customer support ticket and determines its urgency.

## Project Objective

The goal of this project is to automatically classify customer support tickets into different categories and assign an urgency level.

### Ticket Categories

The model predicts one of the following categories:

- Billing inquiry
- Cancellation request
- Product inquiry
- Refund request
- Technical issue

### Urgency Levels

The system assigns:

- Low
- Medium
- High

Urgency is determined using keyword-based rules.

---

## Technologies Used

- Python
- pandas
- NumPy
- scikit-learn
- TF-IDF
- Logistic Regression
- Streamlit
- joblib

---

## Dataset

The project uses the Customer Support Ticket Dataset from Kaggle.

The dataset contains 8,469 customer support tickets and 17 columns.

For classification, the following fields are used:

- Ticket Subject
- Ticket Description

The target variable is:

- Ticket Type

---

## Machine Learning Approach

### 1. Data Loading

The customer support ticket dataset is loaded using pandas.

### 2. Text Preparation

The Ticket Subject and Ticket Description are combined into a single text field.

### 3. Train/Test Split

The dataset is divided into:

- 80% training data
- 20% testing data

### 4. TF-IDF

TF-IDF is used to convert ticket text into numerical features that can be processed by the machine learning model.

### 5. Classification

Logistic Regression is trained using the TF-IDF features.

### 6. Evaluation

The model is evaluated using:

- Accuracy
- Weighted F1-score

### 7. Urgency Detection

A keyword-based approach is used to classify tickets as Low, Medium, or High urgency.

### 8. Streamlit Application

A Streamlit application allows users to enter a support ticket and receive:

- Predicted ticket category
- Predicted urgency

---

## Model Performance

The model achieved:

- Accuracy: 20.54%
- Weighted F1-score: 20.54%

The dataset contains noisy and inconsistent ticket text and labels, which limits classification performance.

---

## Project Structure

```text
support-ticket-classifier/
│
├── data/
│   └── customer_support_tickets.csv
│
├── models/
│   ├── ticket_classifier.pkl
│   └── tfidf_vectorizer.pkl
│
├── src/
│   ├── train.py
│   └── predict.py
│
├── app.py
├── requirements.txt
└── README.md
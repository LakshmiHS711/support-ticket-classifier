# Support Ticket Category Classifier

## How to Run

### Prerequisites

Make sure Python 3.10 or later is installed.

Check Python:

```bash
python --version
```

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/support-ticket-classifier.git
```

Go to the project folder:

```bash
cd support-ticket-classifier
```

---

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3: Train the Model

```bash
python src/train.py
```

This trains the classifier and saves the trained model inside the `models/` folder.

---

### Step 4: Test Urgency Detection

```bash
python src/predict.py
```

This tests the urgency prediction using sample tickets.

---

### Step 5: Run the Demo App

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

If it does not open automatically, go to:

```text
http://localhost:8501
```

---

### Step 6: Use the Application

Enter a customer support ticket in the text box and click **Predict**.

The application will show:

- Predicted category
- Predicted urgency

Example:

```text
I cannot access my account. It is not working and I need help immediately.
```

The application will return the predicted category and urgency.

---

## Project Files

- `app.py` — Streamlit demo application
- `src/train.py` — Model training
- `src/predict.py` — Urgency testing
- `data/` — Dataset
- `models/` — Trained model and TF-IDF vectorizer
- `requirements.txt` — Required Python packages
- `PROJECT_WRITEUP.md` — Project write-up

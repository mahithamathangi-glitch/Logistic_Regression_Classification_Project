import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Breast Cancer Classification",
    page_icon="🩺",
    layout="wide"
)

# Load model and scaler
model = joblib.load("logistic_regression_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🩺 Breast Cancer Classification")
st.write(
    "Logistic Regression based binary classification "
    "using the Breast Cancer Wisconsin dataset."
)

st.info(
    "Enter the 30 tumor measurement features below to generate "
    "a classification prediction."
)

# Feature names
feature_names = [
    "mean radius",
    "mean texture",
    "mean perimeter",
    "mean area",
    "mean smoothness",
    "mean compactness",
    "mean concavity",
    "mean concave points",
    "mean symmetry",
    "mean fractal dimension",
    "radius error",
    "texture error",
    "perimeter error",
    "area error",
    "smoothness error",
    "compactness error",
    "concavity error",
    "concave points error",
    "symmetry error",
    "fractal dimension error",
    "worst radius",
    "worst texture",
    "worst perimeter",
    "worst area",
    "worst smoothness",
    "worst compactness",
    "worst concavity",
    "worst concave points",
    "worst symmetry",
    "worst fractal dimension"
]

# Load example data
try:
    sample_data = pd.read_csv("preprocessed_breast_cancer.csv")
    sample_values = sample_data.drop(columns=["target"]).iloc[0].values
except Exception:
    sample_values = [0.0] * 30

st.subheader("Tumor Measurements")

input_values = []

cols = st.columns(3)

for i, feature in enumerate(feature_names):
    with cols[i % 3]:
        value = st.number_input(
            feature,
            value=float(sample_values[i]),
            format="%.6f"
        )
        input_values.append(value)

if st.button("🔍 Predict", type="primary"):

    input_df = pd.DataFrame(
        [input_values],
        columns=feature_names
    )

    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)[0]
    probabilities = model.predict_proba(input_scaled)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Prediction: Malignant")
    else:
        st.success("Prediction: Benign")

    st.write(
        f"Benign Probability: {probabilities[0] * 100:.2f}%"
    )

    st.write(
        f"Malignant Probability: {probabilities[1] * 100:.2f}%"
    )

    probability_df = pd.DataFrame({
        "Class": ["Benign", "Malignant"],
        "Probability": probabilities
    })

    st.bar_chart(
        probability_df.set_index("Class")
    )

st.divider()

st.caption(
    "Educational machine-learning demonstration. "
    "This model should not be used as a medical diagnostic tool."
)
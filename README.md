# Logistic Regression Classification

## Project Overview

This project implements a Logistic Regression model for binary classification using the Breast Cancer Wisconsin dataset.

The objective is to train a classification model and evaluate its predictions on previously unseen test data.

## Objective

Build a Logistic Regression classification model and evaluate its performance using appropriate classification metrics.

## Dataset

The Breast Cancer Wisconsin dataset available through Scikit-learn was used.

The target variable represents two classes:

- 0 = Benign
- 1 = Malignant

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Google Colab
- Git
- GitHub

## Machine Learning Workflow

1. Dataset loading
2. Data exploration
3. Missing-value checking
4. Target preparation
5. Train-test splitting
6. Feature scaling
7. Logistic Regression training
8. Class prediction
9. Probability prediction using `predict_proba()`
10. Model evaluation
11. Confusion matrix analysis
12. ROC-AUC analysis
13. Model coefficient interpretation
14. Saving predictions and model files

## Model

The project uses Logistic Regression as the binary classification algorithm.

The model predicts whether a sample belongs to the Benign or Malignant class.

## Evaluation Metrics

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC-AUC

## Prediction Probabilities

The `predict_proba()` method is used to obtain the probability associated with each class.

## Project Files

| File | Description |
|---|---|
| `Logistic_Regression_Classification.ipynb` | Complete Colab notebook |
| `preprocessed_breast_cancer.csv` | Preprocessed dataset |
| `predictions.csv` | Model predictions |
| `logistic_regression_model.pkl` | Trained Logistic Regression model |
| `scaler.pkl` | Feature scaling object |
| `app.py` | Streamlit application |
| `requirements.txt` | Python dependencies |
| `deployment.yaml` | Deployment configuration |
| `rollback_evidence.md` | Git rollback documentation |
| `images/` | Project screenshots and visual results |

## Results

The notebook contains the complete accuracy, classification report, confusion matrix and ROC-AUC results obtained during model evaluation.

## Model Interpretation

Logistic Regression coefficients provide information about how individual features contribute to the model's classification decision.

Positive coefficients increase the model's tendency toward the positive class, while negative coefficients decrease it, with other features held constant.

## Conclusion

This project demonstrates the complete workflow of a binary classification problem using Logistic Regression, from preprocessing and training to prediction, probability estimation and model evaluation.

## Disclaimer

This project is an educational machine-learning demonstration and is not intended for medical diagnosis or clinical decision-making.
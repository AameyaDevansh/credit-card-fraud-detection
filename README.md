# 💳 Credit Card Fraud Detection

A machine learning project to identify fraudulent credit card transactions using a real-world, highly imbalanced dataset. The goal is to build a predictive model that can detect fraud with high accuracy and recall.

---

## 📂 Dataset

- **Source**: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Description**: Anonymized transactions from European credit card holders (September 2013).
- **Size**: 284,807 transactions × 31 features
- **Target**: `Class` — 0 (Not Fraud), 1 (Fraud)
- **Imbalance**: Only ~0.17% transactions are fraudulent.

**Note:** To download the dataset, run:
```bash
python get_data.py
```
---

## ⚙️ Project Structure

```
credit-card-fraud-detection/
├── data/                        # Dataset CSV
├── models/                     # Saved ML model (.pkl)
├── notebooks/                  # EDA & Model Training notebooks
├── src/                        # Preprocessing Python scripts
├── requirements.txt            # Project dependencies
├── README.md                   # This file
└── .gitignore
```

---

## 🚀 Workflow

### 🔍 1. EDA (`EDA_With_Text.ipynb`)
- Checked class imbalance
- Analyzed distributions of `Amount` and `Time`
- Visualized feature correlations
- Compared PCA components for fraud vs non-fraud

### 🧹 2. Preprocessing (`src/preprocessing.py`)
- Scaled `Amount` and `Time` features
- Dropped original unscaled columns
- Performed train-test split (stratified)

### ⚖️ 3. Class Imbalance Handling
- Applied **SMOTE (Synthetic Minority Oversampling Technique)** on training data to balance classes

### 🤖 4. Model Training (`Model_Training_With_Text.ipynb`)
- Trained **Logistic Regression**
- Trained **Random Forest Classifier**
- Evaluated using:
  - Precision, Recall, F1-Score
  - ROC-AUC
  - Confusion Matrix
  - ROC Curves

### 💾 5. Model Export
- Saved best-performing model (`fraud_detection_rf.pkl`) using `joblib`

---

## 🧠 Best Model: Random Forest

| Metric        | Value      |
|---------------|------------|
| Accuracy      | ~99%       |
| Precision     | High       |
| Recall        | High       |
| ROC-AUC       | ~0.98      |

> Random Forest outperformed Logistic Regression, especially in detecting the minority class.

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

If you'd prefer a minimal list:

```txt
pandas
numpy
matplotlib
seaborn
scikit-learn
imbalanced-learn
joblib
```

---

## ▶️ How to Run

```bash
git clone https://github.com/your-username/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```

Open and run these notebooks:
- `notebooks/EDA_With_Text.ipynb`
- `notebooks/Model_Training_With_Text.ipynb`

---

## ✅ Future Work

- Hyperparameter tuning (GridSearchCV, RandomizedSearchCV)
- Streamlit dashboard for real-time predictions
- Deploy model via Flask or FastAPI
- Use SHAP for model interpretability

---

## ✍️ Author

**Aameya Devansh**  
NIT Jamshedpur | CSE 2nd year Undergrad  
📫 adevansh123@gmail.com
=======


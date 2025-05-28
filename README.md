# 🧠 Income Prediction Using Census Data

A Machine Learning project that predicts whether an individual's income exceeds $50,000/year based on various demographic features from the Adult Census Income dataset. The project includes exploratory data analysis (EDA), model building, evaluation, and deployment using both Flask and Streamlit web applications.

---

## 🎯 Objective

The primary objective of the Census Income Predictor project is to build a machine learning model that accurately predicts whether an individual’s annual income exceeds $50,000 or not based on demographic and socio-economic attributes. This classification task helps in identifying income groups for policy-making, market segmentation, and economic research.

By analyzing data from the Adult Census dataset, the project aims to:

Understand the key factors influencing income levels such as education, occupation, and hours worked.

Apply data preprocessing and feature engineering techniques to clean and transform the data.

Train and evaluate various classification algorithms to select the best-performing model.

Deploy the final model through a user-friendly web interface using Flask and Streamlit, enabling real-time predictions for new user inputs.

Ultimately, this project demonstrates the practical application of data science—from data exploration and modeling to deployment—to solve a real-world classification problem in the domain of socio-economic analytics.
---

## 📦 Dataset Information

- **Dataset Name:** Adult Census Income
- **Source:** [OpenML](https://www.openml.org/d/1590)
- **Load using:**  
  ```python
  from sklearn.datasets import fetch_openml
  data = fetch_openml("adult", version=2, as_frame=True)
  ````

* **Target column:** `income`
* **Task type:** Binary Classification (`>50K` or `<=50K`)

---

## 📝 Assignment Instructions

1. **Fork this repository** to your GitHub account.
2. Perform **EDA** and **data preprocessing** in a Jupyter Notebook.
3. Build a **classification model**, evaluate its performance (accuracy, precision, recall, etc.).
4. **Save the trained model** using `pickle` or `joblib`.
5. Create a **Flask web app** that takes user input and displays the predicted income category.
6. Create a **Streamlit app** with the same functionality but using Streamlit widgets.
7. Update the `README.md` with:

   * Your project overview
   * Methodology
   * Live app links (Streamlit if possible)
   * Screenshots, etc.
9. Push all your files to your forked GitHub repo and **submit the GitHub repo link**.

---

## 📂 Folder Structure

```
income-predictor/
├── flask_app.py                # Flask app entry point
├── streamlit_app.py            # Streamlit app entry point
├── model/
│   └── model.pkl               # Trained and serialized model files
├── templates/
│   └── index.html              # HTML template for Flask form
├── static/                     # (Optional) Static files for Flask
├── notebook/
│   └── eda\_model.ipynb        # notebooks
├── requirements.txt            # List of Python dependencies
└── README.md                   # Updated with your project details
```

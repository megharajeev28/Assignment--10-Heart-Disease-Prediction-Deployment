# ❤️ Heart Disease Prediction using Machine Learning

An end-to-end Machine Learning project that predicts the likelihood of heart disease based on patient clinical parameters. The application is built using **Python, Flask, Scikit-learn**, and deployed on **Render** as a live web application.

---

# 👨‍🎓 Student Details

| Field | Details |
|--------|---------|
| **Name** | Megha Rajeev |
| **Registration Number** | 23MIM10047 |
| **Application Number** | IN26011193 |
| **Batch Number** | 1A |
| **Assignment Number** | Assignment - 10 |
| **Project Title** | Heart Disease Prediction using Machine Learning |
| **Email Address** | megha.23mim10047@vitbhopal.ac.in |

---

# 📌 Project Overview

This project demonstrates the complete Machine Learning deployment lifecycle by developing a Heart Disease Prediction system. A Random Forest Classifier is trained using patient clinical data and integrated into a Flask web application. The application provides an interactive web interface for users to enter patient details and receive predictions. It also exposes a REST API that accepts JSON input and returns predictions. The complete project is version-controlled using GitHub and deployed on Render for public access.

---

# 🎯 Objective

The objective of this project is to develop and deploy a machine learning model capable of predicting heart disease risk based on clinical parameters while demonstrating the fundamentals of MLOps, including model training, serialization, API development, version control, and cloud deployment.

---

# 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML5
- CSS3
- Git
- GitHub
- Render

---

# 📂 Dataset

**Dataset Name:** Heart Disease Prediction Dataset

**Source:**  
https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

---

# 🤖 Machine Learning Model

**Algorithm Used:** Random Forest Classifier

### Model Performance

| Metric | Value |
|---------|-------|
| Accuracy | **98.54%** |

The trained model is saved as:

```
model.pkl
```

---

# 📁 Repository Structure

```
Assignment--10-Heart-Disease-Prediction/
│
├── app.py
├── train_model.py
├── model.pkl
├── heart.csv
├── requirements.txt
├── Procfile
├── runtime.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

# ✨ Features

- Heart Disease Prediction using Machine Learning
- User-friendly Flask Web Interface
- REST API for JSON Predictions
- Responsive HTML & CSS Design
- Machine Learning Model Deployment
- Cloud Hosting using Render
- GitHub Version Control

---

# 🌐 Live Deployment

The application is successfully deployed on Render.

**Live Application:**  
https://assignment-10-heart-disease-prediction-1bgf.onrender.com/

---

# 🔗 GitHub Repository

Repository Link:

https://github.com/megharajeev28/Assignment--10-Heart-Disease-Prediction

---

# ⚙️ Installation Guide

## Clone the Repository

```bash
git clone https://github.com/megharajeev28/Assignment--10-Heart-Disease-Prediction.git
```

## Navigate to the Project Folder

```bash
cd Assignment--10-Heart-Disease-Prediction
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 🔌 REST API

### Endpoint

```
POST /predict
```

### Sample Request

```json
{
    "age": 63,
    "sex": 1,
    "cp": 3,
    "trestbps": 145,
    "chol": 233,
    "fbs": 1,
    "restecg": 0,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 2.3,
    "slope": 0,
    "ca": 0,
    "thal": 1
}
```

### Sample Response

```json
{
    "prediction": "Heart Disease Detected"
}
```

---

# 📈 Project Workflow

1. Load the Heart Disease dataset.
2. Perform data preprocessing and train-test split.
3. Train a Random Forest Classifier.
4. Evaluate the model using Accuracy Score.
5. Save the trained model using Joblib.
6. Develop a Flask web application.
7. Build a REST API for predictions.
8. Push the project to GitHub.
9. Deploy the application on Render.
10. Test the live web application and API.

---

# 🎓 Learning Outcomes

- Data preprocessing using Pandas
- Machine Learning model development
- Model serialization using Joblib
- Flask web application development
- REST API implementation
- Git and GitHub version control
- Cloud deployment using Render
- Understanding the fundamentals of MLOps

---

# 📝 Conclusion

This project successfully developed and deployed a Heart Disease Prediction system using a Random Forest Classifier. The model achieved an accuracy of **98.54%**, demonstrating strong predictive performance on the test dataset. The trained model was serialized using Joblib and integrated into a Flask web application that provides both a user-friendly interface and a REST API for real-time predictions. During deployment, challenges such as configuring project dependencies, resolving Git merge conflicts, and deploying the application on Render were successfully addressed. This project highlights the importance of MLOps practices, including version control with GitHub, model serialization, dependency management, API development, and cloud deployment. These practices enable machine learning models to be transformed into reliable, scalable, and production-ready applications.

---

# 👩‍💻 Author

**Megha Rajeev**

Integrated M.Tech in Artificial Intelligence

VIT Bhopal University

**GitHub:** https://github.com/megharajeev28

---

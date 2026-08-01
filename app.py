from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# Website Prediction
# ==========================
@app.route("/predict_form", methods=["POST"])
def predict_form():

    features = [
        float(request.form["age"]),
        float(request.form["sex"]),
        float(request.form["cp"]),
        float(request.form["trestbps"]),
        float(request.form["chol"]),
        float(request.form["fbs"]),
        float(request.form["restecg"]),
        float(request.form["thalach"]),
        float(request.form["exang"]),
        float(request.form["oldpeak"]),
        float(request.form["slope"]),
        float(request.form["ca"]),
        float(request.form["thal"])
    ]

    prediction = model.predict([features])[0]

    if prediction == 1:
        result = "❤️ Heart Disease Detected"
    else:
        result = "💚 No Heart Disease"

    return render_template("index.html", prediction=result)


# ==========================
# REST API
# ==========================
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    features = np.array([[
        data["age"],
        data["sex"],
        data["cp"],
        data["trestbps"],
        data["chol"],
        data["fbs"],
        data["restecg"],
        data["thalach"],
        data["exang"],
        data["oldpeak"],
        data["slope"],
        data["ca"],
        data["thal"]
    ]])

    prediction = model.predict(features)[0]

    if prediction == 1:
        result = "Heart Disease Detected"
    else:
        result = "No Heart Disease"

    return jsonify({
        "prediction": result
    })


if __name__ == "__main__":
    app.run(debug=True)
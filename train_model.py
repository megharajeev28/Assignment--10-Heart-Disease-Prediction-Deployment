import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ==============================
# Load Dataset
# ==============================
df = pd.read_csv("heart.csv")

print("=" * 50)
print("First Five Records")
print("=" * 50)
print(df.head())

# ==============================
# Numerical Features
# ==============================
print("\n" + "=" * 50)
print("Numerical Features")
print("=" * 50)

numerical_features = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

print(numerical_features)

# ==============================
# Target Variable
# ==============================
target = "target"

print("\nTarget Variable:")
print(target)

# ==============================
# Missing Values
# ==============================
print("\n" + "=" * 50)
print("Missing Values")
print("=" * 50)

print(df.isnull().sum())

# ==============================
# Feature Selection
# ==============================
X = df.drop("target", axis=1)
y = df["target"]

# ==============================
# Train Test Split
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples :", X_train.shape[0])
print("Testing Samples  :", X_test.shape[0])

# ==============================
# Model
# ==============================
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ==============================
# Prediction
# ==============================
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 50)
print("Model Accuracy")
print("=" * 50)

print(f"Accuracy : {accuracy:.4f}")

# ==============================
# Save Model
# ==============================
joblib.dump(model, "model.pkl")

print("\nModel saved successfully as model.pkl")
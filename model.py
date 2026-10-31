
import numpy as np
import pandas as pd

import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

from config import DATA_PATH, FEATURES, TARGET


# =====================================================
# 1. LOAD DATASET
# =====================================================

@st.cache_data
def load_data(file_path, modified_time):
    return pd.read_csv(file_path)


# =====================================================
# 2. TRAIN MACHINE LEARNING MODEL
# =====================================================

@st.cache_resource
def train_model(file_path, modified_time):

    data = load_data(file_path, modified_time)

    required = FEATURES + [TARGET]

    missing = set(required) - set(data.columns)

    if missing:
        raise ValueError(
            f"Dataset is missing columns: {sorted(missing)}"
        )

    # Preserve student names if available
    display_columns = required.copy()

    if "student_name" in data.columns:
        display_columns.append("student_name")

    data = data[display_columns].copy()

    # Convert only numerical ML columns
    for column in required:
        data[column] = pd.to_numeric(
            data[column], errors="coerce"
        )

    # Remove invalid numerical records
    data = data.dropna(subset=required)

    if len(data) < 10:
        raise ValueError(
            "Please provide at least 10 valid student records."
        )

    if not np.isfinite(
        data[required].to_numpy()
    ).all():
        raise ValueError(
            "Dataset contains invalid numeric values."
        )

    # Validate marks and attendance
    for column in [
        TARGET,
        "attendance",
        "previous_marks",
        "assignments_score"
    ]:

        if not data[column].between(0, 100).all():
            raise ValueError(
                f"{column} must contain values between 0 and 100."
            )

    # =================================================
    # 3. PREPARE FEATURES AND TARGET
    # =================================================

    X = data[FEATURES]
    y = data[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # =================================================
    # 4. MODEL EVALUATION
    # =================================================

    evaluation_model = LinearRegression()

    evaluation_model.fit(X_train, y_train)

    predictions = evaluation_model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    r2 = r2_score(y_test, predictions)

    # =================================================
    # 5. TRAIN FINAL MODEL
    # =================================================

    final_model = LinearRegression()

    final_model.fit(X, y)

    # Return data WITH student names
    return data, final_model, mae, r2, len(X_test)


# =====================================================
# 6. PREDICT STUDENT FINAL MARKS
# =====================================================

def predict_marks(model, student_input):

    prediction = float(
        model.predict(student_input[FEATURES])[0]
    )

    return float(np.clip(prediction, 0, 100))
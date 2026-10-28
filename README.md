# 🎓 AI Student Learning System

An AI-powered student performance prediction and personalized learning system that analyzes student academic data, predicts performance, visualizes results, and provides personalized learning recommendations.

## 📌 Project Overview

The **AI Student Learning System** aims to help students understand their academic performance and identify areas for improvement. It uses machine learning to analyze student data and generate predictions, visualizations, and personalized study plans.

## ✨ Features

* 📊 **Student Performance Prediction** — Predict academic performance using a trained machine learning model.
* 📈 **Performance Visualization** — Display academic performance through charts and graphs.
* 🎯 **Personalized Recommendations** — Suggest learning strategies based on student performance.
* 📚 **Daily Study Plan** — Generate a structured study plan to improve learning outcomes.
* 🧠 **Machine Learning Evaluation** — Evaluate model performance using MAE and R² metrics.
* 🖥️ **Interactive Dashboard** — Provide a user-friendly interface for entering student information and viewing results.
* 🎨 **Custom Styling** — Maintain a consistent interface with organized layouts, colors, and fonts.

## 🗂️ Project Structure

```text
AI-Student-Learning-System/
│
├── app.py                  # Main application and dashboard
├── styles.py               # Application styling and UI design
├── model.py                # Model training and predictions
├── charts.py               # Charts and performance visualizations
├── recommendations.py      # Learning recommendations and study plans
├── config.py               # Configuration and model settings
│
├── data/
│   └── student_data.csv    # Student dataset
│
└── requirements.txt        # Project dependencies (if included)
```

## 🛠️ Technologies Used

* **Python** — Core programming language
* **Pandas** — Data processing and analysis
* **NumPy** — Numerical computations
* **Scikit-learn** — Machine learning and model evaluation
* **Streamlit** — Interactive web application interface, if used in `app.py`
* **Plotly / Matplotlib** — Data visualization, depending on the chart library used

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/vats070/AI_Student_Learning_System.git
```

### 2. Navigate to the project directory

```bash
cd AI-Student-Learning-System
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 4. Install dependencies

If your project includes a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install the packages required by your application and create a `requirements.txt` file.

### 5. Run the application

If the project uses Streamlit:

```bash
streamlit run app.py
```

If it uses another framework, run `app.py` using the appropriate command for that framework.

## 📊 Model Evaluation

The system uses machine learning evaluation metrics to assess prediction quality:

* **MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted values.
* **R² Score:** Measures how well the model explains variation in the target variable.

The model is trained using the configured student dataset and feature columns.

## 🎯 Expected Outcomes

* Better understanding of student academic performance.
* Identification of subjects or skills that need improvement.
* Data-driven learning recommendations.
* Structured daily study plans.
* Clear visual summaries of academic results.

## 🚀 Future Improvements

* Add student login and profile management.
* Store student prediction history.
* Improve model accuracy through feature engineering and model comparison.
* Add downloadable performance reports.
* Introduce subject-specific learning resources.
* Deploy the application online for wider access.


---

⭐ If you find this project useful, consider giving the repository a star!

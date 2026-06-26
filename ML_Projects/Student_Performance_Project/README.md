# Student Math Score Prediction System

A complete end-to-end machine learning project that predicts a student's math score based on academic, demographic, and socioeconomic factors — served through a Flask web app with a clean dark-themed UI.

---

## Live Demo

> Run locally using the steps below. A live deployment link will be added here once hosted.

---

## Project Structure

```
Student Performance projec/
├── models/
│   ├── ridge.pkl                    # Trained Ridge Regression model
│   └── scaler.pkl                   # Fitted StandardScaler
├── notebooks/
│   ├── StudentsPerformance.csv      # Raw dataset (1,000 records)
│   └── Student_Performance.ipynb   # EDA, preprocessing, training & visualizations
├── templates/
│   ├── index.html                   # Landing page
│   └── home.html                    # Prediction form & result display
├── application.py                   # Flask app entry point
└── README.md
```

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.11 |
| Machine Learning | scikit-learn (Ridge Regression, StandardScaler) |
| Data & EDA | Pandas, NumPy, Matplotlib, Seaborn |
| Notebook | Jupyter Notebook |
| Web Framework | Flask, Jinja2 |
| Frontend | HTML5, CSS3 (custom dark theme) |

---

## Dataset

- **Source:** Students Performance in Exams (Kaggle)
- **Records:** 1,000 students
- **Target:** Math score (0–100)
- **Features:**

| Feature | Type | Values |
|---|---|---|
| Gender | Categorical | Male / Female |
| Race / Ethnicity | Categorical | Group A, B, C, D, E |
| Parental Level of Education | Ordinal | Some High School → Master's Degree |
| Lunch Program | Categorical | Standard / Free or Reduced |
| Test Preparation Course | Categorical | None / Completed |
| Reading Score | Numeric | 0–100 |
| Writing Score | Numeric | 0–100 |

---

## ML Pipeline

### 1. Preprocessing
| Feature | Encoding |
|---|---|
| Gender | Binary (`0` = Male, `1` = Female) |
| Race / Ethnicity | One-Hot Encoding → 5 columns (Group A–E) |
| Parental Education | Ordinal (`0` = Some High School → `5` = Master's Degree) |
| Lunch | Binary (`0` = Standard, `1` = Free/Reduced) |
| Test Prep | Binary (`0` = None, `1` = Completed) |
| Reading & Writing Score | Continuous — passed through as-is |

All 11 features are normalized using `StandardScaler` before model input.

### 2. Models Compared

| Model | R² Score | MAE | MSE |
|---|---|---|---|
| Linear Regression | 0.8793 | 4.25 | 29.37 |
| **Ridge Regression** | **0.8796** | **4.24** | **29.29** |
| Lasso Regression | 0.8498 | 4.71 | 36.55 |

**Ridge Regression** was selected — highest R² and lowest error across all metrics.

Train/test split: **80/20**, `random_state=42`

---

## Visualizations

The notebook includes 11 charts for full EDA and model evaluation:

**Exploratory Data Analysis**
- Score distributions (Math, Reading, Writing)
- Math score by gender — violin + box plot
- Math score by race/ethnicity — box plot + average bar chart
- Math score by parental education level
- Socioeconomic factors (lunch type & test prep) vs math score
- Feature correlation heatmap
- Pairplot of all three scores by gender

**Model Evaluation**
- Model comparison bar chart (R², MAE, MSE)
- Actual vs Predicted scatter plots — all 3 models
- Ridge residuals vs predicted + residual distribution
- Ridge feature coefficients (importance)

---

## How to Run

### Prerequisites

Python 3.11 from [python.org](https://www.python.org/downloads/)

```bash
python --version
```

### 1. Install Dependencies

```bash
pip install flask scikit-learn pandas numpy matplotlib seaborn
```

> **Windows users with multiple Python installations:** use the `py` launcher to target the right version:
> ```bash
> py -3.11 -m pip install flask scikit-learn pandas numpy matplotlib seaborn
> ```

### 2. Start the Flask Server

```bash
python application.py
```

You should see:
```
* Running on http://127.0.0.1:5000
* Running on http://0.0.0.0:5000
```

### 3. Open in Browser

| Page | URL |
|---|---|
| Home | http://127.0.0.1:5000/ |
| Predict | http://127.0.0.1:5000/predictdata |

Press `Ctrl + C` to stop the server.

---

## Troubleshooting

**`ModuleNotFoundError: No module named 'flask'`**
The packages aren't installed for the Python version running the app. Use `py -3.11 -m pip install flask scikit-learn pandas numpy` to target the correct interpreter.

**SSL errors during pip install (`CERTIFICATE_VERIFY_FAILED`)**
Caused by MinGW/MSYS2 Python builds. Switch to the official Windows Python from [python.org](https://www.python.org/downloads/).

**Port 5000 already in use**
Change the port in `application.py`:
```python
app.run(host="0.0.0.0", port=5001)
```

---

## Author

**Parth Mahale**

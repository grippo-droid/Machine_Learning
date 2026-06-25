# Student Marks Prediction System

A machine learning-powered web application that predicts a student's math score based on academic, demographic, and socioeconomic indicators.

The project covers a complete ML workflow — from exploratory data analysis and model training in a Jupyter Notebook, to serving predictions through a Flask web app with a dark-themed UI.

---

## Project Structure

```
Student Performance projec/
├── models/
│   ├── ridge.pkl               # Trained Ridge Regression model
│   └── scaler.pkl              # Fitted StandardScaler
├── notebooks/
│   ├── StudentsPerformance.csv # Raw student dataset (1,000 records)
│   └── Untitled9.ipynb         # Data preprocessing & model training
├── templates/
│   ├── index.html              # Landing page
│   └── home.html               # Prediction form & result display
├── application.py              # Flask application entry point
├── oldapplication.py           # Previous version (kept for reference)
└── README.md
```

---

## Tech Stack

| Layer | Tools |
|---|---|
| Machine Learning | Scikit-Learn (Ridge Regression, StandardScaler) |
| Data | Pandas, NumPy, Jupyter Notebook |
| Web | Flask, Jinja2, HTML5/CSS3 |

---

## How to Run

### Prerequisites

Make sure you have **Python 3.11** installed from [python.org](https://www.python.org/downloads/).
You can verify with:

```bash
python --version
```

### 1. Install Dependencies

Open a terminal in the project folder and run:

```bash
pip install Flask scikit-learn pandas numpy
```

> **Note for Windows users with multiple Python installations:**
> If `python` points to the wrong interpreter (e.g., an MSYS2/MinGW Python), use the full path or the `py` launcher:
> ```bash
> py -3.11 -m pip install Flask scikit-learn pandas numpy
> ```

### 2. Start the Flask Server

```bash
python application.py
```

Or with `py` launcher:

```bash
py -3.11 application.py
```

You should see output like:

```
* Running on http://127.0.0.1:5000
* Running on http://0.0.0.0:5000
```

### 3. Open in Browser

| Page | URL |
|---|---|
| Landing page | http://127.0.0.1:5000/ |
| Prediction form | http://127.0.0.1:5000/predictdata |

To stop the server, press `Ctrl + C` in the terminal.

---

## Common Issues

**`ModuleNotFoundError: No module named 'flask'`**
The packages are not installed for the Python version being used. Run `pip install Flask scikit-learn pandas numpy` using the same Python that will run the app. If you have multiple Pythons, prefer `py -3.11 -m pip install ...`.

**SSL errors during pip install (e.g. `CERTIFICATE_VERIFY_FAILED`)**
This happens with MinGW/MSYS2 Python builds. Use the official Windows Python from [python.org](https://www.python.org/downloads/) instead.

**Port 5000 already in use**
Another process is occupying the port. Either stop that process or change the port in `application.py`:
```python
app.run(host="0.0.0.0", port=5001)
```

---

## Model & Feature Details

The Ridge Regression model expects 11 features after preprocessing:

| # | Feature | Encoding |
|---|---|---|
| 1 | Gender | `0` = Male, `1` = Female |
| 2 | Parental education | `0` (Some High School) → `5` (Master's Degree) |
| 3 | Lunch type | `0` = Standard, `1` = Free/Reduced |
| 4 | Test prep course | `0` = None, `1` = Completed |
| 5 | Reading score | Continuous (0–100) |
| 6 | Writing score | Continuous (0–100) |
| 7–11 | Race/Ethnicity | One-hot encoded: Group A, B, C, D, E |

All features are normalized using `StandardScaler` before being passed to the model.

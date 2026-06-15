# 🎓 Student Marks Prediction System

A machine learning-powered web application that predicts student math scores based on academic, demographic, and socioeconomic indicators. 

---

## 📁 Project Structure

```text
Student_Marks_Prediction/
├── artifacts/
│   ├── ridge.pkl              # Trained Ridge Regression model
│   └── scaler.pkl             # Fitted StandardScaler object
├── notebook/
│   ├── StudentsPerformance.csv # Raw student dataset
│   └── Untitled9.ipynb        # Data preprocessing & model training pipeline
├── templates/
│   ├── index.html             # Basic landing page
│   └── home.html              # Interactive score prediction form
├── static/                    # Static UI assets (CSS/JS)
├── src/                       # Source code scripts
├── .gitignore                 # Files excluded from git
├── app.py                     # Flask application entry point
├── requirements.txt           # Python package dependencies
└── README.md                  # Project documentation
```

---

## 🛠️ Tech Stack

- **Machine Learning & Data Science:** Python, Scikit-Learn, Pandas, NumPy, Jupyter Notebook
- **Web Development:** Flask (Python web framework), HTML5, Jinja2 template engine

---

## 🚀 Setup & Execution

### 1. Set Up a Virtual Environment
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the Web Server
```bash
python app.py
```
Open your browser and navigate to: **`http://127.0.0.1:5000/predictdata`**

---

## 🧠 Model & Feature Mappings

The Ridge regression model expects 11 scaled features:
1. **Gender:** Male (0) / Female (1)
2. **Parental level of education:** Rank-mapped from Some High School (0) to Master's (5)
3. **Lunch:** Standard (0) / Free/Reduced (1)
4. **Test preparation course:** None (0) / Completed (1)
5. **Reading score:** Continuous test score
6. **Writing score:** Continuous test score
7. **Race/Ethnicity Groups A-E:** One-hot encoded binary columns

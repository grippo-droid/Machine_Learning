# Algerian Forest Fires - Fire Weather Index (FWI) Prediction App

> **Note:** Backend is hosted on Render's free tier, which spins down after periods of inactivity. The first request may take 30-60 seconds to load while the server wakes up. Subsequent requests will be fast.

An end-to-end Machine Learning web application built using Python, Flask, and Scikit-Learn to predict the **Fire Weather Index (FWI)**. The FWI is a core component of the Canadian Forest Fire Weather Index System, which evaluates fire danger based on meteorological observations.

This project utilizes historical forest fire data from two regions in Algeria: **Bejaia** (North-East) and **Sidi-Bel Abbes** (North-West).

---

## 📂 Project Structure

```text
├── models/
│   ├── ridge.pkl          # Serialized Ridge Regression model
│   └── scaler.pkl         # Serialized StandardScaler object for inputs preprocessing
├── notebooks/
│   ├── Algerian_forest_fires_dataset_UPDATE.csv   # The historical dataset
│   ├── 2.0-EDA And FE Algerian Forest Fires.ipynb  # Exploratory Data Analysis & Feature Engineering
│   └── 3.0-Model Training.ipynb                   # Model selection, validation, and training
├── templates/
│   ├── index.html         # Homepage welcome page template
│   └── home.html          # Web form template for predicting FWI
├── venv/                  # Python Virtual Environment
├── application.py         # Main Flask application file for running the server
└── README.md              # Project documentation
```

---

## 📊 Dataset & Features Info

The predictive model accepts **9 distinct feature inputs** representing weather conditions and fire weather indicators:

| Feature Name | Type | Description |
| :--- | :--- | :--- |
| **Temperature** | `float` | Noon Temperature (in Celsius, range: 22°C to 42°C) |
| **RH** | `float` | Relative Humidity (in %, range: 21% to 90%) |
| **Ws** | `float` | Wind Speed (in km/h, range: 6 to 29 km/h) |
| **Rain** | `float` | Daily rainfall (in mm, range: 0 to 16.8 mm) |
| **FFMC** | `float` | Fine Fuel Moisture Code (moisture content of litter; range: 28.6 to 92.5) |
| **DMC** | `float` | Duff Moisture Code (moisture content of loosely compacted organic layers; range: 1.1 to 65.9) |
| **ISI** | `float` | Initial Spread Index (expected rate of fire spread; range: 0.0 to 22.0) |
| **Classes** | `float` | Fire risk status (`1.0` for Fire, `0.0` for Not Fire) |
| **Region** | `float` | Geographic Region index (`0.0` for Bejaia, `1.0` for Sidi-Bel Abbes) |

The target output is **FWI (Fire Weather Index)**, a continuous numerical rating of fire intensity.

---

## 🛠️ Machine Learning Pipeline

1. **Exploratory Data Analysis (EDA) & Feature Engineering**:
   * Removed extraneous headers and standardized column spaces.
   * Addressed missing values and cleaned records.
   * Mapped categorical regions to numerical representations.
   * Handled outlier removal and feature correlation analysis.
2. **Model Training**:
   * Features normalized using `StandardScaler` to ensure balanced regression coefficients.
   * Explored Linear Regression, Lasso, Ridge, and ElasticNet models.
   * Selected the **Ridge Regression** model due to its robustness against multi-collinearity.
   * Serialized the model and scaler using Python's `pickle` module.

---

## 🚀 How to Run the Project

Follow these steps to run the application locally on your machine.

### Prerequisites
Make sure you have **Python 3.8+** installed.

### 1. Clone or Open the Directory
Open your terminal/command prompt and navigate into the project workspace root:
```bash
cd "E:\LETS COOK\Machine Learning\End to end project implementation"
```

### 2. Set Up Virtual Environment
If you don't have the virtual environment configured, create it:
```bash
python -m venv venv
```

Activate the virtual environment:
*   **Windows (PowerShell)**:
    ```powershell
    .\venv\Scripts\Activate.ps1
    ```
*   **Windows (Command Prompt)**:
    ```cmd
    .\venv\Scripts\activate.bat
    ```
*   **macOS / Linux**:
    ```bash
    source venv/bin/activate
    ```

### 3. Install Dependencies
Install all required libraries using standard `pip`:
```bash
pip install flask numpy pandas scikit-learn
```

> [!TIP]
> If you experience slow downloads or connection timeout errors, use a mirror:
> ```bash
> pip install --index-url https://pypi.tuna.tsinghua.edu.cn/simple flask numpy pandas scikit-learn
> ```

### 4. Run the Web Server
Launch the Flask development server:
```bash
python application.py
```

Upon successful startup, the console will output:
```text
 * Serving Flask app 'application'
 * Running on http://127.0.0.1:5000
```

### 5. Access the Web Application
Open your web browser and navigate to:
*   **Homepage**: [http://127.0.0.1:5000](http://127.0.0.1:5000)
*   **Prediction Interface**: [http://127.0.0.1:5000/predictdata](http://127.0.0.1:5000/predictdata)

---

## 🧪 Example Test Case
To verify the model prediction, open the `/predictdata` page and enter the following values:
*   **Temperature**: `30`
*   **RH**: `50`
*   **Ws**: `15`
*   **Rain**: `0`
*   **FFMC**: `85`
*   **DMC**: `12`
*   **ISI**: `5`
*   **Classes**: `1`
*   **Region**: `1`

Click **Predict**. The application will return a predicted FWI value of approximately **`6.35`**.

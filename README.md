# 🛡️ Predictive_Transaction_Intelligence_using_for_BFSI

A **FastAPI-based backend system** that detects fraudulent financial transactions using **Machine Learning**, **Rule-Based Logic**, and **LLM (Google Gemini) Explainability**.  
Designed as a **production-ready fintech backend** with alerts, explainable AI, and database persistence.

---

## 🚀 Features

- 🔍 **ML-Based Fraud Prediction**
- 📏 **Rule-Based Fraud Detection**
- 🧠 **LLM Explainability (Google Gemini)**
- 🚨 **Fraud Alert System**
- 🗄️ **SQLite Database**
- 📊 **Model Metrics Tracking**
- ⚡ **FastAPI REST APIs**

---

## 🧩 Tech Stack

| Layer | Technology |
|------|------------|
Backend API | FastAPI
ML Model | Scikit-learn (RandomForest)
Database | SQLite
LLM | Google Gemini API
Data Processing | Pandas, NumPy
Model Storage | Joblib
Environment Config | python-dotenv
Testing | Postman
Graph | Matplotlib, Seaborn
---

## 📂 Project Structure
predictive-transaction-backend/
│── main.py
│── .env
│── README.md
│
├── data/
│ ├── raw/
│ └── processed/
│ └── transactions_processed.csv
│
├── src/
│ ├── api/
│ │ └── predict.py
│ │
│ ├── ml/
│ │ ├── train_model.py
│ │ ├── fraud_model.pkl
│ │ ├── scaler.pkl
│ │ └── metrics.json
│ │
│ ├── rules/
│ │ └── rule_engine.py
│ │
│ ├── llm/
│ │ └── gemini_client.py
│ │
│ └── database/
│ ├── init_db.py
│ └── transactions.db
│
└── requirements.txt

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd predictive-transaction-backend
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

Windows
```bash
venv\Scripts\activate
```

Linux / macOS
```bash
source venv/bin/activate
```

### 4️⃣ Upgrade pip (Recommended)
```bash
python -m pip install --upgrade pip
```
### 5️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 6️⃣ Create .env File
```bash
echo GOOGLE_API_KEY=your_gemini_api_key_here > .env
```

⚠️ Replace your_gemini_api_key_here with your actual Gemini API key.

🗄️ Database Setup
### 7️⃣ Initialize Database
```bash
python src/database/init_db.py
```

This creates:

-- transactions table
-- fraud_alerts table

📊 Data Preprocessing Pipeline
8️⃣ Run Data Cleaning Pipeline
python src/preprocessing/cleaning_pipeline.py

9️⃣ Train-Test Split
python src/preprocessing/train_test_split.py


Creates:

train.csv

test.csv

🤖 Machine Learning Model Training
🔟 Train Fraud Detection Model
python src/ml/train_model.py


Generates:

src/ml/fraud_model.pkl

src/ml/scaler.pkl

src/ml/metrics.json

▶️ Running the Backend Server
1️⃣ Start FastAPI Server
uvicorn main:app --reload

🌐 Access API
Backend Server
```bash
http://127.0.0.1:8000
```

🧪 Testing APIs (Postman)
```bash
Predict Transaction (POST)
POST http://127.0.0.1:8000/api/predict

Fetch Transactions (GET)
http://127.0.0.1:8000/api/transactions

Fetch Model Performance Metrics (GET)
http://127.0.0.1:8000/api/metrics

Fetch all alert messages
http://127.0.0.1:8000/api/alert

```

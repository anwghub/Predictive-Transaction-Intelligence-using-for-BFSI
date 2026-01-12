# 🛡️ Predictive Transaction Intelligence for BFSI

A **scalable, explainable fraud detection system** designed for the Banking, Financial Services, and Insurance (BFSI) domain.  
This system combines **Machine Learning**, **Rule-Based Intelligence**, and **LLM-powered Explainability** to detect fraudulent transactions in real time while ensuring transparency and compliance. This project focuses on developing an AI-driven system that utilizes Large Language Models (LLMs) to analyse historical customer transaction patterns and behavioral data in order to predict future transactions and assess fraud risks in real time. By identifying anomalies and learning fraud indicators from previous data, this solution will help financial institutions enhance transaction security, improve fraud detection, and optimize risk management—without disrupting customer experience.

---

## 📌 Problem Statement

Traditional fraud detection systems often act as **black boxes**, making it difficult for banks to justify why a transaction was flagged.  
This project addresses that gap by:
- Detecting fraud in real time
- Providing **human-readable explanations**
- Supporting **auditability and compliance**

---

## 🚀 Key Features

- 🔍 Real-time fraud prediction using Machine Learning
- 🧠 Rule-based validation for high-risk patterns
- 🤖 LLM-based explainability using **Google Gemini**
- 🔐 Secure authentication (Login, Register, Forgot & Reset Password)
- 📊 Transaction monitoring and analytics
- 🧾 Historical transaction logs for auditing
- 🌐 RESTful APIs for system integration
- 🐳 Dockerized deployment with Nginx reverse proxy

---

## 🧱 Tech Stack

### Frontend
- React.js
- Chart.js (Interactive visualizations)

### Backend
- FastAPI (High-performance Python backend)
- Uvicorn + Gunicorn
- Nginx (Reverse Proxy)

### Machine Learning & Data
- Scikit-learn (Random Forest)
- Pandas, NumPy
- Joblib (Model serialization)

### AI Explainability
- Google Gemini API (LLM reasoning)

### Database
- SQlite3 (Transaction & user data)

### DevOps & Tools
- Docker & Docker Compose
- Postman (API testing)
- python-dotenv (Environment management)

---

## 🧠 Feature Engineering & Preprocessing

### Feature Extraction Techniques
- Transaction amount normalization
- Transaction frequency analysis
- Time-based features (hour, day, weekend flag)
- Location-based risk indicators
- User behavior profiling
- KYC consistency checks

### Data Preprocessing Steps
- Missing value handling
- Categorical encoding
- Feature scaling (StandardScaler)
- Outlier detection
- Train-test split
- Class imbalance handling

---

## 🔄 System Architecture & Data Flow

### Data Flow Pipeline

1. **Data Input**
   - User submits transaction details via frontend

2. **Backend Processing**
   - FastAPI validates request schema
   - Data cleaned and preprocessed using Pandas & NumPy

3. **Fraud Intelligence**
   - Random Forest model predicts fraud probability

4. **Explainability Layer**
   - Gemini LLM generates natural-language explanations

5. **Persistence & Monitoring**
   - Results stored in MongoDB
   - Transactions available for auditing and analytics

---

## 🧪 Machine Learning Model

- Algorithm: **Random Forest Classifier**
- Reason for selection:
  - High accuracy
  - Handles non-linear relationships
  - Robust to noisy data
- Model stored using **Joblib**
- Supports probability-based fraud scoring

---

## 🤖 Explainable AI (XAI)

For every flagged transaction:
- Model output is passed to Gemini LLM
- LLM generates:
  - Fraud reasoning
  - Risk factors
  - Actionable insights
- Ensures transparency for compliance teams

---

## 🔐 Authentication & Security

- User Registration & Login
- JWT-based authentication
- Forgot Password & Reset Password flow
- Role-based API protection
- Secure environment variables

---

## 🛣️ RESTful API Endpoints

### Authentication
| Method | Endpoint | Description |
|------|--------|------------|
| POST | `/api/register` | User registration |
| POST | `/api/login` | User login |
| POST | `/api/forgot-password` | Password reset request |
| POST | `/api/reset-password` | Reset password |

### Fraud Detection
| Method | Endpoint | Description |
|------|--------|------------|
| POST | `/api/predict` | Fraud probability prediction & LLM explanation |
| GET | `/api/feedback` | user feedback |
| GET | `/api/transactions` | Transaction history |

---

## 🧪 Postman Testing

- Complete Postman collection included
- Covers:
  - Authentication flows
  - Fraud prediction
  - Explainability responses
  - Transaction history
- Useful for demo and API validation

---

## 🐳 Docker Deployment

### Services
- FastAPI app (Gunicorn + Uvicorn)
- Nginx reverse proxy


### Run with Docker Compose
```bash
docker-compose up --build
```

### 📈 Project Milestones
Milestone 1: Foundation & Data Setup

- Dataset preprocessing

- Database schema design

- Environment configuration

Milestone 2: ML Intelligence

- Feature engineering

- Random Forest training

- Model evaluation and tuning

Milestone 3: Explainability

- Rule-based fraud detection

- Gemini API integration

- Natural language reasoning

Milestone 4: Integration & Deployment

- Frontend-backend integration

- Authentication & analytics

- Dockerization and deployment readiness

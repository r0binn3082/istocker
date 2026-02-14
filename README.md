# IStocker

A web-based financial forecasting and risk profiling platform for EGX market analytics.

IStocker combines time-series modeling, machine learning forecasting, and personalized risk assessment into a modular, scalable web architecture.

---

## 🏗 Architecture Overview

IStocker follows a layered web architecture:

Presentation Layer → API Layer → Business Logic → ML Engine → Infrastructure → Data Storage

This separation ensures:

- Clear responsibility boundaries  
- Scalability  
- Maintainability  
- Production-readiness  
- Time-series discipline  

---

## 📂 Project Structure


---

## 🖥 Presentation Layer (`presentation/`)

Frontend interface built with HTML, CSS, and JavaScript.

Includes:

- Modular CSS structure
- Component-based styling
- API client layer
- Arabic / English localization
- Financial dashboard UI

This layer communicates exclusively with the API layer.

---

## 🌐 API Layer (`api/`)

Handles:

- HTTP routing
- Request validation
- Data serialization
- Response formatting

The API layer does not contain financial logic.  
It delegates all processing to the business layer.

---

## 🧠 Business Layer (`business/`)

Core domain logic including:

- Market processing
- Risk assessment
- User classification
- Recommendation engine
- Decision orchestration pipeline

This layer enforces financial rules and system decisions but does not directly access the database.

---

## 🤖 ML Engine (`ml/`)

Machine learning subsystem responsible for:

- Model training
- Hyperparameter configuration
- Backtesting
- Evaluation metrics
- Inference
- Confidence scoring

Model artifacts are stored in:


---

## 🗄 Infrastructure Layer (`infrastructure/`)

Handles system-level integrations such as:

- Database connection
- Repository pattern
- External APIs

This is the only layer that communicates directly with the database.

---

## 📊 Data Layer (`data/`)

Storage-only layer.

Contains:

- Raw and processed market data
- ML datasets
- Metadata
- System logs
- User storage

No business logic exists inside this folder.

---

## 🔬 Research (`research/`)

Contains:

- Exploratory Data Analysis (EDA)
- Experimental notebooks
- Hypothesis testing

Not part of runtime system.

---

## ⚙ Configuration (`config/`)

Centralized configuration files:

- Constants
- Paths
- Environment settings

Ensures configurable and environment-safe deployment.

---

## 🧪 Testing (`tests/`)

Automated tests for:

- Data pipeline validation
- Recommendation engine logic
- Risk assessment consistency

---

## 🚀 Features

- EGX30 time-series forecasting  
- Machine learning-driven predictions  
- Risk-based recommendation engine  
- Bilingual user interface  
- Modular layered architecture  
- Scalable backend design  

---

## 🛠 Setup Instructions

### 1️⃣ Create Conda Environment

```bash
conda env create -f environment.yml

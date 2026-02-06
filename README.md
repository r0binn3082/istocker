# iStocker – AI-Based Investment Decision Support System

## 📌 Project Overview
iStocker is an **AI-based decision support system** designed to help **retail (beginner) investors** in the Egyptian stock market make more informed investment decisions.

The system provides investment recommendations based on:
- User risk profiling
- Market data analysis
- Machine learning predictions (as a supporting signal)

⚠️ This project is **not a trading system** and does not guarantee profits.  
It is an educational decision-support tool.

---

## 🧠 System Architecture
The system follows a:
- **Layered Architecture**
- With **Feature-Based Organization** inside each layer

### Main Layers:
1. **Presentation Layer** – User Interface (HTML / CSS / JavaScript)
2. **Business Layer** – Core decision logic
3. **Data Layer** – Data storage and access
4. **Machine Learning Layer** – Model training, evaluation, and inference

**Goal:**  
Clear separation of concerns, maintainability, and scalability.

---

## 📁 Project Structure
The project is organized into clearly defined layers.  
Each folder has **one responsibility only**.

## 1. Data Layer (`data/`)
This layer is responsible for **all data preparation activities** before any model training.


### `raw/`
- Contains raw, unmodified data
- Data sources may include APIs, CSV files, or databases
- **No changes are allowed** in this folder

**Purpose:**  
Single source of truth for original data

---

### `preprocessing/`
- Data cleaning and basic preparation
- Examples:
  - Handling missing values
  - Type conversion
  - Scaling and normalization
  - Encoding categorical variables

**Purpose:**  
Make the data usable (not analytical)

---

### `eda/`
- Exploratory Data Analysis
- Used to understand:
  - Distributions
  - Correlations
  - Outliers
  - Trends and anomalies
- Typically contains notebooks and analysis reports

**Purpose:**  
Understand the data before modeling  
**Note:** EDA is not used during runtime

---

### `feature_engineering/`
- Creation of new features from existing data
- Examples:
  - Lag features
  - Rolling statistics
  - Technical indicators

**Purpose:**  
Enrich the dataset with meaningful signals

---

### `feature_selection/`
- Selecting the most relevant features
- Reducing noise and dimensionality
- Preventing overfitting

**Purpose:**  
Decide which features will be used by the model

---

### `datasets/`
- Final datasets after preprocessing, engineering, and selection
- These datasets are the **only inputs** to the AI models

**Purpose:**  
Provide clean and ready-to-use data for training and inference

---

## 2. AI Layer (`ml/`)
This layer contains everything related to machine learning models.


### `training/`
- Model training scripts
- Experiments and hyperparameter tuning

**Purpose:**  
Teach the model using prepared datasets

---

### `models/`
- Saved trained models
- Serialized artifacts (e.g., `.pkl`, `.joblib`)

**Purpose:**  
Store trained models for reuse

---

### `inference/`
- Loading trained models
- Generating predictions using new data

**Purpose:**  
Use the trained model (no training happens here)

---

## 3. Business Layer (`business/`)
This layer contains the **system logic**, independent of data preparation and model internals.


- Business rules
- Decision-making logic
- Post-processing of model outputs

**Purpose:**  
Convert predictions into actionable decisions

---

## 4. Application Layer (`app/`)
This layer exposes the system through a Flask application.


- Handles HTTP requests
- Calls business logic
- Returns responses to users or clients

**Important Notes:**
- No data preprocessing
- No feature engineering
- No model training

**Purpose:**  
Serve the system to users via an API or interface

---

## 5. Environment Configuration
### `environment.yml`

This file defines the Conda environment used across the project to ensure consistency among all team members.

- Defines Python version
- Defines core dependencies
- Keeps the environment portable and reproducible

---

## Design Philosophy
The project follows this clear flow:

**Data prepares → AI learns → Business decides → App serves**

Each layer is isolated to:
- Reduce complexity
- Improve maintainability
- Enable team collaboration

---

## Notes
- The environment is intentionally minimal at the early stage
- Dependencies will be added incrementally as the project evolves
- Each folder should only contain code relevant to its responsibility

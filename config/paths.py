from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# Data Directories
# -------------------------
DATA_DIR = BASE_DIR / "data"
MARKET_DIR = DATA_DIR / "market_data"
ML_DIR = DATA_DIR / "ml_data"

# -------------------------
# Market Data Files |
# -------------------------
RAW_MARKET_FILE = MARKET_DIR / "raw" / "EGX30_All_Data_Combined.csv"
PROCESSED_MARKET_FILE = MARKET_DIR / "processed" / "egx30_clean.csv"

# -------------------------
# ML Datasets (Optional for EDA)
# -------------------------
TRAIN_DATA = ML_DIR / "datasets" / "train.csv"
TEST_DATA = ML_DIR / "datasets" / "test.csv"

# -------------------------
# EDA Output Folder
# -------------------------
EDA_OUTPUT_DIR = BASE_DIR / "research" / "EDA" / "outputs"
EDA_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
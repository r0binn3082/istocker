import pandas as pd
from pathlib import Path
import sys
ROOT_DIR = Path().resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from config.paths import RAW_DATA_DIR, CLEAN_DATA_DIR

class MarketDataCleaner:

    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        self.df = pd.read_csv(self.filepath)

    def clean(self):
        # Convert date
        self.df['date'] = pd.to_datetime(self.df['date'])

        # Sort properly
        self.df = self.df.sort_values(['symbol', 'date'])

        # Drop duplicates
        self.df = self.df.drop_duplicates()

        # Drop redundant column
        if 'Ticker' in self.df.columns:
            self.df = self.df.drop(columns=['Ticker'])

        # Ensure numeric
        numeric_cols = ['open', 'high', 'low', 'close', 'volume']
        self.df[numeric_cols] = self.df[numeric_cols].apply(pd.to_numeric, errors='coerce')

        # Remove zero or negative prices
        self.df = self.df[self.df['close'] > 0]

        return self.df

    def save(self, output_path):
        self.df.to_csv(output_path, index=False)
import os
import sys
from dataclasses import dataclass
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import get_logger

# Project logger
logging = get_logger()


@dataclass
class DataIngestionConfig:
    """Configuration for data ingestion paths."""
    data_source: str = os.path.join("notebook", "data", "stud.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")


class DataIngestion:
    """Handles loading the raw dataset and splitting into train/test sets.

    Usage:
        ingestion = DataIngestion()
        train_path, test_path, raw_path = ingestion.initiate_data_ingestion()
    """

    def __init__(self, config: DataIngestionConfig = DataIngestionConfig()):
        self.ingestion_config = config

    def _find_data_source(self) -> str:
        """Return a valid data source path; try configured path, then common fallbacks."""
        # Primary configured path
        if os.path.exists(self.ingestion_config.data_source):
            return self.ingestion_config.data_source

        # Try absolute path under DS_COUSE if present (common in this repo)
        alt_path = os.path.join(os.getcwd(), "DS_COUSE", "mlproject-main", "notebook", "data", "stud.csv")
        if os.path.exists(alt_path):
            logging.info(f"Found dataset at fallback path: {alt_path}")
            return alt_path

        # Try project-root relative 'notebook/data/stud.csv'
        alt2 = os.path.join(os.getcwd(), "notebook", "data", "stud.csv")
        if os.path.exists(alt2):
            return alt2

        raise FileNotFoundError(
            f"Could not find dataset. Checked: {self.ingestion_config.data_source}, {alt_path}, {alt2}"
        )

    def initiate_data_ingestion(self) -> Tuple[str, str, str]:
        logging.info("Starting data ingestion")
        try:
            data_path = self._find_data_source()

            df = pd.read_csv(data_path)
            logging.info(f"Successfully read data from {data_path}; shape={df.shape}")

            # Ensure artifacts directory exists
            artifact_dir = os.path.dirname(self.ingestion_config.raw_data_path)
            os.makedirs(artifact_dir, exist_ok=True)

            # Save raw copy
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info(f"Saved raw dataset to {self.ingestion_config.raw_data_path}")

            # Split
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info(
                f"Data ingestion completed. Train shape: {train_set.shape}, Test shape: {test_set.shape}"
            )

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path, self.ingestion_config.raw_data_path

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    ingestion = DataIngestion()
    train_path, test_path, raw_path = ingestion.initiate_data_ingestion()
    logging.info(f"Created train: {train_path}, test: {test_path}, raw: {raw_path}")
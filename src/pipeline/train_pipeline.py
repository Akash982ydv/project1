import sys
from src.exception import CustomException
from src.logger import get_logger
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

logging = get_logger()


class TrainPipeline:
    """Orchestrates data ingestion, transformation, and model training."""

    def __init__(self):
        pass

    def run_pipeline(self):
        try:
            logging.info("Starting training pipeline")

            # Data ingestion
            ingestion = DataIngestion()
            train_path, test_path, raw_path = ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion finished: train={train_path}, test={test_path}")

            # Data transformation
            data_transform = DataTransformation()
            train_arr, test_arr, preprocessor_path = data_transform.initiate_data_transformation(
                train_path, test_path
            )
            logging.info(f"Data transformation finished; preprocessor saved to {preprocessor_path}")

            # Model training
            model_trainer = ModelTrainer()
            r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
            logging.info(f"Model training finished. Best model R2: {r2_score:.4f}")

            return r2_score

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    TrainPipeline().run_pipeline()

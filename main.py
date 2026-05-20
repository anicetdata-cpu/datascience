from src.datascience import  logger
from src.datascience.pipeline.data_ingestion import  DataIngestionTrainingPipeline
STAGE_NAME="Data Ingestion Stage"



if __name__ == "__main__":
    try:
        logger.info(f">>>>> Stage {STAGE_NAME} started <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>> Stage {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.error(e)
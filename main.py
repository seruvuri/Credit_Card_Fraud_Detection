import os,sys
from src.components.data_ingestion import DataIngestion
from src.logger import logging
from src.exception import CustomException



Stage_Name="Data Ingestion"

try:
    logging.info(f">>>>>>>>>Stage {Stage_Name} started <<<<<<<<")
    Ingestion_obj=DataIngestion()
    Dataset=Ingestion_obj.initiate_data_ingestion()
except Exception as e:
    raise CustomException(e,sys)

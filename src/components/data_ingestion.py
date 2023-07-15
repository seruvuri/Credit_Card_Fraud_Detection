import os,sys
import pandas as pd

from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from src.utils import *
from src.utils import *
        

@dataclass
class DataIngestion:

    def initiate_data_ingestion(self):
        try:
            config=read_yaml(path_to_yaml='config\config.yaml')
            logging.info(">>>>>>>>Data ingestion initiated<<<<<<<<<<<")

            #collection=MongoDB_con(url=config['Mongo_Database']['url'],database_name=config['Mongo_Database']['database_name'],collection_name=config['Mongo_Database']['collection_name'])
            #print(collection.find())
            print(config['Mongo_Database'][0])
            
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    ingestion_obj=DataIngestion()
    obj=ingestion_obj.initiate_data_ingestion()
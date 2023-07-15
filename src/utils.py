import yaml
import os,sys
#from ensure import ensure_annotations
from pathlib import Path
#from box import ConfigBox
from src.logger import logging
from src.exception import CustomException
import pymongo
import certifi


def read_yaml(path_to_yaml):
   try:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
        logging.info(f"yaml file: {path_to_yaml} loaded successfully")
        return content
   except Exception as e:
      raise CustomException(e,sys)

    
def MongoDB_con(url,database_name,collection_name):
    try:
        myclient=pymongo.MongoClient(url,tlsCAFile=certifi.where())
        global collection
        logging.info("mongoDB connection initiated")
        db=myclient[database_name]
        collection=db[collection_name]
        return collection
    except Exception as e:
        raise CustomException(e,sys)
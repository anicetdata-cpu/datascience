import os
import zipfile
from urllib import request

from src.datascience import logger
from src.datascience.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(url=self.config.source_URL,
            filename=self.config.local_data_file)
            logger.info(f"Downloaded file {filename}")
        else:
            logger.info(f"File {self.config.local_data_file} already exists")

    def extract_zip_file(self):
        unzipp_path = self.config.unzip_dir
        os.makedirs(unzipp_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file) as zf:
            zf.extractall(unzipp_path)



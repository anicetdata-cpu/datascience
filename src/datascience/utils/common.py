import os
import yaml
from box.exceptions import BoxValueError

from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise BoxValueError("Yaml file is not valid or is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):


    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as json_file:
        json.dump(data, json_file)

    logger.info(f"Saved json file: {path}")



@ensure_annotations
def load_json(path: Path):
    with open(path, "r") as json_file:
        data = json.load(json_file)
    logger.info(f"Loaded json file: {path}")
    return ConfigBox(data)



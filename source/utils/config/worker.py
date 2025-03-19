import os
import yaml

class Config:
    def __init__(self, config_path='config.yml'):
        with open(os.path.join(os.path.dirname(__file__), config_path), 'r') as file:
            self.config_parser = yaml.safe_load(file)

config = Config()

def ConfigParser(category, key):
    try:
        result = config.config_parser[category][key]

        if result == None:
            raise Exception("Failed to retrieve config value")

        return config.config_parser[category][key]
    except Exception as error:
        return f"[ConfigParser] {error}", 500

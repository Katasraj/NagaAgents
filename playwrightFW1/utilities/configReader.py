import os
from configparser import ConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # playwrightFW1
CONFIG_PATH = os.path.join(BASE_DIR, "testData", "config.ini")


class ConfigFileReader:

    def readConfig(self,section, key):
        config = ConfigParser()
        files_read = config.read(CONFIG_PATH)
        if not files_read:
            raise FileNotFoundError(f"Config file not found: {CONFIG_PATH}")
        return config.get(section, key)

# print(readConfig("basic info", "URL"))
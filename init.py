import os
import sys
import json


class InitApp:

    @staticmethod
    def db_uri():
        with open("config.json") as file:
            config = json.load(file)
        return config["postgres"]["uri"]
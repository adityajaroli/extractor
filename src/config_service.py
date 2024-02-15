import os
import requests


class ConfigService:

    BASE_URL = os.getenv("CONFIG_SERVICE_URL", "http://mock-service:8086")

    @staticmethod
    def get_abs_config():
        partial_url = "abs_details"
        url = f"{ConfigService.BASE_URL}/{partial_url}"
        response = requests.get(url)
        return response.json()

    @staticmethod
    def get_db_details():
        partial_url = "db_details"
        url = f"{ConfigService.BASE_URL}/{partial_url}"
        response = requests.get(url)
        return response.json()

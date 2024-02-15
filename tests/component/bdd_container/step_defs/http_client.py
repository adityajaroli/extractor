import requests


class HttpClient:
    BASE_SERVICE_PATH = "http://extraction-service:8085"

    @staticmethod
    def get(end_point, params=None):
        url = f"{HttpClient.BASE_SERVICE_PATH}{end_point}"
        return requests.get(url, params=params)

    @staticmethod
    def post(end_point, params=None, payload=None):
        url = f"{HttpClient.BASE_SERVICE_PATH}{end_point}?order_date=2021-01-01"
        return requests.post(url, data=params, json=payload)

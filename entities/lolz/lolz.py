import asyncio
import time

import requests

import utils
from .models import Valorant


class LolzMarket:
    def __init__(self, token: str):
        self.__default_params = {
            "pmin": 1,
            "pmax": 600
        }
        self.__base_url = "https://api.lzt.market"
        self.__token = token

    def __get_token(self) -> str:
        return f"Bearer {self.__token}"

    def __get_header(self) -> dict:
        return {
            "Authorization": self.__get_token()
        }

    def __make_request(self, request_type: utils.RequestType, endpoint: str, params: dict = None) -> dict:
        if params is None:
            params = {}

        url = self.__base_url + endpoint
        response = None
        match request_type:
            case utils.RequestType.GET:
                response = requests.get(url, params=params, headers=self.__get_header())
            case utils.RequestType.POST:
                response = requests.post(url, params=params, headers=self.__get_header())

        if response.status_code == 429:
            return {
                "ok": response.ok,
                "status_code": response.status_code,
                "data": {}
            }

        return {
            "ok": response.ok,
            "status_code": response.status_code,
            "data": response.json()
        }

    def __get_all_accounts(self, category: str, params: dict = None) -> dict:
        if params is None:
            params = {}

        while True:
            result = self.__make_request(utils.RequestType.GET, f"/{category}", params)

            if result.get("status_code") == 200:
                break

        if not result.get("ok"):
            return {
                "ok": result.get("ok"),
                "error": result.get("data").get("errors"),
                "data": {}
            }

        return {
            "ok": result.get("ok"),
            "error": "",
            "data": result.get("data")
        }

    def run(self, entity: utils.Entities, params: dict = None):
        if params is None:
            params = self.__default_params

        match entity:
            case utils.Entities.Valorant:
                data = self.__get_all_accounts("valorant", params)
                if not data.get("ok"):
                    if data.get("error") is not None:
                        print("Error while getting accounts:\n")

                        for err in data.get("error"):
                            print(err)
                            print("\n")
                else:
                    Valorant(data).start()

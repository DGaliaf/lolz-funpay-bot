import asyncio
from dataclasses import dataclass

import time

import requests

import service
import utils
from .models import Valorant


class LolzMarket:
    def __init__(self, token: str, funpay_service: service.FunPay = None):
        self.__default_params = {
            "pmin": 1,
            "pmax": 250
        }
        self.__base_url = "https://api.lzt.market"
        self.__token = token
        self.__funpay_service = funpay_service
        self.__blacklist = list()

    def __get_header(self) -> dict:
        return {
            "Authorization": f"Bearer {self.__token}"
        }

    def __wrapper(self, func):
        """func - should return itemId, price"""

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

    @dataclass
    class __Credentials:
        login: str = ""
        password: str = ""
        raw: str = ""

    @dataclass
    class AccountData:
        title: str
        description: str
        login: str
        password: str
        raw: str

    def __buy(self, item: Valorant.ValidAccount) -> __Credentials:
        response = self.__make_request(utils.RequestType.POST, f"/{item.id}/fast-buy", {
            "price": item.price,
            "buy_without_validation": 0
        })

        data: dict = response.get("data")
        errors = data.get("errors")
        if errors:
            for error in errors:
                print(error + "\n")

            print(f"Не удалось купить аккаунт #{item.id} :(\n")
            return self.__Credentials()

        __Credentials: dict = data.get("item").get("loginData")

        return self.__Credentials(
            login=__Credentials.get("login"),
            password=__Credentials.get("password"),
            raw=__Credentials.get("raw")
        )

    def run(self, entity: utils.Entities, params: dict = None):
        while True:
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
                        valorant = Valorant(data, self.__blacklist)
                        valid_accounts = valorant.check()

                        for valid_account in valid_accounts:
                            self.__blacklist.append(valid_account.id)

                            params = {
                                "price": valid_account.price,
                                "buy_without_validation": 0
                            }

                            __Credentials: LolzMarket.__Credentials = self.__buy(valid_account)
                            
                            account: LolzMarket.AccountData = self.AccountData(
                                title=valid_account.title,
                                description=valid_account.description,
                                login=__Credentials.login,
                                password=__Credentials.password,
                                raw=__Credentials.raw
                            )
                            self.__funpay_service.list(account)

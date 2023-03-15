import asyncio

import service
import utils


def main():
    funpay = service.FunPay()
    lolz = service.LolzMarket("4e4cb682c56b19d98faef2fd75a7323c2e0be3b7", funpay)
    lolz.run(utils.Entities.Valorant)


if __name__ == "__main__":
    main()

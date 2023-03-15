import asyncio

import entities
import utils


async def valorant(lolz: entities.LolzMarket):
    while True:
        lolz.run(utils.Entities.Valorant)


def main():
    lolz = entities.LolzMarket("4e4cb682c56b19d98faef2fd75a7323c2e0be3b7")
    asyncio.run(valorant(lolz))


if __name__ == "__main__":
    main()

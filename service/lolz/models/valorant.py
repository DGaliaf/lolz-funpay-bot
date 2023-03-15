import config
from dataclasses import dataclass


class Valorant:
    def __init__(self, data: dict, blacklist: list):
        self.__data = data
        self.__blacklist = blacklist

    @dataclass
    class __AccountInfo:
        rank: str
        prev_rank: str
        level: str
        price: int
        region: str
        agents: list
        agents_count: int
        skins: dict
        skins_count: int
        knifes: list
        knifes_count: int

    @dataclass
    class ValidAccount:
        id: str
        price: int
        title: str
        description: str

    def __validate(self, item: dict) -> bool:
        region: str = item.get("valorant_region")
        item_id: str = item.get("item_id")
        weapons: list = item.get("valorantInventory").get("WeaponSkins")

        if (region not in config.valorant_data.regions) and \
                (weapons is None) and \
                (item_id in self.__blacklist):
            return False

        for weapon in weapons:
            if weapon.get("uuid") in config.valorant_data.knifes:
                return True

        return False

    @staticmethod
    def __create_title(data: __AccountInfo) -> str:
        if data.region != "TR" or data.region != "BR" or data.region != "LA":
            data.region = "EU"

        return f"🌈🌐{data.region} 🌐🌈🌟{data.rank} 🌟🌈🔪{data.knifes_count} ножей 🔪🌈🥵{data.agents_count}" \
               f" агентов 🥵🌈👔{data.skins_count} скинов 👔🌈🆙{data.level} уровень 🆙🌈 "

    @staticmethod
    def __create_description(data: __AccountInfo) -> str:
        text = f"❗После оплаты, Вы получаете аккаунт, с игрой Valorant, а также почту к нему.❗\n❗Аккаунт после оплаты " \
               f"- только Ваш.❗\n\n📝 ИНСТРУКЦИЯ 📝\n  ▪️️Измените полученные данные, на свои.\n  ▪️️Выйдите из всех " \
               f"сеансов.\n  ▪️️Поставьте на Ваш аккаунт двухэтапную аутентификацию.\n\n🔆ОБ АККАУНТЕ🔆\n\n "

        level = f"🆙Уровень: {data.level}\n"
        rank = f"🌟Ранг: {data.rank}\n"
        prev_rank = f"🌟Предыдущий ранг: {data.prev_rank}\n\n"
        text += level + rank + prev_rank

        skins = "👔Скины:\n"
        for skin_name in data.skins:
            if len(data.skins[skin_name]) > 0:
                skins += "  ▪️️" + skin_name + ": "
                for skin in data.skins[skin_name]:
                    skins += skin + ", "

                skins = skins[0:-2] + "\n"
        skins += "\n"
        text += skins

        knifes = "🔪Ножи:\n"
        knifes += "  ▪️️"
        for knife in data.knifes:
            knifes += knife + ", "
        knifes = knifes[0:-2] + "\n\n"
        text += knifes

        agents = "🥵Агенты:\n"
        agents += "  ▪️️"
        for agent in data.agents:
            agents += agent + ", "
        agents = agents[0:-2] + "\n\n"
        text += agents

        text += "‼️ВАЖНО‼️\nПосле покупки аккаунта я не несу за него ответственность, вся ответственность за аккаунт " \
                "лежит только на Вас, т.к. правильно выполнив все пункты инструкции, вы сможете обезопасить свой " \
                "аккаунт и не потерять его! "

        return text

    def check(self) -> list:
        accounts: dict = self.__data.get("data")
        items: list = accounts.get("items")

        valid_items = list()
        for item in items:

            if not self.__validate(item):
                continue

            print("Found needed account")

            inventory = item.get("valorantInventory")
            weapons = inventory.get("WeaponSkins")
            agents = inventory.get("Agent")
            region = item.get("valorant_region")

            skins = {
                "Odin": list(),
                "Ares": list(),
                "Vandal": list(),
                "Bulldog": list(),
                "Phantom": list(),
                "Judge": list(),
                "Bucky": list(),
                "Frenzy": list(),
                "Classic": list(),
                "Ghost": list(),
                "Sheriff": list(),
                "Shorty": list(),
                "Operator": list(),
                "Guardian": list(),
                "Marshal": list(),
                "Spectre": list(),
                "Stinger": list(),
            }
            knifes, player_agents = list(), list()

            knifes_count = 0
            for weapon in weapons:
                if weapon.get("uuid") in config.valorant_data.knifes:
                    knifes_count += 1
                    knife_name = weapon.get("displayName")
                    knifes.append(knife_name)

                else:
                    weapon_data = weapon.get("displayName").split(" ", 1)
                    weapon_type, weapon_name = weapon_data[0], weapon_data[1]

                    if weapon_type in skins:
                        skins[weapon_type].append(weapon_name)

            for agent in agents:
                agent_name = agent.get("displayName")
                player_agents.append(agent_name)

            rank = "Без ранга" if item.get("valorantRankTitle") not in config.valorant_data.ranks else item.get(
                "valorantRankTitle")
            prev_rank = "Без ранга" if item.get(
                "valorantLastRankTitle") not in config.valorant_data.ranks else item.get(
                "valorantLastRankTitle")
            level = item.get("valorant_level")
            agents_count = item.get("valorant_agent_count")
            skins_count = item.get("valorant_skin_count")
            price = item.get("price")

            product_info = [rank, prev_rank, level, agents_count, player_agents, skins_count, skins, knifes_count,
                            knifes, price, region]

            account_info = self.__AccountInfo(
                rank=rank,
                prev_rank=prev_rank,
                level=level,
                price=price,
                region=region,
                agents=player_agents,
                agents_count=agents_count,
                skins=skins,
                skins_count=skins_count,
                knifes=knifes,
                knifes_count=knifes_count
            )

            item_id = item.get("item_id")
            title = self.__create_title(account_info)
            description = self.__create_description(account_info)

            valid_item = self.ValidAccount(
                id=item_id,
                price=price,
                title=title,
                description=description
            )

            valid_items.append(valid_item)

        return valid_items

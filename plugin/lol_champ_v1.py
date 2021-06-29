from plugin.base import Base
from plugin.lol_summoner_v1 import LolSummonerV1
import json

class LolChampV1(Base):

    def __init__(self):
        super(LolChampV1, self).__init__()
        self.plugin_name = "lol_champions_v1"

    def get_summ_champ_skins(self, summ_id, champ_id):
        func_name = "get_summ_champ_skins"
        func_path = "/inventories/{}/champions/{}/skins".format(summ_id, champ_id)
        return self.send_request(func_name=func_name, func_path=func_path)


def main():
    lol_summ_v1 = LolSummonerV1()
    summ_id = lol_summ_v1.summoner["summonerId"]
    lol_champ_v1 = LolChampV1()
    response = lol_champ_v1.get_summ_champ_skins(summ_id, 1)
    response_json = response.json()
    skin_num = len(response_json)
    print(skin_num)
    for s in response_json:
        skin_name = s["name"]
        owner_ship = s["ownership"]
        is_owned = owner_ship["owned"]
        is_free = owner_ship["freeToPlayReward"]
        print(skin_name, is_owned, is_free)


if __name__ == "__main__":
    main()

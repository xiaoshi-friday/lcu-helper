from plugin.base import Base
from plugin.lol_summoner_v1 import LolSummonerV1
import json


class LolChampSelectV1(Base):

    def __init__(self):
        super(LolChampSelectV1, self).__init__()
        self.plugin_name = "lol_champ_select_v1"
        self.cell_id = None
        self.action_id = None

    # 获取全部英雄
    def get_all_champions(self):
        func_name = "get_all_champions"
        return self.send_request(func_name)

    # 获取选择英雄的状态
    def get_session(self):
        func_name = "get_session"
        return self.send_request(func_name)

    # 选择英雄并确定
    def champ_select(self, champ_id):
        func_name = "champ_select"
        func_path = "/session/actions/{}".format(self.action_id)
        data = {
            "actorCellId": self.cell_id,
            "championId": champ_id,  # 英雄的id
            "completed": True,  # 自动确认
            "id": self.action_id,
            "isAllyAction": False,
            "type": "pick"
        }
        return self.send_request(func_name=func_name, func_path=func_path, data=json.dumps(data))


def main():
    lcsv = LolChampSelectV1()
    result = lcsv.get_all_champions()
    print(result.json())


if __name__ == "__main__":
    main()

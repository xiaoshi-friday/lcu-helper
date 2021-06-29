from plugin.base import Base
import json


class LolChampSelectLegacyV1(Base):

    def __init__(self):
        super(LolChampSelectLegacyV1, self).__init__()
        self.plugin_name = "lol_champ_select_legacy_v1"

    def is_champ_select(self):
        func_name = "is_champ_select"
        return self.send_request(func_name)

    def get_session(self):
        func_name = "get_session"
        return self.send_request(func_name)

    def champ_select(self, champ_id, cell_id, action_id, pick_turn):
        func_name = "champ_select"
        func_path = "/session/actions/{}".format(action_id)
        data = {
            "actorCellId": cell_id,
            "championId": champ_id,
            # "completed": True,  # 为True时会自动锁定英雄 但是当英雄无法选择时 则会随机选择其他的英雄来代替
            "completed": False,
            "id": action_id,
            "isAllyAction": True,
            "isInProgress": True,
            "pickTurn": pick_turn,
            "type": "pick"
        }
        return self.send_request(func_name=func_name, func_path=func_path, data=json.dumps(data))

    def action_complete(self, action_id):
        func_name = "action_complete"
        func_path = "/session/actions/{}/complete".format(action_id)
        return self.send_request(func_name, func_path)

    def get_current_champ(self):
        func_name = "get_current_champ"
        return self.send_request(func_name)


def main():
    test = LolChampSelectLegacyV1()
    while True:
        # response = test.is_champ_select().text
        # if response == "true":
        # response = test.get_current_champ()
        # print(response.json())
        response = test.get_session()
        print(response.json())

if __name__ == "__main__":
    main()

import time

from plugin.lol_gameflow_v1 import LolGameFlowV1
from plugin.lol_champ_select_legacy_v1 import LolChampSelectLegacyV1
from plugin.lol_summoner_v1 import LolSummonerV1
from plugin.lol_chat_v1 import LolChatV1
from plugin.lol_champ_v1 import LolChampV1


class Helper(object):

    def __init__(self):
        self.lol_gameflow_v1 = LolGameFlowV1()
        self.lol_champ_select_legacy_v1 = LolChampSelectLegacyV1()
        self.lol_summoner_v1 = LolSummonerV1()
        self.summoner_id = self.lol_summoner_v1.summoner["summonerId"]
        self.lol_chat_v1 = LolChatV1()
        self.lol_champ_v1 = LolChampV1()
        self.phase_handler = {
            '"None"': self.none_handler,
            '"Lobby"': self.lobby_handler,
            '"ChampSelect"': self.champ_select_handler,
        }
        self.champ_id = 0
        self.champ_select_ids = [1, 2]

    # 通过summonerId获取cellId
    def get_cell_id(self, my_team):
        for member in my_team:
            if member["summonerId"] == self.summoner_id:
                cell_id = member["cellId"]
                return cell_id

    def champ_select_handler(self):
        # 存放可以使用的皮肤列表
        pickable_skins = []
        response = self.lol_champ_select_legacy_v1.get_session()
        response_json = response.json()
        # print(response_json)
        # 找到自己的cell_id
        my_team = response_json["myTeam"]
        cell_id = self.get_cell_id(my_team)

        # 找到自己的action_id和pick_turn
        actions = response_json["actions"]
        # my_info = get_my_info(cell_id, actions)
        action_id, pick_turn, champ_id = get_my_info(cell_id, actions)
        if champ_id != self.champ_id:
            self.champ_id = champ_id
            response = self.lol_champ_v1.get_summ_champ_skins(self.summoner_id, champ_id)
            response_json = response.json()
            # 不计算原皮肤
            skin_num = len(response_json) - 1
            # print(skin_num)
            '''
            征召模式
            bug: TypeError: unhashable type: 'slice'
            '''
            # 不遍历原皮肤
            for s in response_json[1:]:
                skin_name = s["name"]
                owner_ship = s["ownership"]
                is_owned = owner_ship["owned"]
                is_free = owner_ship["freeToPlayReward"]
                # print(skin_name, is_owned, is_free)
                # 能用的才放到列表里面
                if is_owned is True or is_free is True:
                    pickable_skins.append(skin_name)
            print("{}个可用的皮肤".format(len(pickable_skins)))
            print(pickable_skins)

        # 选择英雄
        # for champ_select_id in self.champ_select_ids:
        #     self.lol_champ_select_legacy_v1.champ_select(champ_select_id, cell_id, action_id, pick_turn)
        #     response = self.lol_champ_select_legacy_v1.action_complete(action_id)
        #     # 没选成功 就试着选下一个英雄
        #     if response.status_code != 204:
        #         continue
        #
        #     # 选成功了 结束
        #     break

        # 发送选择成功的消息
        # response = self.lol_chat_v1.get_conversations_info()
        # response_json = response.json()
        # conversation_id = response_json[0]["id"]
        # body = "秒选成功"
        # self.lol_chat_v1.send_public_messa    ge(conversation_id, body)

    def none_handler(self):
        # print("None")
        pass

    def lobby_handler(self):
        pass


# 获取actionId、pickTurn、championId
def get_my_info(cell_id, actions):
    for action in actions[0]:
        if cell_id != action["actorCellId"]:
            continue
        action_id = action["id"]
        pick_turn = action["pickTurn"]
        champ_id = action["championId"]
        # my_info = {
        #     "action_id": action_id,
        #     "pick_turn": pick_turn,
        #     "champ_id": champ_id
        # }
        # return my_info
        return action_id, pick_turn, champ_id


def main():
    helper = Helper()
    while True:
        # 获取状态
        response = helper.lol_gameflow_v1.get_gameflow_phase()
        gameflow_phase = response.text
        # 根据状态不同执行不同阶段的操作
        helper.phase_handler[gameflow_phase]()
        time.sleep(1)



if __name__ == "__main__":
    main()

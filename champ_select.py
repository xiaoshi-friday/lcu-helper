from plugin.lol_champ_select_legacy_v1 import LolChampSelectLegacyV1
from plugin.lol_summoner_v1 import LolSummonerV1
from plugin.lol_chat_v1 import LolChatV1
from loguru import logger


def get_cell_id(my_team):
    logger.info("获取cell_id")
    for member in my_team:
        if member["summonerId"] == LolSummonerV1().summoner["summonerId"]:
            cell_id = member["cellId"]
            logger.info("cell_id: {}".format(cell_id))
            return cell_id


def get_action_id_pick_turn(cell_id, actions):
    logger.info("获取action_id和pick_turn")
    for action in actions[0]:
        if cell_id != action["actorCellId"]:
            continue

        action_id = action["id"]
        pick_turn = action["pickTurn"]
        logger.info("action_id: {}".format(action_id))
        logger.info("pick_turn: {}".format(pick_turn))
        return action_id, pick_turn


def main():
    champ_select_ids = [157, 2]  # 安妮和狂战士
    lcslv = LolChampSelectLegacyV1()
    while True:
        response_text = lcslv.is_champ_select().text
        if response_text == "true":
            break
    logger.info("进入英雄选择")
    response_json = lcslv.get_session().json()

    # 找到自己的cell_id
    my_team = response_json["myTeam"]
    cell_id = get_cell_id(my_team)

    # 找到自己的action_id和pick_turn
    actions = response_json["actions"]
    action_id, pick_turn = get_action_id_pick_turn(cell_id, actions)

    # 选择英雄
    for champ_select_id in champ_select_ids:
        lcslv.champ_select(champ_select_id, cell_id, action_id, pick_turn)
        response = lcslv.action_complete(action_id)
        # 没选成功 就试着选下一个英雄
        if response.status_code != 204:
            logger.info("英雄选择失败")
            continue

        # 选成功了 结束
        break

    # 发送选择成功的消息
    lcv = LolChatV1()
    response = lcv.get_conversations_info()
    response_json = response.json()
    conversation_id = response_json[0]["id"]
    body = "秒选成功"
    lcv.send_public_message(conversation_id, body)


if __name__ == "__main__":
    main()

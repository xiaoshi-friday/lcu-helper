from plugin.base import Base
import json


class LolChatV1(Base):
    def __init__(self):
        super(LolChatV1, self).__init__()
        self.plugin_name = "lol_chat_v1"

    # 获取聊天室信息
    def get_conversations_info(self):
        func_name = "get_conversations_info"
        return self.send_request(func_name=func_name)

    def send_public_message(self, conversation_id, body):
        func_name = "send_public_message"
        func_path = "/conversations/{}/messages".format(conversation_id)
        data = {
            "body": body,
            "type": "chat",  # 或者是system 但是body内容只能是joined_room 或者 left_room
        }
        return self.send_request(func_name=func_name, func_path=func_path, data=json.dumps(data))


def main():
    lcv = LolChatV1()
    response = lcv.get_conversations_info()
    response_json = response.json()
    conversation_id = response_json[0]["id"]
    for i in range(0, 100):
        body = "鼠哥无敌{}".format(i)
        lcv.send_public_message(conversation_id, body)


if __name__ == "__main__":
    main()
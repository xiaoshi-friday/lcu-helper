from plugin.base import Base


class LolGameFlowV1(Base):
    def __init__(self):
        super(LolGameFlowV1, self).__init__()
        self.plugin_name = "lol_gameflow_v1"

    def get_gameflow_phase(self):
        func_name = "get_gameflow_phase"
        return self.send_request(func_name)


if __name__ == "__main__":
    lgf1 = LolGameFlowV1()
    gameflow_phase = lgf1.get_gameflow_phase()
    print(gameflow_phase.text)

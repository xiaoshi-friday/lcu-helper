from plugin.base import Base


class LolSummonerV1(Base):

    def __init__(self):
        super(LolSummonerV1, self).__init__()
        self.plugin_name = "lol_summoner_v1"
        self.summoner = self.get_current_summoner().json()

    def get_current_summoner(self):
        func_name = "get_current_summoner"
        return self.send_request(func_name)


def main():
    lsv = LolSummonerV1()
    response = lsv.get_current_summoner()
    print(response.text)


if __name__ == "__main__":
    main()

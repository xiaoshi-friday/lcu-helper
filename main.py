
class LCU:

    def __init__(self):
        '''
        swagger: swagger/v2/swagger.json
        system.yaml enable_swagger: true
        '''
        self.username = "riot"
        self.password = None
        self.port = None
        self.get_param()
        self.url = "https://{}:{}@127.0.0.1:{}".format(self.username, self.password, self.port)

    def get_param(self):
        with open("F:/lol/英雄联盟/LeagueClient/lockfile") as f:
            lock_file_content = f.read()
            # process_name:pid:token:password:protocol
            # LeagueClient:9928:60809:LCATGK3RheCrMWJwlTYG3Q:https
            split_list = lock_file_content.split(":")
            port, password = split_list[2], split_list[3]
        self.port = port
        self.password = password


if __name__ == "__main__":
    lcu = LCU()
    print(lcu.url)

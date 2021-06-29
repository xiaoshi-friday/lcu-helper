from requests.packages.urllib3.exceptions import InsecureRequestWarning
from loguru import logger
import requests
import yaml
import os

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Base(object):

    def __init__(self):
        self.username = "riot"  # 账号固定为riot
        self.password = None  # 密码需要去读取
        self.port = None  # 端口需要去读取
        self.get_param()
        self.url = "https://{}:{}@127.0.0.1:{}".format(self.username, self.password, self.port)
        logger.info("url: {}".format(self.url))
        # 该文件的路径
        this_path = os.path.dirname(__file__)
        with open('{}/config.yaml'.format(this_path), 'r', encoding="utf-8") as f:
            self.configs = yaml.load(f)

    # 获取密码和端口
    def get_param(self):
        with open("F:\lol\英雄联盟\LeagueClient\lockfile") as f:
            lock_file_content = f.read()
            # process_name:pid:port:password:protocol
            # LeagueClient:9928:60809:LCATGK3RheCrMWJwlTYG3Q:https
            split_list = lock_file_content.split(":")
            port, password = split_list[2], split_list[3]
        self.port = port
        self.password = password

    def send_request(self, func_name, func_path=None, data=None):
        # plugin_name是子类的
        plugin_config = self.configs[self.plugin_name]
        plugin_path = plugin_config["path"]
        func_config = plugin_config[func_name]
        if func_path is None:
            func_path = func_config["path"]
        url = "{}{}{}".format(self.url, plugin_path, func_path)
        response = requests.request(method=func_config["method"], url=url, verify=False, data=data, proxies={"http": "http://127.0.0.1:8888"})
        # response = requests.request(method=func_config["method"], url=url, verify=False, data=data)

        # logger.info(response.status_code)
        # logger.info(response.text)
        return response


if __name__ == "__main__":
    request_base = Base()
    # print(request_base.url)

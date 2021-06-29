from plugin.lol_champ_select_legacy_v1 import LolChampSelectLegacyV1


def main():
    pass

    # 获取是否在选择英雄了
    def is_select_champ():
        while True:
            response_text = lcslv.is_champ_select().text
            if response_text == "true":
                break

    # 如果是在选择英雄了 那么获取在选择的session

    # 取出英雄id

    # 查询该英雄可用的皮肤展示出来


if __name__ == "__main__":
    main()

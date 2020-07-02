import requests
import re
import json
import sqlitesave as save
import time


def deamds(url: str, data: dict) -> json:
    # json.loads(str)
    # json.dumps(json)
    # time.sleep(1)
    data = json.dumps(data)
    data_json = json.loads(data)
    data_json["language"] = 'zh_CN'
    data_str = json.dumps(data_json)
    response = requests.get(url + data_str)
    print(url + data_str)
    print(response.text)
    return json.loads(str(response.text))


def formatting(message: list) -> str:
    msg = ''.join([msg for msg_tuple in message if len(message) != 0 for msg in msg_tuple])
    return msg


def context() -> str:
    with open('deploy.json', 'r', encoding='utf8') as depl:
        depl_dict = json.load(depl)
    depl.close()
    select = depl_dict["environment"]
    print(select)
    return select


def gain_url(self, urlname):
    with save.SqlSave() as execute:
        url_header_list = execute.select('url', 'environment', 'name', context())
        url_end_list = execute.select('url', 'url', 'urlname', urlname)
        url_header = formatting(url_header_list)
        url_end = formatting(url_end_list)
        urls = url_header + url_end
        return urls


class UnifyWays(object):
    pass


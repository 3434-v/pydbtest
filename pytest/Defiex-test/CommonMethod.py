import requests
import re
import json
import sqlitesave as save

class UnifyWays(object):

    def deamds(self, url, data):

        # json.loads(str)
        # json.dumps(json)
        data_json = json.loads(data)
        data_json["language"] = 'zh_CN'
        data_str = json.dumps(data_json)
        response = requests.get(url + data_str)
        print(url + data_str)
        print(response.text)
        return json.loads(str(response.text))

    def formatting(self, message):
        msg = ''.join([msg for msg_tuple in message if len(message) != 0 for msg in msg_tuple])
        return msg

    # def Get_url(self, urlname):
    #
    #     with save.SqlSave() as execute:
    #         url_header_list = execute.select('url', 'environment', 'name', select)
    #         url_end_list = execute.select('url', 'url', 'urlname', urlname)
    #         url_header = ''.join(
    #             [url_header for url_tuple in url_header_list if len(url_header_list) != 0 for url_header in url_tuple])
    #         url_end = ''.join(
    #             [url_end for url_tuple in url_end_list if len(url_end_list) != 0 for url_end in url_tuple])
    #         urls = url_header + url_end
    #     return urls
import requests
import re
import json
import sqlitesave as save
from pymysqlsave import MysqlSave as mysave


# 公共reques请求函数
def deamds(url: str, data: dict) -> json:
    # loads()：将json数据转化成dict数据
    # dumps()：将dict数据转化成json数据
    # load()：读取json文件数据，转成dict数据
    # dump()：将dict数据转化成json数据后写入json文件
    # time.sleep(1)
    data = json.dumps(data)
    data_json = json.loads(data)
    data_json["language"] = 'zh_CN'
    data_str = json.dumps(data_json)
    response = requests.get(url + data_str)
    print(url + data_str)
    print(response.text)
    return json.loads(str(response.text))


# sql格式转换函数
def formatting(message: list) -> str:
    msg = ''.join([msg for msg_tuple in message if len(message) != 0 for msg in msg_tuple])
    return msg


# 读取deploy.json文件中配置的环境
def context() -> str:
    with open('deploy.json', 'r', encoding='utf8') as depl:
        depl_dict = json.load(depl)
    depl.close()
    select = depl_dict["environment"]
    print(select)
    return select


# 正则表达式提取函数
def extract(regular: str, msg: str) -> str:
    message = ''.join(re.findall('"{}": "(.*?)",'.format(regular), msg))
    return message


# 访问链接获取函数
def gain_url(urlname):
    with save.SqlSave() as execute:
        url_header_list = execute.select('url', 'environment', 'name', context())
        url_end_list = execute.select('url', 'url', 'urlname', urlname)
        url_header = formatting(url_header_list)
        url_end = formatting(url_end_list)
        urls = url_header + url_end
        return urls


# 用户token获取函数
def usertoken(username: str) -> str:
    # userlogin(username)
    with save.SqlSave() as execute:
        token = formatting(
            execute.select('token', 'Name_ResponseMsg', 'name', username)
        )

    return token


def exist(tablename: str) -> int:
    with save.SqlSave() as execute:
        state = execute.table_exist(tablename)
        return state


# 用户登录函数
def userlogin(username: str) -> None:
    with save.SqlSave() as execute:
        url = gain_url('登录')
        sqldata = execute.select('*', 'general', 'name', username)
        # 判断是否存在此用户
        if len(sqldata) == 0:
            password = 'b49a9e2a50d24396e08ca047a09588a7'
            # userlogin(username)
            # execute.general(username, password, context())
            exit(0)
        else:
            data = {
                "username": sqldata[0][1],
                "pwd": sqldata[0][2]
            }
            response = json.dumps(deamds(url, data))
            token = extract('token', response)
            userid = extract('userid', response)
            invitecode = extract('invitecode', response)
            print(exist('Name_ResponseMsg'))
            try:
                if exist('Name_ResponseMsg') == 0:

                    execute.Name_ResponseMsg(
                        sqldata[0], userid, token, invitecode, context()
                    )

                elif exist('Name_ResponseMsg') == 1:
                    execute.update(
                        'Name_ResponseMsg', token, sqldata[0]
                    )

            except:
                print('异常')


# brokername = '166704969518@qq.com'
# userlogin(brokername)

# exist('Name_ResponseMsg')


# class UnifyWays(object):
#     pass

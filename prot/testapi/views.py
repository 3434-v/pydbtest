from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import testapi.inform


# 请求内容格式转换函数
def bytes_switch_dict(msg: bytes) -> dict:
    msg_str = str(msg, encoding='utf-8')
    # print(msg_str)
    msg_list = []
    msg_dict = {}
    count = 0
    for index in range(len(msg_str)):
        if msg_str[index] == '&':
            msg_list.append(msg_str[count: index])
            count = index + 1
    msg_list.append(msg_str[count:])
    # print(msg_list)
    dict_count = 0
    for list_index in msg_list:
        for index in range(len(list_index)):
            if list_index[index] == '=':
                array = list_index[dict_count: index]
                msg_dict[array] = list_index[index+1:]
    print(msg_dict)
    return msg_dict


def readim(request):
    if request.method == "POST":
        request_data_dict = bytes_switch_dict(request.body)
        if request_data_dict['type'] == '1':
            returndata = testapi.inform.WX_robot(request_data_dict['msg'])
            return JsonResponse({"status": "WX_robot", "msg": returndata})
        elif request_data_dict['type'] == '2':
            returndata = testapi.inform.DD_robot(request_data_dict['msg'])
            return JsonResponse({"status": "DD_robot", "msg": returndata})
        else:
            return JsonResponse({"status": "-1", "msg": "不支持的请求类型"})
    elif request.method == "GET":
        return JsonResponse({"status": "-1", "msg": "暂不支持GET请求"})
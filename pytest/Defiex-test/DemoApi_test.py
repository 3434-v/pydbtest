import requests
import json




url = 'http://test.api.houtaii.com/v2/project/publish'
header = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjExMDE5LCJwaG9uZV9udW1iZXIiOiIxNTA0NDA1NDgwMCIsInJvbGUiOjMsInVtZW5nX2RldmljZSI6IkFpQVZSQm5oZ1BodjFZUER0Zl9lekxoRW5rd3pwYUVDN2tsMGp6QXFZaDdaIiwiaWF0IjoxNTk0MDI0NDQyLCJleHAiOjE1OTY2MTY0NDJ9.1axW3AUbNH6YJP-rjmkvEtHFwGXiy5ogLQ3trX3yfek",
    "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
data = {
    "project_draft_id":0,
    "project_name":"测试添加多个职位是否成功",
    "pro_cate_id":785,
    "introduct":"",
    "introduct_image":"",
    "pro_show_list":[{
    "time_type":2,
    "date_start":"2020-07-06",
    "time_start":"08:00",
    "date_end":"2020-07-31",
    "time_end":"17:00",
    "address_type":2,
    "address":"上海市徐汇区虹桥路777号(近淮海西路)汇京国际广场",
    "city_code":"310104",
    "lat":"31.19596291",
    "lng":"121.4236145",
    "house_number":"2501"
    }],
    "posts_list":[{
    "posts_name":"001",
    "gender":0,
    "posts_content":"",
    "salary_type":2,
    "salary":"321.12",
    "age":"5",
    "stature":"19,20",
    "posture":"12",
    "skill_tag":"591,592,595"
    },
    {
    "posts_name":"002",
    "gender":1,
    "posts_content":"",
    "salary_type":2,
    "salary":"321.52",
    "age":"6",
    "stature":"20,21",
    "posture":"13",
    "skill_tag":"598,599,600"
    }]
}


data_json = json.dumps(data)
print(type(data_json))
data_json = json.loads(data_json)

print(type(data_json))
response = requests.post(url, data=data_json, headers=header)
print(response.text)












def bytes_switch_dict(msg: bytes) -> dict:

    msg_str = str(msg, encoding='utf-8')
    print(msg_str)
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


# msg = b'type=1&msg=test'
# bytes_switch_dict(msg)

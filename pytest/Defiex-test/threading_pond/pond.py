from concurrent.futures import ThreadPoolExecutor
import time
import sys
import requests
# def spider(page):
#     time.sleep(page)
#     print("time:{}".format(page))
#     return page
#
#
# with ThreadPoolExecutor(max_workers=5) as thrd:
#     task1 = thrd.submit(spider, 1)
#     task2 = thrd.submit(spider, 2)
#     task3 = thrd.submit(spider, 3)
#
#     print("task1:{}".format(task1.done()))
#     print("task2:{}".format(task2.done()))
#     print("task3:{}".format(task3.done()))
#
#     time.sleep(2)
#     print("task1:{}".format(task1.done()))
#     print("task2:{}".format(task2.done()))
#     print("task3:{}".format(task3.done()))
#     print(task1.result())


def test():
    url = 'http://127.0.0.1:5000/login/'
    data = {
        "username": "389863294",
        "password": "yangxun19990728",
    }
    response = requests.post(url, data=data)
    print(response.text)

def test1():
    url = 'http://127.0.0.1:5000/register/'
    data = {
        "username": "3898632",
        "password": "yangxun1999072",
        "email": "38986394@qq.com",
        "phone": "1877018502"
    }
    response = requests.post(url, data=data)
    print(response.text)

test1()
#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: log_setLevel.py
@time: 2020/1/8 5:33 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''1. log_setLevel'''


def setLevel(api_name, params):
	'''
	设置日志级别
	:param api_name:
	:param params: 日志级别（"debug","0"）
	:return: 无
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"log_setLevel","params":["trace"], "id": 3}' -H "Content-Type:application/json"
	响应：
	{"jsonrpc":"2.0","id":3,"result":null}
	'''
	try:
		result = request_Api(api_name, params)
		print("设置日志级别,{}".format(result))
		return result
	except Exception as e:
		print("设置日志级别api报错,{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "log_setLevel"
	params = ["trace"]
	setLevel(api_name, params)

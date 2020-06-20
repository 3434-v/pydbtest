#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: consensus_changeWaitTime.py
@time: 2020/1/8 5:58 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''2. consensus_getMiners '''


def changeWaitTime(api_name, params):
	'''
	共识时间，一般救急时使用
	修改leader等待时间 (ms)
	:param api_name: 等待时间(ms)
	:param params:
	:return: 私钥
	示例代码
	curl http://localhost:35645 -X POST --data '{"jsonrpc":"2.0","method":"consensus_getMiners","params":[""], "id": 3}' -H "Content-Type:application/json"
	'''
	try:
		result = request_Api(api_name, params)
		print("获取当前出块节点成功，{}".format(result))
		return result
	except Exception as e:
		print("获取当前出块节点失败，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "consensus_getMiners"
	params = [""]
	changeWaitTime(api_name, params)
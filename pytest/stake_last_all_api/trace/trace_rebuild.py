#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: trace_rebuild.py
@time: 2020/1/8 5:36 下午
@desc:
'''
import logging

from stake_last_all_api.API import request_Api

'''6. trace_rebuild'''


def rebuild(api_name, params):
	'''
	重建trace中的区块记录
	e.g:
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_rebuild","params":[1,10], "id": 3}' -H "Content-Type:application/json"
	:param api_name:
	:param params:  1. 起始块（包含）2. 终止块（不包含）
	:return:
	'''
	
	try:
		result = request_Api(api_name, params)
		print("重建trace中的区块记录,{}".format(result))
		return result
	except Exception as e:
		print("重建trace中的区块记录api返回错误".format(e))
		logging.info("重建trace中的区块记录api返回错误".format(e))
		return -1


if __name__ == '__main__':
	api_name = "trace_rebuild"
	params = [1, 10]
	rebuild(api_name, params)

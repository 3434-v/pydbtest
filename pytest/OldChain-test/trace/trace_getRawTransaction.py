#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: trace_getRawTransaction.py
@time: 2020/1/8 5:34 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''1. trace_getRawTransaction'''


def getRawTransaction(api_name, params):
	'''
	根据交易hash查询交易字节
	:param api_name: trace_getRawTransaction
	:param params: 交易hash
	:return: 交易字节信息
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_getRawTransaction","params":["0x00001c9b8c8fdb1f53faf02321f76253704123e2b56cce065852bab93e526ae2"], "id": 3}' -H "Content-Type:application/json"
	'''
	try:
		result = request_Api(api_name, params)
		print("把交易字节信息反解析成交易详情，返回值为{}".format(result))
		return result
	except Exception as e:
		print("把交易字节信息反解析成交易详情api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "trace_getRawTransaction"
	params = ["0x00001c9b8c8fdb1f53faf02321f76253704123e2b56cce065852bab93e526ae2"]
	getRawTransaction(api_name, params)

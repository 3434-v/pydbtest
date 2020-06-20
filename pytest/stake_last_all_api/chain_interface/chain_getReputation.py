#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getReputation.py
@time: 2020/1/8 5:23 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''5. chain_getNonce'''


def getReputation(api_name, params):
	'''
	查询地址的名誉值
	:param api_name: chain_getReputation
	:param params:待查询地址
	:return: 地址对应的名誉值
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getReputation","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("查询地址的名誉值，{}".format(result))
		return result
	except Exception as e:
		print("查询地址的名誉值失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getReputation"
	params = ["0xf0FD4230c00f85B0EC32D6eD2Fd4B52dE408b660"]
	getReputation(api_name, params)

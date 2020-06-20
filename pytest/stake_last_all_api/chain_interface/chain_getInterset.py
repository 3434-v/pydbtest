#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getInterset.py
@time: 2020/1/13 6:22 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''chain_getInterset'''


def getInterset(api_name, params):
	'''
	根据txhash获取退质押或者投票利息信息
	:param api_name:
	:param params: txhash
	:return: {}
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getInterset","params":["0x7d9dd32ca192e765ff2abd7c5f8931cc3f77f8f47d2d52170c7804c2ca2c5dd9"], "id": 3}' -H "Content-Type:application/json"
	响应：

	{"jsonrpc":"2.0","id":3,"result":""}
	'''
	try:
		result = request_Api(api_name, params)
		print("根据txhash获取退质押或者投票利息信息成功,{}".format(result))
		return result
	except Exception as e:
		print("根据txhash获取退质押或者投票利息信息失败,{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getInterset"
	# params = ["0x3d3af62b6bd02873d8bf0b6897c8b5651c793b27c24241b1e62442e0384dfdc1"]
	params = ["0x9c9afcc31dc8a8d582a1c0885a5f3baf2eae390ddebd6887c5367acb8caded35"]


	getInterset(api_name, params)



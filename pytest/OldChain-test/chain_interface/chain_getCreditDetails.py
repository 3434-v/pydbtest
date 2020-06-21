#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getCreditDetails.py
@time: 2020/1/8 5:30 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''12. chain_getCreditDetails'''


def getCreditDetails(api_name, params):
	'''
	根据地址获取stake 所有细节信息
	:param api_name: chain_getTransactionByBlockHeightAndIndex
	:param params:地址
	:return: bytecode
	示例代码
	curl http://39.98.39.224:35645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getCreditDetails","params":["0x9aD84792B8B88fA11Ac9DcE0615D8D3DA0A269d4"], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("根据地址获取stake 所有细节信息，{}".format(result))
		return result
	except Exception as e:
		print("根据地址获取stake 所有细节信息失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getCreditDetails"
	# params = ["0xf0FD4230c00f85B0EC32D6eD2Fd4B52dE408b660"]
	params = ["0xB490Ffa71d9d1D9f4472FBc46eE6e4FFd2bb486b"]

	getCreditDetails(api_name, params)

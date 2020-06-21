#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getCancelCreditDetails.py
@time: 2020/1/8 5:30 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''13. chain_GetCancelCreditDetails'''


def getCancelCreditDetails(api_name, params):
	'''
	获取所有退票请求的细节
	:param api_name: chain_getCancelCreditDetails
	:param params:地址
	:return: bytecode
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getCancelCreditDetails","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("根据txhash获取receipt信息成功，{}".format(result))
		return result
	except Exception as e:
		print("根据txhash获取receipt信息失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getCancelCreditDetails"
	params = ["0x9ec31b099f48e20e40698f928ae1b75e114965a9"]
	getCancelCreditDetails(api_name, params)

#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getLogs.py
@time: 2020/1/8 5:29 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''10. chain_getLogs'''


def getLogs(api_name, params):
	'''
	根据txhash获取交易log信息
	:param api_name: chain_getMaxHeight
	:param params:txhash
	:return: []log
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getLogs","params":["0x7d9dd32ca192e765ff2abd7c5f8931cc3f77f8f47d2d52170c7804c2ca2c5dd9"], "id": 3}' -H "Content-Type:application/json"
	'''

	try:
		result = request_Api(api_name, params)
		print("根据txhash获取交易log信息成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("根据txhash获取交易log信息失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getLogs"
	params = ["0xc4b7f1f181296c068e49145e89d5f2775b824d56d61063a658a52282c6b23714"]
	getLogs(api_name, params)

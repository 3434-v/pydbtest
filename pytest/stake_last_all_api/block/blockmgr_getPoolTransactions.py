#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: blockmgr_getPoolTransactions.py
@time: 2020/1/8 5:18 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''2. blockmgr_getPoolTransactions'''


def getPoolTransactions(api_name, params):
	'''
	获取交易池中的交易信息
	:param api_name: blockmgr_getPoolTransactions
	:param params: 待查询地址
	:return: 交易池中所有交易
	示例代码
	curl http://127.0.0.1:35645 -X POST --data '{"jsonrpc":"2.0","method":"blockmgr_getPoolTransactions","params":["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c"], "id": 3}' -H "Content-Type:application/json"
	'''
	try:
		result = request_Api(api_name, params)
		print("获取交易池中的交易信息".format(result))
		return result
	except Exception as e:
		print("获取交易池中的交易信息api报错,{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "blockmgr_getPoolTransactions"
	# params = ["0x9aD84792B8B88fA11Ac9DcE0615D8D3DA0A269d4"]
	params = ["0xe70ae3477f31689f54436bc739961a62ed0a0abb"]


	request_Api(api_name, params)

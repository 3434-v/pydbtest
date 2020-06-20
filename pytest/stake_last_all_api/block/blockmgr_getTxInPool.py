#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: blockmgr_getTxInPool.py
@time: 2020/1/8 5:20 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''4. blockmgr_getTxInPool'''


def getTxInPool(api_name, params):
	'''
	查询交易是否在交易池，如果在，返回交易
	:param api_name:
	:param params: 发起转账的地址
	:return: 交易完整信息
	示例代码
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"blockmgr_getTxInPool","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5"],"id":1}' http://127.0.0.1:15645
	'''
	try:
		result = request_Api(api_name, params)
		print("查询交易是否在交易池中，如果在，返回交易，{}".format(result))
		return result
	except Exception as e:
		print("查询交易是否在交易池中api错误，{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "blockmgr_getTxInPool"
	params = ["0x710295e15edc71653b0ff8e36cf70b05c3e9208703c01a1b4dbc9bf68938fbb3"]
	getTxInPool(api_name, params)

#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getTransactionByBlockHeightAndIndex.py
@time: 2020/1/8 5:24 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''6. chain_getTransactionByBlockHeightAndIndex'''


def getTransactionByBlockHeightAndIndex(api_name, params):
	'''
	获取区块中特定序列的交易
	:param api_name: chain_getTransactionByBlockHeightAndIndex
	:param params:区块高度;交易序列
	:return: 交易信息
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getTransactionByBlockHeightAndIndex","params":[10000,1], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("获取区块中特定序列的交易，{}".format(result))
		return result
	except Exception as e:
		print("获取区块中特定序列的交易失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getTransactionByBlockHeightAndIndex"
	params = [20545, 1]
	getTransactionByBlockHeightAndIndex(api_name, params)

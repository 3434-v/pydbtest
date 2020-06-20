#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getMaxHeight.py
@time: 2020/1/8 5:22 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''2. chain_getMaxHeight'''


def getMaxHeight(api_name, params):
	'''
	用于获取当前最高区块
	:param api_name: chain_getMaxHeight
	:param params:无
	:return: 当前最高区块高度数值
	示例代码
	curl http://39.98.39.224:35645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getMaxHeight","params":[], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("查询地址在链上的nonce成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("查询地址在链上的nonce失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getMaxHeight"

	params = []
	getMaxHeight(api_name, params)

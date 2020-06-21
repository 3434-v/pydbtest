#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: blockmgr_getTransactionCount.py
@time: 2020/1/8 5:19 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''3. blockmgr_getTransactionCount'''


def getTransactionCount(api_name, params):
	'''
	获取地址发出的交易总数.
	:param api_name:
	:param params: 待查询地址
	:return: 获取地址发出的交易总数
	示例代码
	curl http://39.98.39.224:35645 -X POST --data '{"jsonrpc":"2.0","method":"blockmgr_getTransactionCount","params":["0x9aD84792B8B88fA11Ac9DcE0615D8D3DA0A269d4"], "id": 3}' -H "Content-Type:application/json"
	'''
	try:
		result = request_Api(api_name, params)
		print("获取地址发出的交易总数,{}".format(result))
		return result
	except Exception as e:
		print("获取地址发出的交易总数api返回错误,{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "blockmgr_getTransactionCount"
	# params = ["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c"]
	params = ["0x9aD84792B8B88fA11Ac9DcE0615D8D3DA0A269d4"]
	getTransactionCount(api_name, params)

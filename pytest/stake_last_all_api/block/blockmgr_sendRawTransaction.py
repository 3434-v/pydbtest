#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: blockmgr_sendRawTransaction.py
@time: 2020/1/8 5:18 下午
@desc:
'''
from stake_last_all_api.API import request_Api

'''1. blockmgr_sendRawTransaction'''

def sendRawTransaction(api_name, params):
	'''
	发送已签名的交易
	:param api_name:
	:param params:交易内容，交易内容由钱包那边生成，该api主要配合钱包端使用
	:return:交易哈希
	示例代码
	curl http://localhost:35645 -X POST --data '{"jsonrpc":"2.0","method":"blockmgr_sendRawTransaction","params":["0x40a287b6d30b05313131317a4120dd8c23c40910d038fa43b2f8932d3681cbe5ee3079b6e9de0bea6e8e6b2a867a561aa26e1cd6b62aa0422a043186b593b784bf80845c3fd5a7fbfe62e61d8564"], "id": 3}' -H "Content-Type:application/json"
	'''
	try:
		result = request_Api(api_name, params)
		print("发送已签名的交易，返回交易哈希，{}".format(result))
		return result
	except Exception as e:
		print("发送已签名的交易api错误，{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "blockmgr_sendRawTransaction"
	params = ["0x020400ad3dc2d8aedef155eaba42ab72c1fe480699336c000203e802044c027530faf7b8ee0b00411f7b4931488dcaeabbe94d3394c6fdbd84ef873e484ebb2df0efa95949aa9dd4c27eacb6e6ca24b2705232f930c491ed3b40603e68bd3efbbab2b5bdb4df2a0802"]
	sendRawTransaction(api_name, params)


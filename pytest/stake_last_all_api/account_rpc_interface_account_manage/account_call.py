#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_call.py
@time: 2020/1/8 5:53 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''14. account_call'''


def call(api_name, params):
	'''
	调用合约
	:param api_name: "trace_decodeTrasnaction"
	:param params: 调用者的地址;合约地址;代码;金额;gas价格;gas上限
	:return: 合约地址
	示例代码
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_call","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5","0x6d4ce63c","0x111","0x110","0x30000"],"id":1}' http://127.0.0.1:15645
	'''
	try:
		result = request_Api(api_name, params)
		print("把交易字节信息反解析成交易详情，返回值为{}".format(result))
		return result
	except Exception as e:
		print("把交易字节信息反解析成交易详情api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_call"
	params = ["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5", "0x6d4ce63c", "0x111", "0x110", "0x30000"]
	call(api_name, params)

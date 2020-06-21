#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_closeWallet.py
@time: 2020/1/8 5:40 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''7. account_closeWallet'''


def closeWallet(api_name, params):
	'''
	关闭钱包
	:param api_name: "trace_decodeTrasnaction"
	:param params:
	:return: 无
	示例代码
	curl http://39.98.39.224:35645 -X POST --data '{"jsonrpc":"2.0","method":"account_closeWallet","params":[], "id": 3}' -H "Content-Type:application/json"
	'''
	try:
		result = request_Api(api_name, params)
		print("关闭钱包成功，返回值为{}".format(result))
		return result
	except Exception as e:
		print("关闭钱包失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_closeWallet"
	params = []
	closeWallet(api_name, params)
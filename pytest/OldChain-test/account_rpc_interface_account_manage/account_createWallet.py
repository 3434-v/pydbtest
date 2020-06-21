#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_createWallet.py
@time: 2020/1/8 5:39 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''3. account_createWallet'''


def createWallet(api_name, params):
	'''
	创建本地钱包
	:param api_name: account_createWallet
	:param params:钱包密码
	:return: 失败返回错误原因，成功不返回任何信息
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_createWallet","params":["123"], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("创建本地钱包成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("创建本地钱包失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_createWallet"
	params = ["123"]
	createWallet(api_name, params)
#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_listAddress.py
@time: 2020/1/8 5:38 下午
@desc:
'''


from stake_last_all_api.API import request_Api

'''1. account_listAddress'''

def listAddress(api_name, params):
	'''
	列出所有本地地址
	:param api_name: account_listAddress
	:param params:
	:return: 地址数组
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_listAddress","params":[], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("列出所有本地地址，地址为{}".format(result))
		return result
	except Exception as e:
		print("列出所有本地地址api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_listAddress"
	params = ["1234567989465"]
	listAddress(api_name, params)

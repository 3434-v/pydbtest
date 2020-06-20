#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_setAlias.py
@time: 2020/1/8 5:41 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''9. account_setAlias'''


def setAlias(api_name, params):
	'''
	设置别名
	:param api_name: account_setAlias
	:param params:带设置别名的地址；别名；gas价格；gas上限
	:return: 交易地址
	示例代码
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_setAlias","params":["0x9aD84792B8B88fA11Ac9DcE0615D8D3DA0A269d4","AAAAA","0x110","0x30000"],"id":1}' http://39.98.39.224:35645
	'''
	
	try:
		result = request_Api(api_name, params)
		print("设置别名成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("设置别名失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_setAlias"
	params = ["0x9ec31b099f48e20e40698f928ae1b75e114965a9","a6sdf156sdf1","0x110","0x30000"]
	setAlias(api_name, params)

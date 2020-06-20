#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getAddressByAlias.py
@time: 2020/1/8 5:27 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''8. chain_getAddressByAlias'''


def getAddressByAlias(api_name, params):
	'''
	根据别名获取别名对应的地址
	:param api_name: chain_getAddressByAlias
	:param params:待查询地别名
	:return: 别名对应的地址
	示例代码
	curl http://39.98.39.224:35645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getAddressByAlias","params":["AAAAA"], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("根据别名获取别名对应的地址成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("根据别名获取别名对应的地址失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getAddressByAlias"
	params = ["a6sdf156sdf1"]
	getAddressByAlias(api_name, params)

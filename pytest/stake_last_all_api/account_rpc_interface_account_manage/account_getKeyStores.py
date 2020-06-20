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

'''9. account_dumpKeyStore'''
#
# 	 name: dumpKeyStore
# 	 usage: 导出keystore
# 	 params:
# 		1.addr -- 地址
# 		2.password -- keystore 密码
# 		3.path -- keystore 存储路径
# 	 return: address
# 	 example:
# 		curl http://localhost:35645 -X POST --data '{"jsonrpc":"2.0","method":"account_dumpKeyStore","params":["0x9ec31b099f48e20e40698f928ae1b75e114965a9","123456","C:\keystore"], "id": 3}' -H "Content-Type:application/json"
# 	response:
# 		 {"jsonrpc":"2.0","id":3,"result":"0x748eb65493a964e568800c3c2885c63a0de9f9ae"}
#



def getKeyStores(api_name, params):

	
	try:
		result = request_Api(api_name, params)
		print("获取keyStore路径成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("获取keyStore路径失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_getKeyStores"
	params = []
	getKeyStores(api_name, params)

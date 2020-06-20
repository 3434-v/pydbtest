#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_importKeyStore.py
@time: 2020/1/8 5:57 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''19. account_importKeyStore'''


def importKeyStore(api_name, params):
	'''
	导入keystore
	:param api_name: "account_importKeyStore"
	:param params:path；password
	:return: address list
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_importKeyStore","params":["path","123"], "id": 3}' -H "Content-Type:application/json"

	'''
	try:
		result = request_Api(api_name, params)
		print("导入keystore成功，返回值为{}".format(result))
		return result
	except Exception as e:
		print("导入keystore失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_importKeyStore"
	params = ["C:\keystore","123456"]
	importKeyStore(api_name, params)



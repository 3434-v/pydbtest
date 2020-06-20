#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_dumpPrivkey.py
@time: 2020/1/8 5:54 下午
@desc:
'''


from stake_last_all_api.API import request_Api

'''16. account_dumpPrivkey'''


def dumpPrivkey(api_name, params):
	'''
	导出私钥
	:param api_name: "account_dumpPrivkey"
	:param params:
	:return: 私钥
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_dumpPrivkey","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5"], "id": 3}' -H "Content-Type:application/json"
	'''
	try:
		result = request_Api(api_name, params)
		print("导出私钥成功，返回值为{}".format(result))
		return result
	except Exception as e:
		print("导出私钥失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_dumpPrivkey"
	params = ["0x72fbad34459b1d0f9984dd295261887c661ee841"]
	dumpPrivkey(api_name, params)
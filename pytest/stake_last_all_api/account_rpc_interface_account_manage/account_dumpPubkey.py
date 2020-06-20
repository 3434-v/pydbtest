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

# 20. account_DumpPubkey
# 作用：导出地址对应的公钥


def dumpPrivkey(api_name, params):
	'''
	导出私钥
	:param api_name: "account_dumpPrivkey"
	:param params:
	:return: 私钥
	示例代码
	curl http://127.0.0.1:35645 -X POST --data '{"jsonrpc":"2.0","method":"account_dumpPubkey","params":["0xf783741a1f125c2e0c0e9dafd2017f03c03e403b"], "id": 3}' -H "Content-Type:application/json"
	'''
	try:
		result = request_Api(api_name, params)
		print("导出私钥成功，返回值为{}".format(result))
		return result
	except Exception as e:
		print("导出私钥失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_dumpPubkey"
	params = ["0x67ab89dcfb051bdcf15d8b665f568cb118eeab2d"]
	dumpPrivkey(api_name, params)
#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_lockAccount.py
@time: 2020/1/8 5:39 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''4. account_lockAccount'''


def lockAccount(api_name, params):
	'''
	锁定账号
	:param api_name: account_lockAccount
	:param params:需要锁住的账号地址
	:return: 失败返回错误原因，成功不返回任何信息
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_lockAccount","params":["0x518b3fefa3fb9a72753c6ad10a2b68cc034ec391"], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("锁定账号成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("锁定账号失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_lockAccount"
	params = ["0x67ab89dcfb051bdcf15d8b665f568cb118eeab2d"]
	lockAccount(api_name, params)
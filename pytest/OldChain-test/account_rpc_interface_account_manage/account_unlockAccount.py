#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_unlockAccount.py
@time: 2020/1/8 5:40 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''5. account_account_unlockAccount'''


def unlockAccount(api_name, params):
	'''
	解锁账号
	:param api_name: account_unlockAccount
	:param params:账号地址
	:return: 失败返回错误原因，成功不返回任何信息
	示例代码
	curl  http://154.197.27.232:35645 -X POST --data '{"jsonrpc":"2.0","method":"account_unlockAccount","params":["0xb6e5378dD0248D957EF150bF198ff0ad99e10228", "123456"], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("转账成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("转账失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':

	api_name = "account_unlockAccount"


	params = ["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c", "1234567"]
	# params = ["0x14aF424238BD4eA60C356c967D5709AB3f8224ed", "123456"]
	# params = ["0xf0FD4230c00f85B0EC32D6eD2Fd4B52dE408b660"]
	# params = ["0x9ec31b099f48e20e40698f928ae1b75e114965a9"]
	# params = ["0x7b1cAdA0C9c25Eb2E1dE5e5A03a407D11c45b3DE"]
	# params = ["0xAa9f9063000e783924CC0A507bb51936dDD018ab"]




	unlockAccount(api_name, params)
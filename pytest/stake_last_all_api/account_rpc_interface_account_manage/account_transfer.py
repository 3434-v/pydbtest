#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_transfer.py
@time: 2020/1/8 5:41 下午
@desc:
'''

from stake_last_all_api.API import request_Api
from time import sleep
import random

'''8. account_transfer'''


def transfer(api_name, params):
	'''
	转账
	:param api_name: account_transfer
	:param params:发起转账的地址；接受者的地址；金额；gas价格；gas上限；备注
	:return: 交易地址
	示例代码
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_transfer","params":["0x72fbad34459b1d0f9984dd295261887c661ee841","0xB490Ffa71d9d1D9f4472FBc46eE6e4FFd2bb486b","0x111","0x110","0x30000",""],"id":1}' http://39.98.39.224:35645
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_transfer","params":["0x72fbad34459b1d0f9984dd295261887c661ee841","0xB490Ffa71d9d1D9f4472FBc46eE6e4FFd2bb486b","0x111‬","0x110","0x30000",""],"id":1}' http://localhost:35645
	'''
	
	try:
		result = request_Api(api_name, params)
		print("转账成功，返回值{}".format(result))
		return result
	except Exception as e:
		print("转账失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
		api_name = "account_transfer"

		params = ["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c","0x6ddf4bd80c274711d8022e9251323377ba09a2d9","0x21e19e0c9bab2400000","0x110","0x30000",""]
		# params = ["0x9aD84792B8B88fA11Ac9DcE0615D8D3DA0A269d4","0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c","0xDE0B6B3A7640000","0x110","0x30000",""]
		# params = ["0x72fbad34459b1d0f9984dd295261887c661ee841","0xB490Ffa71d9d1D9f4472FBc46eE6e4FFd2bb486b","0xDE0B6B3A7640000","0x20000","0x300000",""]
		# params = ["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c","0xBb6F539027D6A767D8eca16806804A85A5b82ea6","0xd3c21bcecceda1000000","0x20000","0x300000",""]
		# params = ["0xBb6F539027D6A767D8eca16806804A85A5b82ea6","0x9aD84792B8B88fA11Ac9DcE0615D8D3DA0A269d4","0xDE0B6B3A7640000","0x20000","0x300000",""]
		# params = ["0xBb6F539027D6A767D8eca16806804A85A5b82ea6","0x7b1cAdA0C9c25Eb2E1dE5e5A03a407D11c45b3DE","0xDE0B6B3A7640000","0x20000","0x300000",""]

		transfer(api_name, params)



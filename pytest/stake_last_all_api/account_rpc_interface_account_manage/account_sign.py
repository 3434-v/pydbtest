#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_sign.py
@time: 2020/1/8 5:56 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''17. account_sign'''


def sign(api_name, params):
	'''
	账号签名
	:param api_name: account_sign
	:param params:地址；消息hash
	:return: 签名结果，签名后的交易，裸交易结果
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"account_sign","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5", "0x00001c9b8c8fdb1f53faf02321f76253704123e2b56cce065852bab93e526ae2"], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("账号签名成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("账号签名失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_sign"
	params = ["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c", "0x00001c9b8c8fdb1f53faf02321f76253704123e2b56cce065852bab93e526ae2"]
	sign(api_name, params)


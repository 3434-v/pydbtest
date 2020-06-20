#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: blockMgr_gasPrice.py
@time: 2020/2/13 3:58 pm
@desc:
'''

from stake_last_all_api.API import request_Api

'''blockMgr_gasPrice'''


def blockmgrGasPrice(api_name, params):
	'''
	获取系统的给出的gasprice建议值
	:param api_name: blockmgr_gasPrice
	:param params: [],待查询地址
	:return: 价格和是否错误信息
	'''
	try:
		result = request_Api(api_name, params)
		print("获取系统的给出的gasprice建议值成功，返回值为{}".format(result))
		return result
	except Exception as e:
		print("获取系统的给出的gasprice建议值成功，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "blockmgr_gasPrice"
	# params = ["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c"]
	params = [""]
	blockmgrGasPrice(api_name, params)
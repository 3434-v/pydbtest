#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getBlockGasInfo.py
@time: 2020/2/13 4:50 pm
@desc:
'''


from stake_last_all_api.API import request_Api

'''chain_getBlockGasInfo'''


def getBlockGasInfo(api_name, params):
	'''
	获取gas相关信息
	:param api_name: chain_getBlockGasInfo
	:param params: []
	:return: 系统需要的gas最小值、最大值；和当前块被设置的最大gas值
	'''
	try:
		result = request_Api(api_name, params)
		print("获取gas相关信息，返回值为{}".format(result))
		return result
	except Exception as e:
		print("获取获取gas相关信息失败，api返回错误，返回值为：".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getBlockGasInfo"
	params = [""]
	getBlockGasInfo(api_name, params)
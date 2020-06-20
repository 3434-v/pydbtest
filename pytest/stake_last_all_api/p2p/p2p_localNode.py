#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: p2p_localNode.py
@time: 2020/1/9 11:43 上午
@desc:
'''

from stake_last_all_api.API import request_Api


def localNode(api_name, params):
	'''
	需要获取本地的enode，用于P2p链接
	:param api_name: p2p_localNode
	:param params: [""]
	:return: 本地节点的enode
	'''
	try:
		result = request_Api(api_name, params)
		print("把交易字节信息反解析成交易详情，返回值为{}".format(result))
		return result
	except Exception as e:
		print("把交易字节信息反解析成交易详情api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "p2p_localNode"
	params = [""]
	localNode(api_name, params)

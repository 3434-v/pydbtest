#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: p2p_addPeers.py
@time: 2020/1/8 5:32 下午
@desc:
'''

from stake_last_all_api.API import request_Api

''' p2p_addPeers
'''


def addPeers(api_name, params):
	'''
	添加节点
	:param api_name: p2p_addPeers
	:param params: 添加的节点的p2p信息+ip地址,以数组的形式传入
	:return: nil
	示例代码
	"enode://e823f76643b55d93ece0f62b01000c21202a49700a8752e31eb3002a631da9a7@39.98.39.224:35645"
	'''
	try:
		result = request_Api(api_name, params)
		print("添加节点，返回值为{}".format(result))
		return result
	except Exception as e:
		print("添加节点返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "p2p_addPeer"
	params = ["enode://25d02838c0a1da90bfac372439db9ba3c94604c72f3625cd0b9453afdd36b014@127.0.0.1:44444"]
	addPeers(api_name, params)

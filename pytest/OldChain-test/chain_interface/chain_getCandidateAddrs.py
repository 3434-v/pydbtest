#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getCandidateAddrs.py
@time: 2020/1/8 5:31 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''14. chain_GetCandidateAddrs'''


def getCandidateAddrs(api_name, params):
	'''
	获取所有候选节点地址和对应的信任值
	:param api_name: chain_getCandidateAddrs
	:param params:地址
	:return: []
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getCandidateAddrs","params":[""], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("获取所有候选节点地址和对应的信任值成功，{}".format(result))
		return result
	except Exception as e:
		print("获取所有候选节点地址和对应的信任值失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getCandidateAddrs"
	params = [""]
	getCandidateAddrs(api_name, params)

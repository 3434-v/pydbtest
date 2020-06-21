#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: trace_getSendTransactionByAddr.py
@time: 2020/1/8 5:35 下午
@desc:
'''
import logging

from stake_last_all_api.API import request_Api

'''4. trace_getSendTransactionByAddr'''


def getSendTransactionByAddr(api_name, params):
	'''
	根据地址查询该交易发出的交易，支持分页，从0开始计数，返回结果中的nonce为交易序号
	e.g:
	curl http://localhost:35645 -X POST --data '{"jsonrpc":"2.0","method":"trace_getSendTransactionByAddr","params":["0x7923a30bbfbcb998a6534d56b313e68c8e0c594a",1,10], "id": 3}' -H "Content-Type:application/json"
	:param api_name:
	:param params:  1. 交易地址 2. 分页号（从1开始）3. 页大小
	:return: 交易列表
	'''
	try:
		result = request_Api(api_name, params)
		print("根据地址查询该交易发出的交易，支持分页,{}".format(result))
		return resulttrace_getSendTransactionByAddr
	except Exception as e:
		print("根据地址查询该交易发出的交易，支持分页,api返回错误".format(e))
		logging.info("根据地址查询该交易发出的交易，支持分页,api返回错误".format(e))
		return -1


if __name__ == '__main__':
	api_name = "trace_getSendTransactionByAddr"
	params = ["0x7923a30bbfbcb998a6534d56b313e68c8e0c594a", 1, 10]
	getSendTransactionByAddr(api_name, params)
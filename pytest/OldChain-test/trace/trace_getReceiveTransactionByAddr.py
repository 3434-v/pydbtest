#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: trace_getReceiveTransactionByAddr.py
@time: 2020/1/8 5:36 下午
@desc:
'''
import logging

from stake_last_all_api.API import request_Api

'''5. trace_getReceiveTransactionByAd'''


# 目前为未分页效果，分页未实现
# 得到地址中所有交易
def getReceiveTransactionByAd(api_name, params):
	'''
	根据地址查询该地址接受的交易，支持分页
	:param api_name:
	:param params:  1. 交易地址; 2. 分页号（从1开始）3. 页大小
	:return: 交易列表
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_getReceiveTransactionByAddr","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5",1,10], "id": 3}' -H "Content-Type:application/json"
	'''
	try:
		reTransaction = request_Api(api_name, params)
		print(reTransaction)
		return reTransaction
	except Exception as e:
		print("根据地址查询该交易接受的交易，支持分页,api返回错误".format(e))
		logging.info("根据地址查询该交易接受的交易，支持分页,api返回错误".format(e))
		return -1
	

if __name__ == '__main__':
	api_name = "trace_getReceiveTransactionByAddr"
	params = ["0x9aD84792B8B88fA11Ac9DcE0615D8D3DA0A269d4", 1, 10]
	getReceiveTransactionByAd(api_name, params)




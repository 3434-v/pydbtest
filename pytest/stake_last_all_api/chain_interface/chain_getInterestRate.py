#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: chain_getInterset.py
@time: 2020/1/13 6:22 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''chain_getInterestRate'''


def getInterset(api_name, params):
	'''
	根据txhash获取退质押或者投票利息信息
	:param api_name:
	:param params: txhash
	:return: {}
	示例代码
    curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getInterestRate","params":"", "id": 3}' -H "Content-Type:application/json"
	响应：
	{"jsonrpc":"2.0","id":3,"result":"{\"ThreeMonthRate\":4,\"SixMonthRate\":12,\"OneYearRate\":25,\"MoreOneYearRate\":51}"}
	'''
	try:
		result = request_Api(api_name, params)
		print("获取3个月内、3-6个月、6-12个月、12个月以上的利率成功,{}".format(result))
		return result
	except Exception as e:
		print("获取3个月内、3-6个月、6-12个月、12个月以上的利率失败,{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getI" \
			   "nterestRate"
	params = [""]
	getInterset(api_name, params)



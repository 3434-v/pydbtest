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

'''chain_getChangeCycle'''


def chain_getChangeCycle(api_name, params):
	'''
	根据txhash获取退质押或者投票利息信息
	:param api_name:
	:param params: txhash
	:return: {}
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getChangeCycle","params":"", "id": 3}' -H "Content-Type:application/json"
	响应：
	{"jsonrpc":"2.0","id":3,"result":"{100}"}
	'''
	try:
		result = request_Api(api_name, params)
		print("获取出块节点换届周期成功,{}".format(result))
		return result
	except Exception as e:
		print("获取出块节点换届周期失败,{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "chain_getChangeCycle"
	params = [""]
	chain_getChangeCycle(api_name, params)



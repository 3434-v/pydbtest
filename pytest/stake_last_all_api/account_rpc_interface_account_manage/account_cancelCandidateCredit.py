#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_cancelCandidateCredit.py
@time: 2020/1/8 5:43 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''13. account_CancelCandidateCredit'''


def cancelCandidateCredit(api_name, params):
	'''
	取消候选
	:param api_name: account_cancelCandidateCredit
	:param params: 发起转账的地址;接受者的地址;金额;gas价格;gas上线;备注
	:return: 交易地址
	示例代码
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_cancelCandidateCredit","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5","0x111","0x110","0x30000",""],"id":1}' http://127.0.0.1:15645
	'''
	try:
		result = request_Api(api_name, params)
		print("取消候选成功，返回值为{}".format(result))
		return result
	except Exception as e:
		print("取消候选失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "account_cancelCandidateCredit"
	params = ["0x9aD84792B8B88fA11Ac9DcE0615D8D3DA0A269d4", "0xd3c21bcecceda1000000", "0x110", "0x30000", ""]
	cancelCandidateCredit(api_name, params)

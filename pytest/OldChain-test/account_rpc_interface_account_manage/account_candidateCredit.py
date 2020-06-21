#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_candidateCredit.py
@time: 2020/1/8 5:43 下午
@desc:
'''


from stake_last_all_api.API import request_Api

'''12. account_CandidateCredit   候选节点质押'''


def candidateCredit(api_name, params):
	'''
	作用：候选节点质押
	:param api_name: "account_candidateCredit"
	:param params: 发起转账的地址；接受者的地址；金额；gas价格；gas上线；用户pubkey ip等信息
	:return: 交易地址
	示例代码
	curl -H "Content-Type: application/json" -X post --data '{"jsonrpc":"2.0","method":"account_candidateCredit","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5","0x111","0x110","0x30000","{\"Pubkey\":\"0x020e233ebaed5ade5e48d7ee7a999e173df054321f4ddaebecdb61756f8a43e91c\",\"Node\":\"192.168.31.51:55555\"}"],"id":1}' http://127.0.0.1:15645
	'''
	try:
		result = request_Api(api_name, params)
		print("候选投票成功，返回值为{}".format(result))
		return result
	except Exception as e:
		print("候选投票失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	for i in range(1):
		api_name = "account_candidateCredit"
		params = ["0xB490Ffa71d9d1D9f4472FBc46eE6e4FFd2bb486b", "0xd3c21bcecceda1000000", "0x110", "0x30000", "{\"Pubkey\":\"0x02c03851e2223a973968f3b1e14fb3308e221634bfdba64f156a882678b2696461\",\"Node\":\"enode://328bcd41c37a7cb9382048f1ec6b9b546f7b261c1177dcf992859a665cc664ca@39.98.39.224:44444\"}"]
		candidateCredit(api_name, params)

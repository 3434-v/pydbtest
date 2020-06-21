#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: trace_decodeTrasnaction.py
@time: 2020/1/8 5:35 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''3. trace_decodeTrasnaction'''


def decodeTrasnaction(api_name, params):
	'''
	把交易字节信息反解析成交易详情
	:param api_name: "trace_decodeTrasnaction"
	:param params: 交易字节信息
	:return: 交易详情
	示例代码
	curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_decodeTrasnaction","params":["0x02a7ae20007923a30bbfbcb998a6534d56b313e68c8e0c594a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002011102011003030000bc9889d00b004120eba14c77eab7a154833ff14832d8769cfc0b30db288445d6a83ef2fe337aa09042f8174a593543c4acabe7fadf1ad5fceea9c835682cb9dbea3f1d8fec181fb9"], "id": 3}' -H "Content-Type:application/json"
	'''
	try:
		result = request_Api(api_name, params)
		print("把交易字节信息反解析成交易详情，返回值为{}".format(result))
		return result
	except Exception as e:
		print("把交易字节信息反解析成交易详情api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "trace_decodeTrasnaction"
	params = [
		"0x02a7ae20007923a30bbfbcb998a6534d56b313e68c8e0c594a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002011102011003030000bc9889d00b004120eba14c77eab7a154833ff14832d8769cfc0b30db288445d6a83ef2fe337aa09042f8174a593543c4acabe7fadf1ad5fceea9c835682cb9dbea3f1d8fec181fb9"]
	decodeTrasnaction(api_name, params)

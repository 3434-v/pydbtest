#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: trace_getTransaction.py
@time: 2020/1/8 5:35 下午
@desc:
'''

'''
2. trace_getTransaction
作用：根据交易hash查询交易详细信息
参数：

交易hash
返回值：交易详细信息
示例代码
请求：
curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"trace_getTransaction","params":["0x00001c9b8c8fdb1f53faf02321f76253704123e2b56cce065852bab93e526ae2"], "id": 3}' -H "Content-Type:application/json"
响应：
{
	  "jsonrpc": "2.0",
	  "id": 3,
	  "result": {
		"Hash": "0x00001c9b8c8fdb1f53faf02321f76253704123e2b56cce065852bab93e526ae2",
		"From": "0x7923a30bbfbcb998a6534d56b313e68c8e0c594a",
		"Version": 1,
		"Nonce": 530215,
		"Type": 0,
		"To": "0x7923a30bbfbcb998a6534d56b313e68c8e0c594a",
		"ChainId": "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
		"Amount": "0x111",
		"GasPrice": "0x110",
		"GasLimit": "0x30000",
		"Timestamp": 1560356382,
		"Data": null,
		"Sig": "0x20eba14c77eab7a154833ff14832d8769cfc0b30db288445d6a83ef2fe337aa09042f8174a593543c4acabe7fadf1ad5fceea9c835682cb9dbea3f1d8fec181fb9"
	  }
	}


'''
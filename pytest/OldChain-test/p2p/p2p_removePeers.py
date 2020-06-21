#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: p2p_removePeers.py
@time: 2020/1/8 5:33 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''p2p_removePeers
作用：移除节点
返回值：
示例代码
请求：
"enode://e1b2f83b7b0f5845cc74ca12bb40152e520842bbd0597b7770cb459bd40f109178811ebddd6d640100cdb9b661a3a43a9811d9fdc63770032a3f2524257fb62d@192.168.74.1:55555"
响应：
'''


def removePeers(api_name, params):
	try:
		result = request_Api(api_name, params)
		print("移除节点成功，{}".format(result))
		return result
	except Exception as e:
		print("移除节点失败，api返回为{}".format(e))
		return -1


if __name__ == '__main__':
	api_name = "p2p_removePeer"
	params = [
		"enode://e1b2f83b7b0f5845cc74ca12bb40152e520842bbd0597b7770cb459bd40f109178811ebddd6d640100cdb9b661a3a43a9811d9fdc63770032a3f2524257fb62d@192.168.74.1:44444"]
	removePeers(api_name, params)

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import requests
import xlwt
import logging
from apis.log import Logger


def request_Api(api_name, params):
	"""
    通用HTTP 发送请求
	:param api_name:   接口名
	:param params:     参数
	:return:
	"""
	("api名字: {}  -- 参数: {}".format(api_name, params))
	url = "http://39.98.39.224:35645"
	# url = "http://127.0.0.1:35645"
	# url = "http://39.100.111.74:35645"
	# url = "http://118.25.154.186:35645"
	# url = "http://47.240.254.234:35645"
	# url = "http://154.197.27.232:35645"
	# url = "http://192.168.31.219:15645"

	payload = {
		'jsonrpc': '2.0',
		'method': api_name,  # 'chain_getBalance'
		'params': params,  # ['0xad3dc2d8aedef155eaba42ab72c1fe480699336c'],
		'id': 3
	}
	logging.info("参数:{},payload:{}".format(params, payload))
	payload = json.dumps(payload)
	
	headers = {
		'Content-Type': "application/json",
		'cache-control': "no-cache",
		'Postman-Token': "27a29181-18f4-4549-80c2-d23196a7df15"
	}
	try:
		response = requests.request("POST", url, data=payload, headers=headers)
		logging.info(response.text)
		jsonDic = json.loads(response.text)
		return jsonDic
	except Exception as e:
		logging.error("接口报错".format(e))
		return -1  # -1 默认接口调用失败


def save_excel(account, result, sheet1_name, sheet2_name, file_name):
	'''
	list写入EXcel
	:param account: 输入第一列内容
	:param result: 输入第二列内容
	:param sheet1_name: 输入表格第一列名称
	:param sheet2_name: 输入表格第二列名称
	:param file_name: 文件名字
	:return: Excel
	'''
	f = xlwt.Workbook()  # 创建工作簿
	sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
	# 写入内容，设置表头为账号,金额
	sheet1.write(0, 0, sheet1_name)
	sheet1.write(0, 1, sheet2_name)
	j = 1
	s = 1
	for ac in account:
		sheet1.write(j, 0, ac)  # 循环写入 竖着写
		j = j + 1
	for i in result:
		sheet1.write(s, 1, i)  # 循环写入 竖着写
		s = s + 1
	f.save('{}.xls'.format(file_name))  # 保存文件


if __name__ == '__main__':
	log = Logger(filename='../logs/API.log', level='info')
	a = request_Api(api_name="account_createAccount", params=[])

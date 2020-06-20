#!/usr/bin/env python
# encoding: utf-8
'''
@author: caroline
@license: (C) Copyright 2019-2022, Node Supply Chain Manager Corporation Limited.
@contact: caroline.fang.cc@gmail.com
@software: pycharm
@file: account_unlockAccount.py
@time: 2020/1/8 5:40 下午
@desc:
'''

from stake_last_all_api.API import request_Api

'''5. account_account_unlockAccount'''


def unlockAccount(api_name, params):
	'''
	解锁账号
	:param api_name: account_unlockAccount
	:param params:账号地址
	:return: 失败返回错误原因，成功不返回任何信息
	示例代码
	curl  http://39.98.39.224:35645 -X POST --data '{"jsonrpc":"2.0","method":"account_unlockAccount","params":["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c"], "id": 3}' -H "Content-Type:application/json"
	'''
	
	try:
		result = request_Api(api_name, params)
		print("转账成功，地址为{}".format(result))
		return result
	except Exception as e:
		print("转账失败，api返回错误，返回值为{}".format(e))
		return -1


if __name__ == '__main__':
	addrs = ['0x72fbad34459b1d0f9984dd295261887c661ee841', '0x577aff8b6773a6cafd6aadbb0b0b3e9665fc42f6',
			 '0x9ec73a447b6dc1fc72736887cbd180e255ef09f3', '0x3fe98a15ec576f8aa7f8e18352b9fa05dba3a77a',
			 '0x9023d52c4ea6993d0eef4b3c856c5c051a871e11', '0x9ea3754d1f9b968efdc20528f0192ef25e59611c',
			 '0xd2034451d6624dca53dad80c9bae9c53adc8f338', '0xc241ceded13e5d4ff7217253047a40f57ee0b985',
			 '0xb68e455bda3e37ed5a87167b107e125b0b18808e', '0xc9312d7e2edd8680c9e99e15b37be21d913dad25',
			 '0x87b68353fc1335e61ae4b7dca911a7ad558a1f11', '0xea7fe43edba518bbb642909576dbe14e2c931e2c',
			 '0xbcd1e6bfbf25aab3ebdd84083855a17ca01e4b25', '0x9a29680e23e9aafc615f0eff066617856c152938',
			 '0x17c73cef41e22ac8adda071f4f66f0fcd976c129', '0x15fd240a553ac596d6c65f4d128d12a28d04d7be',
			 '0x18d953d11f670179eee9f0309e77977518bb1e9f', '0xd4b4e8a57b49319b8706937ba60c6350d8811ba8',
			 '0xb01b2dca9f9b40f4e2d31e1f00560b16223e4287', '0xa411260aef74fb1d36f8a07310d42b356f9d5357',
			 '0x3155d2ca715772ee687dccb87345f75b86b7b3c7', '0x4d8a55ac670d8d3fbfe9fc1d4ef6afc0b68105c6',
			 '0x596e880e7962c177d18f7db62c70882b041a85b4', '0x5de780b8412fc2977e158ac60cc6d9bfce7a1e9f',
			 '0x990abadb5d43e6d13be7fb7f5e6798b6d9d74297', '0x91749be41d456d3e29bb6b60415fc7291cf5b8a1',
			 '0x3c03d972b70ed891335b63cef8ceeef399e128a5', '0x9e51d0696a5ba9b871754110aa64e881b11cd69a',
			 '0xa279c2887a2bfab6327cb8389d858c9333bd4b46', '0xebe551a3460eae110a275a57a0cb0e260978a46a',
			 '0xebce82bccfcc2edde722d0f3a0fb2e82acbddd1c', '0x446aac9e444613b172a4968cc431a984b69f320f',
			 '0x49de216d11e162f9bf1eadb8f5e14c3d1923bf27', '0x573f9d85d6feb1c87910d733d9c372d4640e5e7b',
			 '0x375135b2ac2968c08c04f4ebe9eaa5e105bddf49', '0x5b732b5b8199af48c8b78b98d5b2a0be483f3e14',
			 '0x2e59b11dd0221ec8776662a35aa9f5c3b79b946c', '0xd6e1b15eddd2e93fe48e62583fd32c22044e7b6f',
			 '0x90033092c0797db9528b6963ab0a9d9f28679181', '0xd1233d1d61f919d0d44661349728bce594fcc3a1',
			 '0x695686cfc39d9f06794da2bc68e6abeed9e955e6', '0xee91efe703be64b08f6c5fd91fee9ae3813ccfe5',
			 '0x712f7df84303d953870540b43c21bcffd2dae12c', '0xb0a784fbf41bb6bddd308fbceea8c58c94d34526',
			 '0xe1e956a75c3f6f57fe687f0b83e51edf02a005ba', '0xe24bd83418624e641bcd6e22e027f33477d22e34',
			 '0x4f831f2bab486e73f7d3cc70db7d1541767094cf', '0x7409be9d7cce96b2660a0c6fa5c0dfba027a9ea6',
			 '0x8ccdb4165e125ec4617535eef52e710742a47af9', '0x5bc1782f0f59de815b70a534fe2ae5792b4da186',
			 '0xf66b24217798de4600a079c8b7bcfa8acfdd5c80', '0xd36e9299aca1a32776b8cdedaceecc0bee8f693d',
			 '0xeeca8879721045b27b05c592b5f82601f5ae87f0', '0xa7f22ee6dd46df92470313eb7794a4ab3eff5c98',
			 '0xe5915990ae66a2abe07df7ea09c25a9c7405ba83', '0x1a660a30e7f578f28f28d6f1d6ade0843757895f',
			 '0x98dbd76d2731b9b27172b08c864473bc10e2966d', '0xe73fd0a5161eec0585ceadaa2c18040c4677a972',
			 '0xfff3ef8cced8b35837dd48798c826241324362b5', '0x8d64991e4dca06f7d10fa88e6f14b39b06c5cfdf',
			 '0xd8b15fe38eaf7d289885f46ba3fe5a4039f10a23', '0x474da9675de3f918bdbdb6f0d7d285064ef34a0c',
			 '0x37f436d39093c312a6145f17cce7fa04a9570620', '0x4eceecf468d2f4d985537d530fad938b9583810a',
			 '0x5cfa74d261514774c647b671fb36f7ab3c4f4f1c', '0x1bc97ca5e63e25843b9ed636c10f0b38ee16ff1f',
			 '0x86ae857bf0193630c40853b15cef08d26ace97ba', '0xc78a80b2f5be10d78f9f4d888845953d2f9ff400',
			 '0x3202172fa3b58d78e2963f28fdd2367d4f3abf83', '0xda85131e40ea08c05628f7708e20e0068315f018',
			 '0x8f5c10ee9c6a543beb7e6b5464ca5f196d678c33', '0x1a0e45ac31edf54c3ea212461d5301247cdffa29',
			 '0xb22a413cc762222275d06db3fc56ac49c88d0ed7', '0x517f99b57eda71fd52cf43133c040972d20f7f2d',
			 '0x3127bcbde2b0cc1c963e44a9c29a2883a33a301e', '0x1f38aa88949e858e0fd611ea272ea596555363c1',
			 '0xcc0fd14cb9e50357fea53fa45b7cc0351dada728', '0x3ab375b4ad8d4a770b8662072cae26c92ccdb82c',
			 '0xae4543c02412a208a53f2fdf56ee3e5d943022a0', '0x6511f783077f1c2fc1bbb0a83aa75d248258e528',
			 '0xc00b7fd2a605c9bced1d73a66f5e7f1e88c177e6', '0x35a49641e78500c79ae60fe02a153e49cf899971',
			 '0x01f24c6415bbce8c426185dabe0e3995583d1372', '0x8eca2b45002d56c8d10229c96652a5dea90302ec',
			 '0xc33e7be3f12ecbe11d566de9aa7552c0b6aae9d5', '0x7d1d99b761457d8905c16e2bd6022282d53135fd',
			 '0xef2bb3fc203b8cb6a245ef31ad8d169ffd78b801', '0x3275ad121a4ba9d38c963783e9a3fb11ac1ee6d1',
			 '0xff8d52bb3337b42c4f717cd742f5b38a193cac07', '0xc391cdeb69490ed54f0a017afcbbde26a48b7a0d',
			 '0xeba7e6584a92cf1273d1d3a5fa6faf188173d08c', '0x20170a0d5209cb757293f85c08bb77d20aaf5baf',
			 '0xca345d024bc00eee65bdfb802262f71b37ca6415', '0x6b2eb86ade050d58899705582d5234bccdd28a37',
			 '0xf04957c69e18eb4867901eb732ffc9c5bb15e4b6', '0x7a9eec03141a2937baa0d385f7e68867a5e3e499',
			 '0x80b9cab400732a98545420cd26c2c4f44b086420', '0xa882b9650bb89b82279cf36bb4553e3f93631553',
			 '0x80f90500d6e080b37a4c500b64eb412bd0e1abfa', '0xb5b8e571024ce2f1c8605ef72657e41d535b5948']
	for i in range(len(addrs)):
		api_name = "account_unlockAccount"


		params = [addrs[i], "123456"]
		# params = ["0xB490Ffa71d9d1D9f4472FBc46eE6e4FFd2bb486b"]
		# params = ["0xf0FD4230c00f85B0EC32D6eD2Fd4B52dE408b660"]
		# params = ["0x9ec31b099f48e20e40698f928ae1b75e114965a9"]
		# params = ["0x7b1cAdA0C9c25Eb2E1dE5e5A03a407D11c45b3DE"]
		# params = ["0xAa9f9063000e783924CC0A507bb51936dDD018ab"]
		print("共计账号",len(addrs),"个，","正在解锁第", i, "个账号")

		unlockAccount(api_name, params)
import requests
import re,json,os
import random
import time
from py_mongodb import TestMongoDB 
pynosql = TestMongoDB('localhost:27017/','test_drep')

header = {
		    'Content-Type':'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
		}

#简单的实际处理
def get_time():

    otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return otherStyleTime

#预处理数据格式转换
def dict_msg(name,method,describe):

    method_dict = {"name":name,"method":method,"describe":describe}
    return method_dict

#调试模式
def Debug(msg):
    print("Debug:--------------------"+msg+"------------------")

#db数据处理方法
def stropway(CollectionName,Term,update_msg,message):

    # CollectionName = 'result_msg'
    Term = {"method":Term}
    count = pynosql.StropExist(CollectionName,Term)
    if count:
        pynosql.update(CollectionName,Term,update_msg)
    else:
        pynosql.insert(CollectionName,message)

#公共方法类
class General(object):

    def __init__(self,CollectionName,url):
        self.CollectionName = CollectionName
        self.url = url

    def get_method(self,Term):
        method = pynosql.select(self.CollectionName,Term,'method')
        return method

    def General_way(self,method,params):

        payload = '{"jsonrpc":"2.0","method":"'+method+'","params":'+params+', "id": 3}'
        print("请求参数:{}".format(payload))
        response = requests.post(self.url,data=payload,headers=header)
        try:
            Collection = 'result_msg'
            result = json.loads(str(response.text))["result"]
            message = {"method":method,"result":result,"time":get_time()}
            stropway(Collection,method,message,message)
            print("正常返回结果:{}".format(response.text))


        except Exception as err:
            print("方法错误:{}".format(err))
            print("错误的结果:{}".format(response.text))

# 用于处理区块链偏上层逻辑
class BlockMgr(General):

    def __init__(self,CollectionName,url):
        super().__init__(CollectionName,url)
        
    # 发送已签名的交易
    def sendRawTransaction(self,DealHash):

        Term = {"name":"sendRawTransaction"}
        method = self.get_method(Term)
        params = '["'+DealHash+'"]'
        self.General_way(method,params)
        
    # 获取系统的给出的gasprice建议值
    def gasPrice(self):

        Term = {"name":"transfer"}
        method = self.get_method(Term)
        #获取第一条测试用例
        Term = {"TestID":1}
        testcase_list = dict(pynosql.select_testcase('TestCase',Term))
        Launch = testcase_list['Launch']
        Term = {"name":"gasPrice"}
        method = self.get_method(Term)
        params = '["'+Launch+'"]'
        self.General_way(method,params)

    # 获取交易池中的交易信息.
    def GetPoolTransactions(self,Site):

        Term = {"name":"GetPoolTransactions"}
        method = self.get_method(Term)
        params = '["'+Site+'"]'
        self.General_way(method,params)

    # 获取地址发出的交易总数
    def GetTransactionCount(self,Site):

        Term = {"name":"GetTransactionCount"}
        method = self.get_method(Term)
        params = '["'+Site+'"]'
        self.General_way(method,params)

    # 查询交易是否在交易池，如果在，返回交易
    def GetTxInPool(self,Site):

        Term = {"name":"GetTxInPool"}
        method = self.get_method(Term)
        params = '["'+Site+'"]'
        self.General_way(method,params)

 
# 链接口 用于获取区块信息
class chain(General):

    def __init__(self,CollectionName,url):
        super().__init__(CollectionName,url)

    # 用于获取区块信息
    def getblock(self,height):

        Term = {"name":"getblock"}
        method = self.get_method(Term)
        params = '["'+height+'"]'
        self.General_way(method,params)
    
    # 用于获取当前最高区块
    def getMaxHeight(self):
        
        Term = {"name":"getMaxHeight"}
        method = self.get_method(Term)
        params = '[""]'
        self.General_way(method,params)

    # 获取gas相关信息
    def getBlockGasInfo(self):

        Term = {"name":"getBlockGasInfo"}
        method = self.get_method(Term)
        params = '[""]'
        self.General_way(method,params)

    # 查询地址余额
    def getBalance(self,Site):

        Term = {"name":"getBalance"}
        method = self.get_method(Term)
        params = '["'+Site+'"]'
        self.General_way(method,params)
        

    # 查询地址在链上的nonce
    def getNonce(self):
        Term = {"name":"getNonce"}
        method = self.get_method(Term)
        Term = {"TestID":1}
        testcase_list = dict(pynosql.select_testcase('TestCase',Term))
        Launch = testcase_list['Launch']
        Term = {"name":"getNonce"}
        method = self.get_method(Term)
        params = '["'+Launch+'"]'
        self.General_way(method,params)

    # 查询地址的名誉值
    def getNonce_s(self):
        
    
        Term = {"TestID":1}
        testcase_list = dict(pynosql.select_testcase('TestCase',Term))
        Launch = testcase_list['Launch']
        Term = {"name":"getNonce_s"}
        method = self.get_method(Term)
        params = '["'+Launch+'"]'
        self.General_way(method,params)

    # 获取区块中特定序列的交易
    def getTransactionByBlockHeightAndIndex(self,height,order):
        
        Term = {"name":"getTransactionByBlockHeightAndIndex"}
        method = self.get_method(Term)
        params = '["'+height+'","'+order+'"]'
        self.General_way(method,params)
    
    # 根据地址获取地址对应的别名
    def getAliasByAddress(self,Site):
        
        Term = {"name":"getAliasByAddress"}
        method = self.get_method(Term)
        params = '["'+Site+'"]'
        self.General_way(method,params)

    # 根据别名获取别名对应的地址
    def getAddressByAlias(self,Site):

        Term = {"name":"getAddressByAlias"}
        method = self.get_method(Term)
        params = '["'+Site+'"]'
        self.General_way(method,params)


    # 根据txhash获取receipt信息
    def getReceipt(self,txhash):
        
        Term = {"name":"getReceipt"}
        method = self.get_method(Term)
        params = '["'+txhash+'"]'
        self.General_way(method,params)
    
    # 根据txhash获取交易log信息
    def getLogs(self,txhash):
        
        Term = {"name":"getLogs"}
        method = self.get_method(Term)
        params = '["'+txhash+'"]'
        self.General_way(method,params)


    # 根据txhash获取退质押或者退投票信息
    def getCancelCreditDetail(self,txhash):

        Term = {"name":"getCancelCreditDetail"}
        method = self.get_method(Term)
        params = '["'+txhash+'"]'
        self.General_way(method,params)
        


    # 根据地址获取bytecode
    def getByteCode(self,Site):

        Term = {"name":"getByteCode"}
        method = self.get_method(Term)
        params = '["'+Site+'"]'
        self.General_way(method,params)


    # 根据地址获取stake 所有细节信息
    def getVoteCreditDetails(self,Site):
        
        Term = {"name":"getVoteCreditDetails"}
        method = self.get_method(Term)
        params = '["'+Site+'"]'
        self.General_way(method,params)

    # 获取所有退票请求的细节
    def GetCancelCreditDetails(self,Site):
        
        Term = {"name":"getVoteCreditDetails"}
        method = self.get_method(Term)
        params = '["'+Site+'"]'
        self.General_way(method,params)

    
    # 获取所有候选节点地址和对应的信任值
    def GetCandidateAddrs(self,Site):
        
        Term = {"name":"GetCandidateAddrs"}
        method = self.get_method(Term)
        params = '["'+Site+'"]'
        self.General_way(method,params)

    # 获取3个月内、3-6个月、6-12个月、12个月以上的利率
    def getInterestRate(self):
        
        Term = {"name":"getInterestRate"}
        method = self.get_method(Term)
        params = '[""]'
        self.General_way(method,params)

    # 获取出块节点换届周期
    def getChangeCycle(self):
        
        Term = {"name":"getInterestRate"}
        method = self.get_method(Term)
        params = '[""]'
        self.General_way(method,params)

# p2p网络接口 设置查询网络状态

class p2p(General):

    def __init__(self,CollectionName,url):
        super().__init__(CollectionName,url)

    # 获取当前连接的节点
    def getPeers(self):
        
        Term = {"name":"getPeers"}
        method = self.get_method(Term)
        params = '[""]'
        self.General_way(method,params)


    # 添加节点
    def addPeer(self,enode):
        
        Term = {"name":"addPeer"}
        method = self.get_method(Term)
        params = '["'+enode+'"]'
        self.General_way(method,params)

    # 移除节点
    def removePeer(self,enode):

        Term = {"name":"removePeer"}
        method = self.get_method(Term)
        params = '["'+enode+'"]'
        self.General_way(method,params)

    # 需要获取本地的enode，用于P2p链接
    def localNode(self):

        Term = {"name":"localNode"}
        method = self.get_method(Term)
        params = '[""]'
        self.General_way(method,params)



# 日志rpc接口 设置日志级别

class log(General):

    def __init__(self,CollectionName,url):
        super().__init__(CollectionName,url)


    # 设置日志级别
    def setLevel(self,caste):
        
        Term = {"name":"setLevel"}
        method = self.get_method(Term)
        params = '["'+caste+'"]'
        self.General_way(method,params)


    # 分模块设置级别
    def setVmodule(self,caste_msg):
        
        Term = {"name":"setVmodule"}
        method = self.get_method(Term)
        params = '["'+caste_msg+'"]'
        self.General_way(method,params)


# 记录接口 查询交易地址等信息（需要开启记录模块）
class trace(General):

    def __init__(self,CollectionName,url):
        super().__init__(CollectionName,url)


    # 根据交易hash查询交易字节
    def getRawTransaction(self,txhash):

        Term = {"name":"getRawTransaction"}
        method = self.get_method(Term)
        params = '["'+txhash+'"]'
        self.General_way(method,params)

    # 根据交易hash查询交易详细信息
    def getTransaction(self,txhash):
        
        Term = {"name":"getTransaction"}
        method = self.get_method(Term)
        params = '["'+txhash+'"]'
        self.General_way(method,params)
    
    # 把交易字节信息反解析成交易详情
    def decodeTrasnaction(self,DealByte):
        
        Term = {"name":"decodeTrasnaction"}
        method = self.get_method(Term)
        params = '["'+DealByte+'"]'
        self.General_way(method,params)


    # 根据地址查询该地址发出的交易，支持分页//无效
    def getSendTransactionByAddr(self,Site,begin,end):

        Term = {"name":"getSendTransactionByAddr"}
        method = self.get_method(Term)
        params = '["'+Site+'","'+str(begin)+'","'+str(end)+'"]'
        self.General_way(method,params)

    
    # 根据地址查询该地址接受的交易，支持分页//无效
    def getReceiveTransactionByAd(self,Site,begin,end):
        
        Term = {"name":"getReceiveTransactionByAd"}
        method = self.get_method(Term)
        params = '["'+Site+'","'+begin+'","'+end+'"]'
        self.General_way(method,params)

    # 重建trace中的区块记录
    def rebuild(self,begin,end):
        
        Term = {"name":"rebuild"}
        method = self.get_method(Term)
        params = '["'+begin+'","'+end+'"]'
        self.General_way(method,params)

    
# 账号rpc接口 地址管理及发起简单交易

class account(General):

    def __init__(self,CollectionName,url):
        super().__init__(CollectionName,url)

   
    # 列出所有本地地址
    def listAddress(self):
        
        Term = {"name":"listAddress"}
        method = self.get_method(Term)
        params = '[""]'
        self.General_way(method,params)


    # 创建本地账号
    def createAccount(self):

        Term = {"name":"createAccount"}
        method = self.get_method(Term)
        params = '[""]'
        self.General_way(method,params)

    
    # 创建本地钱包
    def createWallet(self,password):
        
        Term = {"name":"createWallet"}
        method = self.get_method(Term)
        params = '["'+password+'"]'
        self.General_way(method,params)
        
    
    # 锁定账号
    def lockAccount(self,Site):

        Term = {"name":"lockAccount"}
        method = self.get_method(Term)
        params = '["'+Site+'"]'
        self.General_way(method,params)
    
    # 解锁账号
    def account_unlockAccount(self,Site,password):

        Term = {"name":"account_unlockAccount"}
        method = self.get_method(Term)
        params = '["'+Site+'","'+password+'"]'
        self.General_way(method,params)
        

    # 打开钱包
    def openWallet(self,password):
        
        Term = {"name":"openWallet"}
        method = self.get_method(Term)
        params = '["'+str(password)+'"]'
        self.General_way(method,params)

    
    # 关闭钱包
    def closeWallet(self):
        
        Term = {"name":"closeWallet"}
        method = self.get_method(Term)
        params = '[""]'
        self.General_way(method,params)
    
    # 转账
    def transfer(self):

        Term = {"name":"transfer"}
        method = self.get_method(Term)
        #获取第一条测试用例
        Term = {"TestID":1}
        testcase_list = dict(pynosql.select_testcase('TestCase',Term))
        Launch = testcase_list['Launch']
        Receive = testcase_list['Receive']
        money = hex(testcase_list['money'] * (10**18))
        gasprice = hex(testcase_list['gasprice'])
        gaslimt = hex(testcase_list['gaslimt'])
        params = '["'+Launch+'","'+Receive+'","'+money+'","'+gasprice+'","'+gaslimt+'",""]'
        self.General_way(method,params)

    # 转账
    def transferWithNonce(self,nonce):
        
        Term = {"name":"transferWithNonce"}
        method = self.get_method(Term)
        Term = {"TestID":1}
        testcase_list = dict(pynosql.select_testcase('TestCase',Term))
        Launch = testcase_list['Launch']
        Receive = testcase_list['Receive']
        money = hex(testcase_list['money'] * (10**18))
        gasprice = hex(testcase_list['gasprice'])
        gaslimt = hex(testcase_list['gaslimt'])
        params = '["'+Launch+'","'+Receive+'","'+money+'","'+gasprice+'","'+gaslimt+'","",'+nonce+']'
        self.General_way(method,params)

    
    # 设置别名
    def setAlias(self):

        Term = {"name":"setAlias"}
        method = self.get_method(Term)
        mingas = hex(272)
        maxgas = hex(196608)
        name = 'TomCats'
        Launch = '0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c'
        params = '["'+Launch+'","'+name+'","'+mingas+'","'+maxgas+'"],"id":3}'
        self.General_way(method,params)

    # 投票
    def VoteCredit(self):
        
        Term = {"name":"VoteCredit"}
        method = self.get_method(Term)
        Term = {"TestID":1}
        testcase_list = dict(pynosql.select_testcase('TestCase',Term))
        Launch = testcase_list['Launch']
        Receive = testcase_list['Receive']
        money = hex(testcase_list['money'])
        gasprice = hex(testcase_list['gasprice'])
        gaslimt = hex(testcase_list['gaslimt'])
        params = '["'+Launch+'","'+Receive+'","'+money+'","'+gasprice+'","'+gaslimt+'"]'
        self.General_way(method,params)

    # 取消投票
    def CancelVoteCredit(self):
        
        Term = {"name":"CancelVoteCredit"}
        method = self.get_method(Term)
        Term = {"TestID":1}
        testcase_list = dict(pynosql.select_testcase('TestCase',Term))
        Launch = testcase_list['Launch']
        Receive = testcase_list['Receive']
        money = hex(testcase_list['money'])
        gaslimt = hex(testcase_list['gaslimt'])
        params = '["'+Launch+'","'+Receive+'","'+money+'","'+money+'","'+gaslimt+'"]'
        self.General_way(method,params)


    # 候选节点质押
    def CandidateCredit(self,Site,Pubkey,Node):
        
        Term = {"name":"CandidateCredit"}
        method = self.get_method(Term)
        payload = {"jsonrpc":"2.0","method":method,"params":[Site,"0x111","0x110","0x30000","{\"Pubkey\":\""+Pubkey+"\",\"Node\":\""+Node+"\"}"],"id":3}
        response = requests.post(self.url,json=payload,headers=header)
        print(response.text)

    # 取消候选
    def CancelCandidateCredit(self):
        
        Term = {"name":"CancelCandidateCredit"}
        method = self.get_method(Term)
        Term = {"TestID":1}
        testcase_list = dict(pynosql.select_testcase('TestCase',Term))
        Launch = testcase_list['Launch']
        Receive = testcase_list['Receive']
        money = hex(testcase_list['money'])
        gaslimt = hex(testcase_list['gaslimt'])
        params = '["'+Launch+'","'+Receive+'","'+money+'","'+gaslimt+'"]'
        self.General_way(method,params)

    # 读取智能合约（无数据被修改）
    def readContract(self):
        
        Term = {"name":"CancelCandidateCredit"}
        method = self.get_method(Term)
    
    # 估算交易需要多少gas
    def estimateGas(self):
        
        Term = {"name":"estimateGas"}
        method = self.get_method(Term)
        Term = {"TestID":1}
        testcase_list = dict(pynosql.select_testcase('TestCase',Term))
        Launch = testcase_list['Launch']
        Receive = testcase_list['Receive']
        money = hex(testcase_list['money'])
        params = '["'+Launch+'","'+money+'","","'+Receive+'"]'
        self.General_way(method,params)

    # 执行智能合约（导致数据被修改）
    def executeContract(self):
        pass

    # 部署合约
    def createCode(self):
        pass

    # 导出地址对应的私钥
    def dumpPrivkey(self,Site):
        
        Term = {"name":"dumpPrivkey"}
        method = self.get_method(Term)
        params = '["'+Site+'"]'
        self.General_way(method,params)


    
    # 导出地址对应的公钥
    def DumpPubkey(self,Site):

        Term = {"name":"DumpPubkey"}
        method = self.get_method(Term)
        params = '["'+Site+'"]'
        self.General_way(method,params)

    
    # 关闭钱包
    def sign(self,Site,txhash):
        
        Term = {"name":"sign"}
        method = self.get_method(Term)
        params = '["'+Site+'","'+txhash+'"]'
        self.General_way(method,params)


    # 生成其他链的地址
    def generateAddresses(self,DrepSite):
        
        Term = {"name":"generateAddresses"}
        method = self.get_method(Term)
        params = '["'+DrepSite+'"]'
        self.General_way(method,params)
    
    # 导入keystore
    def importKeyStore(self,keystore,password):

        Term = {"name":"importKeyStore"}
        method = self.get_method(Term)
        params = '["'+keystore+'","'+password+'"]'
        self.General_way(method,params)

    
    # 导入私钥
    def importPrivkey(self,privkey):
        
        Term = {"name":"importPrivkey"}
        method = self.get_method(Term)
        params = '["'+privkey+'"]'
        self.General_way(method,params)


# 共识rpc接口 查询共识节点功能
class consensus(General):

    def __init__(self,CollectionName,url):
        super().__init__(CollectionName,url)

    # 修改leader等待时间 (ms)
    def changeWaitTime(self,stime):

        Term = {"name":"changeWaitTime"}
        method = self.get_method(Term)
        params = '["'+stime+'"]'
        self.General_way(method,params) 

    # 获取当前出块节点
    def getMiners(self):
        
        Term = {"name":"getMiners"}
        method = self.get_method(Term)
        params = '[""]'
        self.General_way(method,params)

url = 'http://39.98.39.224:35645'
CollectionName = 'method'
# url = "http://127.0.0.1:35645"
consensus = consensus(CollectionName,url)
account = account(CollectionName,url)
trace = trace(CollectionName,url)
log = log(CollectionName,url)
p2p = p2p(CollectionName,url)
chain = chain(CollectionName,url)
BlockMgr = BlockMgr(CollectionName,url)


# account_VoteCredit  
# account_CancelVoteCredit 
# account_CandidateCredit 
# account_CancelCandidateCredit

#投票场景各接口情况验证

def CandidateCredit_Scene():

    #候选
    Site = '0xd6e1b15eDDd2e93FE48e62583FD32C22044e7B6f'
    account.DumpPubkey(Site)
    CollectionName = 'result_msg'
    Trem = {"method":"account_dumpPubkey"}
    Pubkey =  pynosql.select(CollectionName,Trem,'result')
    # print(Pubkey)
    p2p.localNode()
    Trem = {"method":"p2p_localNode"}
    enode =  pynosql.select(CollectionName,Trem,'result')
    enodes = enode.strip('@127.0.0.1:44444') + '@192.168.3.22:44444'
    account.CandidateCredit(Site,Pubkey,enodes)

    time.sleep(3)
    #取消候选
    account.CancelCandidateCredit()



def VoteCredit_Scene():

    enode = 'enode://328bcd41c37a7cb9382048f1ec6b9b546f7b261c1177dcf992859a665cc664ca@192.168.31.245:44444'
    pubkey = '0x03f4e810a0741ff81765a2872675fe7bc54372f2619489d1dae269ddf19305d7aa'
    #发起投票
    Debug('发起投票')
    account.VoteCredit()
    CollectionName = 'result_msg'
    Trem = {"method":"account_voteCredit"}
    txhash = pynosql.select(CollectionName,Trem,'result')
    chain.getCancelCreditDetail(txhash) #查询投票数据
    time.sleep(5)
    #取消投票
    Debug('取消投票')
    account.CancelVoteCredit()
    Trem = {"method":"account_cancelVoteCredit"}
    txhash = pynosql.select(CollectionName,Trem,'result')
    # chain.getCancelCreditDetail(txhash) #查询取消数据
    # trace.getTransaction(txhash)
    #退票细节
    Debug('退票细节')
    Site = '0xd6e1b15eDDd2e93FE48e62583FD32C22044e7B6f'
    chain.GetCancelCreditDetails(Site)
    chain.GetCandidateAddrs(Site)
    Debug('根据地址查询该地址发出的交易，支持分页')
    trace.getSendTransactionByAddr(Site,1,10)
    Debug('获取交易池中的交易信息')
    BlockMgr.GetPoolTransactions(Site)
    Debug('查询交易是否在交易池')
    BlockMgr.GetTxInPool(txhash)
    Debug('根据地址获取bytecode')
    chain.getByteCode(Site)

    # account.listAddress()
    # account.createAccount()
    #查询投票人发出的交易
    # p2p.getPeers()
    # p2p.addPeer(enode)
    # account.account_unlockAccount(Site)
    # p2p.localNode()
    # account.DumpPubkey(Site)

    # account.transfer()
    #gasprice
    # BlockMgr.gasPrice()
    #gaslimt上限
    # account.estimateGas()
    # chain.getNonce()
    # account.transferWithNonce('1421')
    # BlockMgr.gasPrice()

def test3():
    # account.account_unlockAccount('0x1A61B43d6e53954735dd300D5090599A17F8E4db','123456')
    BlockMgr.GetPoolTransactions('0x1A61B43d6e53954735dd300D5090599A17F8E4db')

#获取本地所有地址的余额以及存储
def GetMoneyAddress():
    # account.openWallet('1234567')
    
    # account.transfer()
    CollectionName = 'result_msg'
    Trem = {"method":"account_listAddress"}
    address_list = pynosql.select(CollectionName,Trem,'result')
    for addres in address_list:
        chain.getBalance(addres)
        money = pynosql.select('result_msg',{"method":"chain_getBalance"},"result")
        message = {"address":addres,"money":money}
        pynosql.insert('MoneyCount',message)
    # account.listAddress()

    # chain.getBalance('0x8c944f5db5ed9395dc5b33d1cab1974fa7199e4c')
    # chain.getBalance('0xB7c5F20eED9d0834b97348142A616CE449510009')
    # GetPoolTransactions
    # print((961999886992010000000)/(10**18))
    
    # BlockMgr.GetPoolTransactions('0xB7c5F20eED9d0834b97348142A616CE449510009')
    # BlockMgr.GetTxInPool('0x5117560b34cc3c87d3447fa0b4b66b523e17299232ec69f81488c42ae7eaa487')
    # getBlockGasInfo
    # account.VoteCredit()
    # chain.getBalance('0x6c09dc42420b79b1222bd62d964e9e2dccc558ea')
    # chain.GetCandidateAddrs('0xb490ffa71d9d1d9f4472fbc46ee6e4ffd2bb486b')

def test4():
    # account.listAddress()
    pass


if __name__ == "__main__":

    # VoteCredit_Scene()
    # CandidateCredit_Scene()
    test3()
    # test4()
    

'''

class Drep_Deal(object):

    def __init__(self,url):
        self.url = url

    def get_time(self):
        otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return otherStyleTime

    def Gaslimit(self):
        url = 'http://39.98.39.224:35645'
        Launch = '0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c'
        data = '{"jsonrpc":"2.0","method":"blockmgr_gasPrice","params":["'+Launch+'"], "id": 3}'
        response = requests.post(url,data=data,headers=header)
        result = json.loads(str(response.text))["result"]
        print(response.text)
        return result
        

    
    # def TestCase(self):
    #     money = 100
    #     gaslimt = self.Gaslimit()
    #     message = {"TestID":1,"Launch":"0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c","Receive":"0x28f8C33D0080Bde50F78bF30b84d7d1b8F676170","money":money,"gaslimt":gaslimt}
    #     CollectionName = 'TestCase'
    #     pynosql.insert(CollectionName,message)
    #     pynosql.select_testcase()

        

    #转账
    def Launch_Deal(self):

        CollectionName = 'transfer_recode'
        #获取第一条测试用例
        Term = {"TestID":1}
        testcase_list = dict(pynosql.select_testcase('TestCase',Term))
        Launch = testcase_list['Launch']
        Receive = testcase_list['Receive']
        money = hex(testcase_list['money'])
        gaslimt = hex(testcase_list['gaslimt'])
        data = '["'+Launch+'","'+Receive+'","'+money+'","'+money+'","'+gaslimt+'",""]'
        payload = '{"jsonrpc":"2.0","method":"account_transfer","params":'+data+',"id":1}'
        response = requests.post(self.url,data=payload,headers=header)
        result = json.loads(str(response.text))["result"]
        message = {"LaunchSite":Launch,"ReceiveSite":Receive,"DealHax":result,"transfer_money":money,"gaslimt":gaslimt}
        pynosql.insert(CollectionName,message)

    #创建本地账号
    def CreateAccount(self):

        payload = '{"jsonrpc":"2.0","method":"account_createAccount","params":[""], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        CollectionName = 'Create_Account'
        result = json.loads(str(response.text))["result"]
        message = {"Account":result,"Create_Time":self.get_time()}
        pynosql.insert(CollectionName,message)

    #创建本地钱包
    def Accountwallet(self):

        password = 'yangxun19990728'
        payload = '{"jsonrpc":"2.0","method":"account_createWallet","params":["'+password+'"], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)

    # 锁定账号
    def lockAccount(self):
        payload = '{"jsonrpc":"2.0","method":"account_lockAccount","params":["0x263a4164575772088860ac9d3192067eaae489f9"], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)

    # 解锁账号
    def unlockAccount(self):
        payload = '{"jsonrpc":"2.0","method":"account_unlockAccount","params":["0x263a4164575772088860ac9d3192067eaae489f9",""], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)

    #打开钱包
    def openWallet(self):
        payload = '{"jsonrpc":"2.0","method":"account_openWallet","params":["123"], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)

    # 获取当前出块节点
    def getMiners(self):
        payload = '{"jsonrpc":"2.0","method":"consensus_getMiners","params":[""], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)

    # 获取交易池中的交易信息
    def GetPoolTransactions(self):
        payload = '{"jsonrpc":"2.0","method":"blockmgr_getTxInPool","params":["0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c"], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)

    # 获取当前最高区块
    def getMaxHeight(self):
        payload = '{"jsonrpc":"2.0","method":"chain_getMaxHeight","params":[], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)
        height = json.loads(str(response.text))["result"]
        return height

    # 获取区块信息
    def getblock(self):
        height = str(self.getMaxHeight())
        payload = '{"jsonrpc":"2.0","method":"chain_getBlock","params":['+height+'], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)

    # 获取gas相关信息
    def getBlockGasInfo(self):
        
        payload = '{"jsonrpc":"2.0","method":"chain_getBlockGasInfo","params":[], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        # print(response.text)
        result = json.loads(str(response.text))["result"]
        result = json.loads(result)
        return result["MinGas"],result["MaxGas"],result["CurrentBlockGas"]
        # 系统需要的gas最小值、最大值；和当前块被设置的最大gas值
    
    #gas估值
    def gas_estimate(self):
        Term = {"TestID":1}
        testcase_list = dict(pynosql.select_testcase('TestCase',Term))
        Launch = testcase_list['Launch']
        Receive = testcase_list['Receive']
        # data = '["0xec61c03f719a5c214f60719c3f36bb362a202125","0xecfb51e10aa4c146bf6c12eee090339c99841efc","0x6d4ce63c","0x110","0x30000"]'
        payload = '{"jsonrpc":"2.0","method":"account_estimateGas","params":["'+Launch+'","'+Receive+'","0x110","0x110","0x30000"],"id":1}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)

    # 查询地址在链上的nonce
    def getNonce(self):

        Launch = '0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c'
        payload = '{"jsonrpc":"2.0","method":"chain_getNonce","params":["'+Launch+'"], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)

    # 根据地址获取地址对应的别名
    def getAliasByAddress(self):

        Launch = '0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c'
        payload = '{"jsonrpc":"2.0","method":"chain_getAliasByAddress","params":["'+Launch+'"], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)
    

    #设置地址别名
    def setAlias(self):
        # mingas,maxgas,currentnlockgas = self.getBlockGasInfo()
        mingas = hex(272)
        maxgas = hex(196608)
        name = 'TomCats'
        Launch = '0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c'
        payload = '{"jsonrpc":"2.0","method":"account_setAlias","params":["'+Launch+'","'+name+'","'+mingas+'","'+maxgas+'"],"id":3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)
        self.getAliasByAddress()

    # 投票
    def VoteCredit(self):
        Term = {"TestID":1}
        testcase_list = dict(pynosql.select_testcase('TestCase',Term))
        Launch = testcase_list['Launch']
        Receive = testcase_list['Receive']
        money = hex(testcase_list['money'])
        gaslimt = hex(testcase_list['gaslimt'])
        data = '["'+Launch+'","'+Receive+'","'+money+'","'+money+'","'+gaslimt+'"]'

        payload = '{"jsonrpc":"2.0","method":"account_voteCredit","params":'+data+',"id":1}'
        print(payload)
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)

    #取消投票
    def Cancel_VoteCredit(self):
        Term = {"TestID":1}
        testcase_list = dict(pynosql.select_testcase('TestCase',Term))
        Launch = testcase_list['Launch']
        Receive = testcase_list['Receive']
        money = hex(testcase_list['money'])
        gaslimt = hex(testcase_list['gaslimt'])
        data = '["'+Launch+'","'+Receive+'","'+money+'","'+money+'","'+gaslimt+'"]'
        payload = '{"jsonrpc":"2.0","method":"account_cancelVoteCredit","params":'+data+',"id":1}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)
        print(json.loads(str(response.text))["result"])
        return json.loads(str(response.text))["result"]

    # 根据txhash获取退质押或者退投票信息
    def getCancelCreditDetail(self):
        # txhash = self.Cancel_VoteCredit()
        txhash = '0x64fe1420e285543cd375e90198e660d2365154c4f79af8288d4ad0f13a253c1d'
        payload = '{"jsonrpc":"2.0","method":"chain_getCancelCreditDetail","params":["'+txhash+'"], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)

    # 获取所有退票请求的细节
    def GetCancelCreditDetails(self):

        Launch = '0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c'
        payload = '{"jsonrpc":"2.0","method":"chain_getCancelCreditDetails","params":["'+Launch+'"], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)

    # 需要获取本地的enode，用于P2p链接
    def p2p_localNode(self):

        data = '[]'
        payload = '{"jsonrpc":"2.0","method":"p2p_localNode","params":'+data+',"id":1}'
        response = requests.post(self.url,data=payload,headers=header)
        result = json.loads(str(response.text))["result"]
        print(response.text)
        return result
        

    # 导出地址对应的公钥
    def DumpPubkey(self):
        Launch = '0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c'
        payload = '{"jsonrpc":"2.0","method":"account_dumpPubkey","params":["'+Launch+'"], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)
        Pubkey = json.loads(str(response.text))["result"]
        return Pubkey

    #候选节点
    def CandidateCredit(self):

        Pubkey = self.DumpPubkey()
        payload = {"jsonrpc":"2.0","method":"account_candidateCredit","params":["0x3ebcbe7cb440dd8c52940a2963472380afbb56c5","0x111","0x110","0x30000","{\"Pubkey\":\"0x03f4e810a0741ff81765a2872675fe7bc54372f2619489d1dae269ddf19305d7aa\",\"Node\":\"39.98.39.224:44444\"}"],"id":1}
        response = requests.post(self.url,json=payload,headers=header)
        print(response.text)

    # 添加节点
    def p2p_addPeer(self):

        enode = "enode://328bcd41c37a7cb9382048f1ec6b9b546f7b261c1177dcf992859a665cc664ca@39.98.39.224:44444"
        payload = '{"jsonrpc":"2.0","method":"p2p_addPeer","params":["'+enode+'"], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(payload)
        print(response.text)
        # self.p2p_removePeer(enode)

    #移除节点
    def p2p_removePeer(self,enode):
        payload = '{"jsonrpc":"2.0","method":"p2p_removePeer","params":["'+enode+'"], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)

    # 获取所有候选节点地址和对应的信任值
    def GetCandidateAddrs(self):
        payload = '{"jsonrpc":"2.0","method":"chain_getCandidateAddrs","params":[""], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        result = json.loads(str(response.text))["result"]
        Credit = re.findall('"Credit":"(.*?)"',result)
        for money in Credit:
            count = int(money, 16) 
            print(int(count))
        print(response.text)

    # 生成其他链的地址


    def p2p_getPeers(self):
        payload = '{"jsonrpc":"2.0","method":"p2p_getPeers","params":"", "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)


    def unlock_account(self):

        Launch = '0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c'
        payload ='{"jsonrpc":"2.0","method":"account_unlockAccount","params":["'+Launch+'","123"], "id": 3}'
        # payload = '{"jsonrpc":"2.0","method":"account_openWallet","params":["123"], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)

    def get_money(self):

        Launch = '0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c'
        payload = '{"jsonrpc":"2.0","method":"chain_getBalance","params":["'+Launch+'"], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        result = json.loads(str(response.text))["result"]
        CollectionName = 'Address_Msg'
        message = {"Address":Launch,"Money":result}
        pynosql.insert(CollectionName,message)



    def get_msg(self):

        payload = '{"jsonrpc":"2.0","method":"trace_getTransaction","params":["0x816c297aefb1114f9b86168d1598dd924e83cc6dbddc48eb4c4f64fac4c6d2c7"], "id": 3}'
        response = requests.post(self.url,data=payload,headers=header)
        print(response.text)


    # http://explorer.drep.org/api/transaction?hash=0x816c297aefb1114f9b86168d1598dd924e83cc6dbddc48eb4c4f64fac4c6d2c7
    # http://explorer.drep.org/api/addrTxHistory?address=0x28f8c33d0080bde50f78bf30b84d7d1b8f676170&page=1&limit=15
url = 'http://39.98.39.224:35645'
# url = 'http://39.98.39.224:44444'
# url = 'http://127.0.0.1:35645'
run = Drep_Deal(url)

# run.CreateAccount()
# run.openWallet()
# run.Launch_Deal()
# run.gas_estimate()
# run.p2p_addPeer()
# run.CandidateCredit()
# run.getPeers()
# run.p2p_removePeer()
# run.GetCandidateAddrs()

# run.VoteCredit()
# run.Cancel_VoteCredit()
# run.getCancelCreditDetail()
# run.GetCancelCreditDetails()
# run.CandidateCredit()1
# run.GetCandidateAddrs()
# run.p2p_localNode()
# run.DumpPubkey()
# for index in range(10):
# run.VoteCredit()
# run.Cancel_VoteCredit()
# run.GetCandidateAddrs()

# run.p2p_addPeer()

# run.CandidateCredit()
# run.getBlockGasInfo()
# run.VoteCredit()
# run.Cancel_VoteCredit()
# for index in range(900):
#     run.Launch_Deal()
# run.select_nonce()
# run.unlock_account()
# run.TestCase()
# run.get_msg()
'''
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
            return result


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
    def GetTxInPool(self,hash):

        Term = {"name":"GetTxInPool"}
        method = self.get_method(Term)
        params = '["'+hash+'"]'
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
        adder = self.General_way(method,params)
        return adder

    
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
        money = hex(testcase_list['money'] * (10 ** 18))
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
    def importPrivkey(self,privkey,password):
        
        Term = {"name":"importPrivkey"}
        method = self.get_method(Term)
        params = '["'+privkey+'","'+password+'"]'
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
# url = 'http://node1.drep.org'
# url = 'http://testnet.drep.org'
CollectionName = 'method'
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
    
    # account.VoteCredit()
    BlockMgr.GetTxInPool('0x52d5bd83f3bea76fb0fcb0dfad8e4e877aba8e935be96eb18c37d8caf30e7070')
    print(int(0x52b7d2dcc80cd2e4000000))

#领取测试币验证
def test5():
    adder = account.createAccount()
    url = 'http://testnet.drep.org/api/faucet?address=' + adder
    response = requests.get(url)
    print(response.text)

    
if __name__ == "__main__":

    # test5()
    # VoteCredit_Scene()
    # CandidateCredit_Scene()
    # GetMoneyAddress()
    # chain.getBalance('')
    # BlockMgr.GetTxInPool('0xfd3505658f04e8726234c03c4c3cf4dc9a6a8855')
    # account.transfer()
    # chain.getBalance('0x095173ce86a850ff35aed6000917a141421447eb')
    # print((1997525399999999832/ (10 ** 18)))
    # BlockMgr.GetPoolTransactions('0x095173ce86a850ff35aed6000917a141421447eb')
    # account.account_unlockAccount('0xE93191CaC3C7668a8400BB12FC35c878c134EA1a','Qwer1234')
    # account.dumpPrivkey('0xE93191CaC3C7668a8400BB12FC35c878c134EA1a')
    account.createAccount()
    # account.DumpPubkey('0x92f3842c1dfcb7597a9520a4a00971059747ecb1')
    # BlockMgr.GetTxInPool('0x02a235fdeaf998437a94a8c12a4b056b5701752db812078a440f31908c41f0bbba')
    # chain.getBalance('0xbe0ec4bcc55e18cd4d23058c637308b97ee31ed7')
    # GetMoneyAddress()
    # chain.getBalance('0x8966eb1776b4C52B81B30A9Fd1335b24F187213D')
    # account.transfer()
    # account.importPrivkey('0xea92ca08b1994a93c745c7a7440682e4352f2e44cc8907642b70a2903d65d565','Qwer1234')
    # chain.getBalance('0xfd3505658f04e8726234c03c4c3cf4dc9a6a8855')
    # account.transfer()
    # account.importPrivkey('0x8e89233e4c15f08a1e1affede9de683f4b534647855e6bc49781754d368dec03','Qwer1234')
    # chain.getBalance('0x7d17376a5A611c768970f7CE99FBE309450bfF6f')
    # account.createAccount()
    # account.transfer()

    

    # account.transfer()
    
    # BlockMgr.GetTxInPool('0xe8ef84e4739a83fd22a32f06d2dd113abb2d56632d4fa29569438702ec7c03a8')
    # account.account_unlockAccount('4e0e93162e2e8296cbd377e4a687c590c221649c3ae94732cdcf7f2c80c13aec','Qwer1234')
    
    # test3()
    # test4()
    


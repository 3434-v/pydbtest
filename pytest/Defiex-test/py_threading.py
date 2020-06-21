#!/usr/bin/python3

import threading
import time,datetime
import requests
import sqlite3
import contextlib
exitFlag = 0
class SqlSave(object):
    def __init__(self):
        self.table_list = ['general','supernode','Admin_testname','url']

    def __enter__(self):
        # table_length = len(self.table_list)
        # with open('table.txt','w+') as length:
        #     old_length = length.readlines()
        # length.close()
        # with open('table.txt','w+') as length:
        #     length.write(str(table_length))

        # length.close()
        self.conn = sqlite3.connect('F:\\Defiex\\AutoTest\\run_test\\hierarchy_testcase\\test.db')
        self.curse = self.conn.cursor()
        
        return self

    def __exit__(self, exc_type, exc_val, exc_t):
        
        self.curse.close() 
        self.conn.commit()
        self.conn.close()

    # def unify(self,table):
    #     create_sql = 'create table {}(id integer primary key autoincrement,name varchar(100))'.format(table)
    #     insert_sql = 'insert into {}(name) values("{}")'.format(table,name)
    #     try:
    #         self.curse.execute(create_sql)
    #         self.curse.execute(insert_sql)
    #     except:
    #         self.curse.execute(insert_sql)
    
    #url尾椎表
    def url(self,urlname,url):
        create_sql = 'create table url(id integer primary key autoincrement,urlname text,url text)'
        insert_sql = 'insert into url(urlname,url) values("{}","{}")'.format(urlname,url)
        try:
            self.curse.execute(create_sql)
            self.curse.execute(insert_sql)
        except:
            self.curse.execute(insert_sql)

    #普通账号表
    def general(self,name,password,environment):
        create_sql = 'create table general(id integer primary key autoincrement,name text,password text,environment text)'
        insert_sql = 'insert into general(name,password,environment) values("{}","{}","{}")'.format(name,password,environment)
        try:
            self.curse.execute(create_sql)
            self.curse.execute(insert_sql)
        except:
            self.curse.execute(insert_sql)

    #超级节点账号表
    def supernode(self,name,environment):
        create_sql = 'create table supernode(id integer primary key autoincrement,name varchar(100),environment text)'
        insert_sql = 'insert into supernode(name,environment) values("{}","{}")'.format(name,environment)
        try:
            self.curse.execute(create_sql)
            self.curse.execute(insert_sql)
        except:
            self.curse.execute(insert_sql)

    #管理后台账号表
    def Admin_testname(self,name,password,code):
        create_sql = 'create table Admin_testname(id integer primary key autoincrement,name varchar(100),password varchar(100),code varchar(100))'
        insert_sql = 'insert into Admin_testname(name,password,code) values("{}","{}","{}")'.format(name,password,code)
        try:
            self.curse.execute(create_sql)
            self.curse.execute(insert_sql)
        except:
            self.curse.execute(insert_sql)

    #get内容获取
    def select(self,field,table,condition,data):
        select_sql = 'select {} from {} where {}="{}"'.format(field,table,condition,data)
        self.curse.execute(select_sql)
        msg = self.curse.fetchall()
        return msg
    
    def selects(self,tableName):
        select_sql = 'select name,password,code from {}'.format(tableName)
        self.curse.execute(select_sql)
        msg = self.curse.fetchall()
        return msg

    #操作日志表
    def handle_log(self,handle):
        time = self.get_time()
        create_sql = 'create table handle_log(id integer primary key autoincrement,time varchar(200),handle_type text)'
        insert_sql = 'insert into handle_log(time,handle_type) values("{}","{}")'.format(time,handle)
        try:
            self.curse.execute(create_sql)
            self.curse.execute(insert_sql)
        except:
            self.curse.execute(insert_sql)
    
    def get_time(self):
        otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        # print(otherStyleTime)
        return otherStyleTime

    #环境表
    def environment(self,name,url):
        create_sql = 'create table environment(id integer primary key autoincrement,name varchar(100),url varchar(100))'
        insert_sql = 'insert into environment(name,url) values("{}","{}")'.format(name,url)
        try:
            self.curse.execute(create_sql)
            self.curse.execute(insert_sql)
        except:
            self.curse.execute(insert_sql)

    #response返回信息表
    def Name_ResponseMsg(self,name,userid,token,invitecode,environment):
        times = self.get_time()
        create_sql = 'create table Name_ResponseMsg(id integer primary key autoincrement,name text not null unique,userid text,token text,invitecode text,gettime text,environment text)'
        insert_sql = 'insert into Name_ResponseMsg(name,userid,token,invitecode,gettime,environment) values("{}","{}","{}","{}","{}","{}")'.format(name,userid,token,invitecode,times,environment)
        try:
            self.curse.execute(create_sql)
            self.curse.execute(insert_sql)
        except:
            self.curse.execute(insert_sql)

    #更新token
    def update(self,table,token,name):
        times = self.get_time()
        print(times)
        update_sql = 'update {} set token="{}",gettime="{}" where name="{}"'.format(table,token,times,name)
        self.curse.execute(update_sql)

    #多表连接
    def join_table(self,environment):
        join_sql = 'select * from environment join Admin_testname on environment.id=Admin_testname.id where environment.name="{}"'.format(environment)
        self.curse.execute(join_sql)
        msg = self.curse.fetchall()
        # print(msg)
        return msg

    #超级节点流程情况数据
    def supermsg(self,explain,msg):
        create_sql = 'create table supermsg(id integer primary key autoincrement,explain text not null unique,msg text)'
        insert_sql = 'insert into supermsg(explain,msg) values("{}","{}")'.format(explain,msg)
        try:
            self.curse.execute(create_sql)
            self.curse.execute(insert_sql)
        except:
            self.curse.execute(insert_sql)

    #建仓数据
    def granary(self,name,symbol,orderid,environment,balanceold,balance,openprice,openfee,forceprice,direction):
        create_sql = 'create table granary(id integer primary key autoincrement,name text,symbol text,orderid text,environment text,balanceold text,balance text,openprice text,openfee text,forceprice text,direction text)'
        insert_sql = 'insert into granary(name,symbol,orderid,environment,balanceold,balance,openprice,openfee,forceprice,direction) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(name,symbol,orderid,environment,balanceold,balance,openprice,openfee,forceprice,direction)
        try:
            self.curse.execute(create_sql)
            self.curse.execute(insert_sql)
        except:
            self.curse.execute(insert_sql)
    #删除数据
    def delete(self,table,condition,data):
        delete_sql = 'delete from {} where {}="{}"'.format(table,condition,data)
        try:
            self.curse.execute(delete_sql)
        except:
            self.curse.execute(delete_sql)

    #多级关联专用表
    def multilevel(self,name,invitecode,shareid):
        create_sql = 'create table multilevel(id integer primary key autoincrement,name text,invitecode text,shareid text)'
        insert_sql = 'insert into multilevel(name,invitecode,shareid) values("{}","{}","{}")'.format(name,invitecode,shareid)
        try:
            self.curse.execute(create_sql)
            self.curse.execute(insert_sql)
        except:
            self.curse.execute(insert_sql)

    #测试验证数据
    def testcase(self,state,msg):
        time = self.get_time()
        create_sql = 'create table testcase(id integer primary key autoincrement,state text,msg text,time text)'
        insert_sql = 'insert into testcase(state,msg,time) values("{}","{}","{}")'.format(state,msg,time)
        try:
            self.curse.execute(create_sql)
            self.curse.execute(insert_sql)
        except:
            self.curse.execute(insert_sql)

    #建仓时测试数据输入表
    def test_msg(self,spratio_ratio,slratio_ratio,create_money,pry,formalities_ratio,direction):
        create_sql = 'create table test_msg(id integer primary key autoincrement,spratio_ratio text,slratio_ratio text,create_money text,pry text,formalities_ratio text,direction text)'
        insert_sql = 'insert into test_msg(spratio_ratio,slratio_ratio,create_money,pry,formalities_ratio,direction) values("{}","{}","{}","{}","{}","{}")'.format(spratio_ratio,slratio_ratio,create_money,pry,formalities_ratio,direction)
        try:
            self.curse.execute(create_sql)
            self.curse.execute(insert_sql)
        except:
            self.curse.execute(insert_sql)

    #现金现价建仓数据表
    def current_granary(self,name,balanceold,balance,orderid,wttime,price_money,testcase):
        create_sql = 'create table current_granary(id integer primary key autoincrement,name text,balanceold text,balance text,orderid text,wttime text,price_money text,testcase text)'
        insert_sql = 'insert into current_granary(name,balanceold,balance,orderid,wttime,price_money,testcase) values("{}","{}","{}","{}","{}","{}","{}")'.format(name,balanceold,balance,orderid,wttime,price_money,testcase)
        try:
            self.curse.execute(create_sql)
            self.curse.execute(insert_sql)
        except:
            self.curse.execute(insert_sql)

    #各种金额数据表
    def all_money(self):
        '''
        余额、赠金、冻结赠金
        '''

    #充币地址
    def TopUpSite(self,name,ETH_ERC20,BTC_OMNI,TRX_TRC20):
        create_sql = 'create table TopUpSite(id integer primary key autoincrement,name text,ETH_ERC20 text,BTC_OMNI text,TRX_TRC20 text)'
        insert_sql = 'insert into TopUpSite(name,ETH_ERC20,BTC_OMNI,TRX_TRC20) values("{}","{}","{}","{}")'.format(name,ETH_ERC20,BTC_OMNI,TRX_TRC20)
        try:
            self.curse.execute(create_sql)
            self.curse.execute(insert_sql)
        except:
            self.curse.execute(insert_sql)

    #获取提币纪录
    def Withdraw_recod(self,name,txid):
        create_sql = 'create table Withdraw_recod(id integer primary key autoincrement,name text,txid text)'
        insert_sql = 'insert into Withdraw_recod(name,txid) values("{}","{}")'.format(name,txid)
        try:
            self.curse.execute(create_sql)
            self.curse.execute(insert_sql)
        except:
            self.curse.execute(insert_sql)

# def way(func):        
#     with SqlSave() as run:
#         return run
# @way
# def exit():
#     return 'hanle_log'
    

# class Resource():
#     def __enter__(self):
#         print('===connect to resource===')
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('===close resource connection===')
        
#     def operate(self):
#         print('===in operation===')
        
# with Resource() as res:
#     res.operate()

# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         # print(threading.currentThread())
#         # print(threading.activeCount())
#         print ("开始线程：" + self.name)
#         # print_time(self.name, self.counter, 5)
#         for index in range(10):
#             Login()
#         print ("退出线程：" + self.name)

# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1

# def Login():
#     print('response.text')

# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# # 开启新线程
# start = time.time()
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# stop = time.time()
# print ("退出主线程",stop-start)








'''
#!/usr/bin/python3

import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")


#!/usr/bin/python3

import queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
'''


'''
XXXX点触发止盈/止损平仓
买涨时
止盈：XXXX=建仓价+（设置止盈百分比*建仓花费+ 资金费用+手续费费率*杠杆*建仓花费）*建仓价/ (杠杆*建仓花费) 
止损：XXXX=建仓价 -（设置止损百分比*建仓花费- 资金费用-手续费费率*杠杆*建仓花费）*建仓价/ (杠杆*建仓花费) 
买跌时
止盈：XXXX=建仓价 -（设置止盈百分比*建仓花费+ 资金费用+手续费费率*杠杆*建仓花费）*建仓价/ (杠杆*建仓花费) 
止损：XXXX=建仓价 +（设置止损百分比*建仓花费- 资金费用-手续费费率*杠杆*建仓花费）*建仓价/ (杠杆*建仓花费)  

 
预估盈利=建仓花费*设置的止盈百分比  

预估亏损=建仓花费*设置的止损百分比  

如果是设置的价格

XXXX点触发止盈/止损平仓 ，XXXX=设置的价格 

买涨时的预估盈利/亏损

盈利：(XXXX-建仓价)/建仓价*建仓花费*杠杆  - 手续费费率*杠杆*建仓花费 -  资金费用
亏损：(建仓价-XXXX)/建仓价*建仓花费*杠杆  + 手续费费率*杠杆*建仓花费 + 资金费用

买跌时的预估盈利/亏损  

盈利：(建仓价-XXXX)/建仓价*建仓花费*杠杆  - 手续费费率*杠杆*建仓花费 -  资金费用
亏损：(XXXX-建仓价)/建仓价*建仓花费*杠杆  + 手续费费率*杠杆*建仓花费 + 资金费用  
'''
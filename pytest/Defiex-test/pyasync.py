""" 多进程
import random
import time
from multiprocessing import Process
from os import getpid


def download_task(filename) -> None:
    print("启动下载进程, 编号[{}]".format(getpid()))
    print("开始下载{}...".format(filename))
    time_to_download = random.randint(5, 10)
    time.sleep(time_to_download)
    print("{}下载完成！耗费{}秒".format(filename, time_to_download))


def main() -> None:
    start = time.time()
    task1 = Process(target=download_task, args=('test1',))
    task1.start()
    task2 = Process(target=download_task, args=('test2',))
    task2.start()
    task1.join()
    task2.join()
    end = time.time()
    print("总耗时:{}".format(end - start))


if __name__ == '__main__':
    main()
"""

""" 多线程
from random import randint
from threading import Thread
from time import time, sleep


def download_task(filename: str) -> None:
   print("开始下载{}...".format(filename))
   time_to_download = randint(5, 10)
   sleep(time_to_download)
   print("{}下载完成！耗费{}秒".format(filename, time_to_download))


def main():
   start = time()
   task1 = Thread(target=download_task, args=('test1', ))
   task1.start()
   task2 = Thread(target=download_task, args=('test2', ))
   task2.start()
   task1.join()
   task2.join()
   end = time()
   print("总耗时:{}".format(end - start))


if __name__ == '__main__':
   
   main()
"""
"""
from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print("开始下载{}...".format(self._filename))
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print("{}下载完成！耗费{}秒".format(self._filename, time_to_download))


def main():
    start = time()
    task1 = DownloadTask('test1')
    task1.start()
    task2 = DownloadTask('test2')
    task2.start()
    task1.join()
    task2.join()
    end = time()
    print("总耗时:{}".format(end - start))
main()
"""


from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()
        # 计算存款后的余额
        try:
            new_balance = self._balance + money
            # 模拟受理存款业务需要0.01秒的时间
            sleep(0.01)
            # 修改账户余额
            self._balance = new_balance
        finally:
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    # 创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()

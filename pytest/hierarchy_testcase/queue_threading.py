#! /usr/bin/env python3

import time
import threading
import queue

# 一个线程，间隔一定的时间，把一个递增的数字写入队列
# 生产者
class Producer(threading.Thread):

  def __init__(self, work_queue):
    super().__init__() # 必须调用
    self.work_queue = work_queue
    
  def run(self):
    num = 1
    while True:
      self.work_queue.put(num)
      num = num+1
      time.sleep(1) # 暂停1秒

# 一个线程，从队列取出数字，并显示到终端
class Printer(threading.Thread):

  def __init__(self, work_queue):
    super().__init__() # 必须调用
    self.work_queue = work_queue

  def run(self):
    while True:
      num = self.work_queue.get() # 当队列为空时，会阻塞，直到有数据
      print(num)

def main():
  work_queue = queue.Queue()

  producer = Producer(work_queue)
  producer.daemon = True # 当主线程退出时子线程也退出
  producer.start()

  printer = Printer(work_queue)
  printer.daemon = True # 当主线程退出时子线程也退出
  printer.start()

  work_queue.join() # 主线程会停在这里，直到所有数字被get()，并且task_done()，因为没有调用task_done()，所在这里会一直阻塞，直到用户按^C

if __name__ == '__main__':
  
  main()


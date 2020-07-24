from concurrent.futures import ThreadPoolExecutor
import time


def spider(page):
    time.sleep(page)
    print("time:{}".format(page))
    return page


with ThreadPoolExecutor(max_workers=5) as thrd:
    task1 = thrd.submit(spider, 1)
    task2 = thrd.submit(spider, 2)
    task3 = thrd.submit(spider, 3)

    print("task1:{}".format(task1.done()))
    print("task2:{}".format(task2.done()))
    print("task3:{}".format(task3.done()))

    time.sleep(2)
    print("task1:{}".format(task1.done()))
    print("task2:{}".format(task2.done()))
    print("task3:{}".format(task3.done()))
    print(task1.result())

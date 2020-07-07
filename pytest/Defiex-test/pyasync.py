import asyncio
import threading
import time


async def do_some_work(x):
    print("waiting" + str(x))
    await asyncio.sleep(x)
    print('Done')

# 验证是否为协程函数
# print(asyncio.iscoroutinefunction(do_some_work))

# print(asyncio.iscoroutine(do_some_work(3)))


# loop.run_until_complete(do_some_work(3))


# 回调函数
def done_callback(futu):
    print('Done')

# futu = asyncio.ensure_future(do_some_work(3))
# futu.add_done_callback(done_callback)
# loop.run_until_complete(futu)


# 实例化
loop = asyncio.get_event_loop()
# loop.run_until_complete(
#     asyncio.gather(
#         do_some_work(1),
#         do_some_work(3)
#     )
# )


class MyThread(threading.Thread):
    def __init__(self, threadid):
        threading.Thread.__init__(self)
        self.threadid = threadid

    def run(self):
        print("ID:{}".format(self.threadid))
        loop.run_until_complete(
            asyncio.gather(
                do_some_work(1),
                do_some_work(3)
            )
        )


thread1 = MyThread(1)
thread2 = MyThread(2)
thread1.start()
thread2.start()

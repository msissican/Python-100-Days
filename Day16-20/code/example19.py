"""
扩展性系统性能
- 垂直扩展 - 增加单节点处理能力
- 水平扩展 - 将单节点变成多节点（读写分离/分布式集群）
并发编程 - 加速程序执行 / 改善用户体验
耗时间的任务都尽可能独立的执行，不要阻塞代码的其他部分

- 多线程
1. 创建Thread对象指定target和args属性并通过start方法启动线程
2. 继承Thread类并重写run方法来定义线程执行的任务
3. 创建线程池对象ThreadPoolExecutor并通过submit来提交要执行的任务
第3种方式可以通过Future对象的result方法在将来获得线程的执行结果
也可以通过done方法判定线程是否执行结束

- 多进程

- 异步I/O
"""
import glob
import os
import time

from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from PIL import Image


class ThumbnailThread(Thread):
    # 继承自 Thread 对象
    def __init__(self, infile):
        self.infile = infile
        super().__init__()

    def run(self):
        # 重写 run 方法

        file, ext = os.path.splitext(self.infile) # 分离文件名和扩展名
        filename = file[file.rfind('/') + 1:] # 获取文件名, 找最后一位的'/' + 1
        for size in (32, 64, 128):
            # 生成三种尺寸的缩略图
            outfile = f'thumbnails/{filename}_{size}_{size}.png' # 生成文件名
            image = Image.open(self.infile) # 打开文件, 使用 PIL Image 库打开
            image.thumbnail((size, size)) # image 方法的缩放
            image.save(outfile, format='PNG') # 保存缩略图


# 可以在 Thread 中, target 参数指定要执行的函数
def gen_thumbnail(infile):
    file, ext = os.path.splitext(infile)
    filename = file[file.rfind('/') + 1:]
    for size in (32, 64, 128):
        outfile = f'thumbnails/{filename}_{size}_{size}.png'
        image = Image.open(infile)
        image.thumbnail((size, size))
        image.save(outfile, format='PNG')


def main1():
    start = time.time() # 记录线程开始的时间
    threads = [] # 线程队列

    for infile in glob.glob('images/*'): #  遍历 images 目录下的所有文件

        # 还可以这样写, 定义一个 run 方法, 传入 Thread 对象
        # t = Thread(target=gen_thumbnail, args=(infile, ))
        t = ThumbnailThread(infile) # 创建线程

        t.start() # 启动线程, 线程启动后会回调执行 run 方法
        threads.append(t) # 将线程添加到线程队列

    for t in threads:
        t.join() # 等待每个线程的 t 完成执行

    end = time.time()
    print(f'耗时: {end - start}秒')


def main2():
    pool = ThreadPoolExecutor(max_workers=30) # 创建线程池, 传入最大线程数
    futures = [] # 线程队列
    start = time.time()

    for infile in glob.glob('images/*'): # 遍历 images 目录下的所有文件

        # submit方法是非阻塞式的方法
        """ 阻塞式方法会暂停程序的执行,直到方法完成执行
            非阻塞式方法不会暂停程序的执行,即使方法还没有完成执行"""
        # 即便工作线程数已经用完，submit方法也会接受提交的任务 
        future = pool.submit(gen_thumbnail, infile)
        # 提交一个任务到线程池 pool, 执行 gen_thumbnail, 参数是 infile, 返回一个 Future 对象 future, 表示线程的执行结果
        futures.append(future) # 将 future 添加到线程队列

    for future in futures:
        # result方法是一个阻塞式的方法 如果线程还没有结束
        # 暂时取不到线程的执行结果 代码就会在此处阻塞
        future.result() # 等待所有线程执行完成

    end = time.time()
    print(f'耗时: {end - start}秒')

    # shutdown也是非阻塞式的方法,
    # 但是如果已经提交的任务还没有执行完, 线程池是不会停止工作的
    # shutdown之后再提交任务就不会执行而且会产生异常
    pool.shutdown()


class ThreadPoolManager():
    def __init__(self, max_workers):
        self.pool = ThreadPoolExecutor(max_workers=max_workers)
        self.futures = []

    def task(self, *args, **kwargs):
        pass

    def submit_task(self, task, *args):
        future = self.pool.submit(task, *args)
        self.futures.append(future)

    def wait_tasks(self):
        for future in self.futures:
            future.result()

    def shutdown(self):
        self.pool.shutdown()

class ThumbnailThreadPool(ThreadPoolManager):
    def __init__(self, max_workers):
        super().__init__(max_workers)

    def task(self, infile):
        file, ext = os.path.splitext(infile)
        filename = file[file.rfind('/') + 1:]
        for size in (32, 64, 128):
            outfile = f'thumbnails/{filename}_{size}_{size}.png'
            image = Image.open(infile)
            image.thumbnail((size, size))
            image.save(outfile, format='PNG')


def main3():
    pool = ThumbnailThreadPool(max_workers=30)
    start = time.time()

    for infile in glob.glob('images/*'):
        pool.submit_task(pool.task, infile)

    pool.wait_tasks()
    pool.shutdown()

    end = time.time()
    print(f'耗时: {end - start}秒')


if __name__ == '__main__':
    main2()








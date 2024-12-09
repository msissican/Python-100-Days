"""
协程（coroutine）- 可以在需要时进行切换的相互协作的子程序
"""
import asyncio

from example15 import is_prime


def num_generator(m, n):
    """指定范围的数字生成器"""
    # yield from 等价于 for i in range(m, n + 1): yield i
    yield from range(m, n + 1)


async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        if is_prime(i):
            print('Prime =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return tuple(squares)


def main():
    """主函数"""
    # 获取当前事件循环, 负责管理协程, 调度和执行异步任务
    loop = asyncio.get_event_loop()
    # 创建两个协程, 分别进行素数过滤和平方映射, 创建future对象, 运行两个异步函数, 返回 future 对象
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    # 为future对象添加回调函数, 当 future 对象完成时, 调用回调函数, 打印结果
    future.add_done_callback(lambda x: print(x.result()))
    # 使用事件循环, 运行 future 对象
    # run_until_complete 方法会一直阻塞, 直到 future 对象完成
    loop.run_until_complete(future)
    # 关闭事件循环
    loop.close()


if __name__ == '__main__':
    main()

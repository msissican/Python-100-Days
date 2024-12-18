"""
aiohttp - 异步HTTP网络访问
异步I/O（异步编程）- 只使用一个线程（单线程）来处理用户请求

用户请求一旦被接纳，剩下的都是I/O操作，通过多路I/O复用也可以达到并发的效果
这种做法与多线程相比可以让CPU利用率更高，因为没有线程切换的开销

Redis/Node.js - 单线程 + 异步I/O
Celery - 将要执行的耗时间的任务异步化处理
异步I/O事件循环 - uvloop
"""
"""
`async` 用于定义异步函数，而 `await` 用于等待异步操作完成。
*   `async` 和 `await` 只能在异步函数中使用。
*   `async` 函数必须包含至少一个 `await` 表达式。
*   `await` 表达式必须在异步函数中使用。
*   `async` 和 `await` 可以与其他关键字和语法结构一起使用，例如 `try`-`except`、`for` 循环等。
"""
# TODO 慢慢理解 asyncio, async, await

import asyncio
import re

import aiohttp


async def fetch(session, url):
    # async with 用于管理异步资源, 如异步连接,异步上下文,异步文件
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def main():
    pattern = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    async with aiohttp.ClientSession() as session:
        for url in urls:
            html = await fetch(session, url)
            print(pattern.search(html).group('title'))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()

import requests
import asyncio
import time
import aiohttp


async def get_page(download_url):
    print('正在下载', download_url)
    # requests.get是基于同步、必须使用基于异步的网络请求模块进行指定url的请求发送
    # response = requests.get(url=url)
    # aiohttp:基于异步网络请求的模块
    async with aiohttp.ClientSession() as session:
        async with await session.get(download_url) as response:
            # text()返回字符串形式的响应数据
            # read()返回的二进制形式的响应数据
            # json()返回的就是json对象
            # 注意：获取响应数据操作之前一定要使用await进行手动挂起
            page_text = await response.text()
    print('下载完毕', page_text)


# 注意：运行前先打开Flask服务
if __name__ == '__main__':
    start = time.time()
    urls = [
        'http://127.0.0.1:5000/aaa',
        'http://127.0.0.1:5000/bbb',
        'http://127.0.0.1:5000/ccc'
    ]
    tasks = []
    for url in urls:
        c = get_page(url)
        task = asyncio.ensure_future(c)
        tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print('总耗时: ', end - start)

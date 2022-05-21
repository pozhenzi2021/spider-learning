import asyncio
import time


async def request(download_url):
    print('正在下载', download_url)
    # 在异步协程中如果出现了同步模块相关的代码，那么无法实现异步，因此不能使用time.sleep()
    # time.sleep(2)
    # 挡在asyncio中遇到阻塞操作必须进行手动挂起，比如下面的await是必须的
    await asyncio.sleep(2)
    print('下载完毕', download_url)


if __name__ == '__main__':
    start = time.time()
    urls = [
        'www.baidu.com',
        'www.sogou.com',
        'www.douban.com'
    ]
    tasks = []
    for url in urls:
        c = request(url)
        task = asyncio.ensure_future(c)
        tasks.append(task)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start)

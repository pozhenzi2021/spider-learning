import asyncio


async def request(url):
    print('正在请求的url是', url)
    print('请求成功', url)
    return url


def callback_func(task):
    # 要求任务对象有返回值，即request()函数返回url
    print(task.result())


def demo1():
    # async修饰的函数，调用之后返回的一个协程对象
    c = request("www.baidu.com")
    # 创建一个时间循环对象
    loop = asyncio.get_event_loop()
    # 将协程对象注册到loop中，然后启动loop
    loop.run_until_complete(c)


def demo2():
    # async修饰的函数，调用之后返回的一个协程对象
    c = request("www.baidu.com")
    # 创建一个时间循环对象
    loop = asyncio.get_event_loop()
    # 基于loop创建一个task对象
    task = loop.create_task(c)
    print(task)
    loop.run_until_complete(task)
    print(task)


def demo3():
    # async修饰的函数，调用之后返回的一个协程对象
    c = request("www.baidu.com")
    # 创建一个时间循环对象
    loop = asyncio.get_event_loop()
    # future的使用
    task = asyncio.ensure_future(c)
    print(task)
    loop.run_until_complete(task)
    print(task)


def demo4():
    # async修饰的函数，调用之后返回的一个协程对象
    c = request("www.baidu.com")
    # 创建一个时间循环对象
    loop = asyncio.get_event_loop()
    # future的使用
    task = asyncio.ensure_future(c)
    # 将回调函数绑定到任务对象中
    task.add_done_callback(callback_func)
    loop.run_until_complete(task)


if __name__ == '__main__':
    demo4()

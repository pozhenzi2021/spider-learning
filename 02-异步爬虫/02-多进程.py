import time
from multiprocessing.dummy import Pool


def get_page(url):
    print("正在下载 : " + url)
    time.sleep(2)
    print("下载成功 : " + url)


if __name__ == '__main__':
    start_time = time.time()
    name_list = ['aaa', 'bbb', 'ccc']

    # 实例化一个线程池对象
    pool = Pool(4)
    # 将列表中每一个列表元素传递给get_page进行处理
    pool.map(get_page, name_list)
    end_time = time.time()
    print(end_time - start_time)

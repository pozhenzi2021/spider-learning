import requests
from bs4 import BeautifulSoup

# bs4进行数据解析
# 1. 实例化一个BeautifulSoup对象，并且将源码数据加载到该对象中
# 2. 调用BeautifulSoup对象中的属性或方法进行标签定位和数据提取
#    soup.tagName 返回的是文档中第一次出现的tagName对应的标签
#    soup.find()
#        find('tagName'): find('div')等同于soup.div
#        属性定位: soup.find('div', class_/id/attr='song')
#    soup.find_all('tagName') 返回符合要求的所有标签（列表）
#    soup.select()
#        select('某种选择器(id, class, 标签...选择器)')   返回的是一个列表
#        层级选择器:
#            soup.select('.tang > ul > li > a') 表示的是一个层级
#            soup.select('.tang > ul a')  空格表示多个层级
#    获取标签之间的文本数据
#        soup.a.text/string/get_text()
#        text/get_text() 获取某一个标签中所有的文本内容(即不一定属于该标签直系内容)
#    获取标签中属性值
#        soup.a['href']
# 爬取三国演义小说内容
if __name__ == '__main__':
    # 1. url
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    # 2. UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39 '
    }
    # 3. 发送请求（获取章节名称）
    page_text = requests.get(url=url, headers=headers).text.encode('iso-8859-1')
    # 4. 实例化BeautifulSoup对象
    soup = BeautifulSoup(page_text, 'lxml')
    # 5. 解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li')
    # 6. 持久化路径
    fp = open('../fileLibs/sanguo.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'http://www.shicimingju.com' + li.a['href']
        # 对详情页发起请求，解析出章节内容(后面跟encode解决乱码问题)
        detail_page_text = requests.get(url=detail_url, headers=headers).text.encode('iso-8859-1')
        # 解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        # 解析到了章节的内容
        content = div_tag.text
        fp.write(title + ':' + content + '\n')
        print(title, '爬取成功!!!')

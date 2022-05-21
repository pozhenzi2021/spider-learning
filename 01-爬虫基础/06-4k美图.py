import requests
from lxml import etree
import os

# xpath解析原理
#     1. 实例化一个etree对象，且需要将被解析的页面源码数据加载到该对象中
#         etree.parse(filePath) 将本地的html文档中的源码数据加载到etree对象中
#         etree.HTML('page_text') 将互联网上获取的源码数据加载到该对象中
#     2. 调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的提取
#         /: 表示从根节点开始定位，表示的一个层级
#         //: 表示的是多个层级，可以表示从任意位置开始定位
#         属性定位: //div[@class='song] tag[@attrName="attrValue"]
#         索引定位: //div[@class="song"]/p[3]  索引是从1开始的
#         取文本
#             /text() 获取的是标签中直系的文本内容
#             //text() 标签中非直系的文本内容 （所有的文本内容）
#         取属性
#             /@attrName ==> img/@src
if __name__ == '__main__':
    # 1. url
    url = 'https://pic.netbian.com/4kmeinv/'
    # 2. UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39 '
    }
    # 3. 发送请求并设置设置响应编码
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    page_text = response.text
    # 4. 构造etree对象
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="main"]/div[3]/ul/li')
    # 5. 持久化数据
    if not os.path.exists('../picLibs'):
        os.mkdir('../picLibs')
    for li in li_list:
        img_src = 'https://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
        img_data = requests.get(url=img_src, headers=headers).content
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        img_path = '../picLibs/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name + '保存成功！')

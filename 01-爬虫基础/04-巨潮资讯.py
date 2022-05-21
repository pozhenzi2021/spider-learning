import requests
import os

# 从巨潮资讯网爬取数据
if __name__ == '__main__':
    if not os.path.exists('../fileLibs'):
        os.mkdir('../fileLibs')
    # 1. url
    post_url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
    # 2. UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39 '
    }
    # 3. 构造请求参数
    post_params = {
        "pageNum": 1,
        "pageSize": 30,
        "column": "szse",
        "tabName": "fulltext",
        "isHLtitle": "true"
    }
    # 4. 发起请求
    json_data = requests.post(url=post_url, params=post_params, headers=headers).json()
    # 5. 处理响应数据（持久化存储）
    dicts = []
    for dic in json_data['announcements']:
        pdf_url = 'http://static.cninfo.com.cn/' + dic['adjunctUrl']
        pdf_content = requests.get(url=pdf_url, headers=headers).content
        local_url = '../fileLibs/' + pdf_url.split('/')[-1]
        with open(local_url, 'wb') as fp:
            fp.write(pdf_content)
            print('write pdf success')

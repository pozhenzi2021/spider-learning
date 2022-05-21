import requests

# 保存搜狗搜索出来的结果
if __name__ == "__main__":
    # 1. url
    url = "https://www.sogou.com/web"
    # 2. UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39 '
    }
    # 3. 构造请求参数
    kw = input('enter a key word:')
    param = {
        'query': kw
    }
    # 4. 发起请求
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    # 5. 持久化存储
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName, '保存成功！！')

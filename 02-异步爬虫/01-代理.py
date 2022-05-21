import requests

# 代理：突破封IP这种反爬机制
# 代理的作用：
#     - 突破自身IP访问的闲置
#     - 隐藏自身的IP
# 代理获取：本地部署代理池docker
# 注意：当前urllib3=1.26.9 报错ProxyError，需要降级到urllib3=1.25.11 (pipenv install urllib3==1.25.11)
if __name__ == '__main__':
    url = 'https://ip.293.net/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39 '
    }
    proxies = {
        "https": "https://120.42.46.226:6666"
    }
    page = requests.get(url=url, headers=headers, proxies=proxies)
    # 解决乱码问题
    page.encoding = page.apparent_encoding
    page_text = page.text
    with open("./page.html", 'w', encoding='utf-8') as fp:
        fp.write(page_text)

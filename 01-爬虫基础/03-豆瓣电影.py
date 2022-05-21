import requests

if __name__ == '__main__':
    # 1. 指定url
    get_url = 'https://movie.douban.com/j/new_search_subjects'
    # 2. 构造请求参数
    params = {
        'sort': 'U',  # 分类方式:U近期热门、T标记最多...
        'range': '0,10',
        'tags': '电影',  # 形式:电影、电视剧、综艺...
        'start': '20',
        'genres': '喜剧'  # 类型:喜剧、动作、爱情...
    }
    # 2. 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39 '
    }
    # 3. 发送http请求
    jsonData = requests.get(url=get_url, headers=headers, params=params).json()
    # 4. 处理响应消息
    print(jsonData)

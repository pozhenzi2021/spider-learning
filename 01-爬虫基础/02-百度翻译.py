import requests
import json
if __name__ == '__main__':
    # 1. 指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # 2. 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39 '
    }
    # 3. post请求参数处理
    word = input('enter a word: ')
    data = {
        'kw': word
    }
    # 4. 发送请求
    response = requests.post(url=post_url, data=data, headers=headers)
    # 5. 获取响应数据:json()方法返回的是obj，只有返回application/json的响应才可应用json()获取
    dic_obj = response.json()

    # 持久化存储
    fileName = word + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=fp, ensure_ascii=False)

    print('over!!')

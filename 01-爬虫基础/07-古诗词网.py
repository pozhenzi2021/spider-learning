# import ddddocr
import requests
from lxml import etree
import ddddocr

if __name__ == '__main__':
    # 1. url
    login_url = 'https://so.gushiwen.cn/user/login.aspx'
    # 2. UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39 '
    }
    # 3. 发送请求(所有请求都要使用session方式登录才行）
    session = requests.session()
    login_text = session.get(url=login_url, headers=headers).text
    # 4. 下载验证码图片
    tree = etree.HTML(login_text)
    img_code_src = 'https://so.gushiwen.cn' + tree.xpath('//*[@id="imgCode"]/@src')[0]
    with open('../picLibs/imgCode.jpg', 'wb') as fp:
        # 验证码获取也需要使用session，否则会登录不成功，不知为什么
        img_data = session.get(url=img_code_src, headers=headers).content
        fp.write(img_data)
    # 5. 使用ddddocr识别验证码
    ocr = ddddocr.DdddOcr()
    with open('../picLibs/imgCode.jpg', 'rb') as f:
        img_bytes = f.read()
    img_code = ocr.classification(img_bytes)
    # 6. 登录古诗词网(https://so.gushiwen.cn)
    email = input('please input your email: ')
    password = input('please input your password: ')
    data = {
        "email": email,
        "pwd": password,
        "code": img_code,
        "denglu": "登录"
    }

    login_response = session.post(url=login_url, data=data, headers=headers)
    print('login result: ', login_response.status_code)
    # 7. 使用登录后获取到的cookie查看内容
    collect_url = 'https://so.gushiwen.cn/user/collect.aspx'
    collect_text = session.get(url=collect_url, headers=headers).text
    with open('collect.html', 'w', encoding='utf-8') as fp:
        fp.write(collect_text)

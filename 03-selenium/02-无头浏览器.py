from selenium import webdriver
from time import sleep


# 要求selenium版本在4.0.0以上，否则webdriver没有EdgeOptions()选项
def get_driver():
    # 构造请求头参数
    options = webdriver.EdgeOptions()
    options.add_argument('DNT=1')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    # 让selenium规避被检测到的风险(可能有七八种被检测到的手段，此处只是规避其中一种而已)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 实例化一个浏览器对象
    driver = webdriver.Edge(options=options)
    return driver


if __name__ == '__main__':
    bro = get_driver()
    bro.get('https://www.baidu.com')
    print(bro.page_source)
    sleep(2)
    bro.quit()

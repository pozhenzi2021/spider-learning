from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# 要求selenium版本在4.0.0以上，否则webdriver不支持EdgeOptions()选项
def get_driver():
    # 构造请求头参数
    options = webdriver.EdgeOptions()
    options.add_argument('DNT=1')
    # 实例化一个浏览器对象
    driver = webdriver.Edge(options=options)
    return driver


if __name__ == '__main__':
    bro = get_driver()
    bro.get("https://www.taobao.com/")
    # 标签定位(找到输入框)
    search_input = bro.find_element(By.ID, 'q')
    # 标签交互
    search_input.send_keys('IPhone')
    # 执行一组js程序(实现滚轮向下滚动一屏的效果)
    bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(2)
    # 点击搜索按钮
    btn = bro.find_element(By.CSS_SELECTOR, '.btn-search')
    btn.click()
    sleep(5)
    bro.quit()
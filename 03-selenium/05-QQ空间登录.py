from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
    # 构造请求头参数
    options = webdriver.EdgeOptions()
    options.add_argument('DNT=1')
    # 实例化一个浏览器对象
    driver = webdriver.Edge(options=options)
    return driver


if __name__ == '__main__':
    bro = get_driver()
    bro.get('https://qzone.qq.com/')
    # 切换到登录框所在iframe
    bro.switch_to.frame('login_frame')
    # 找到"账号密码登录"所在位置
    switcher = bro.find_element(By.ID, 'switcher_plogin')
    switcher.click()
    # 找到账号/密码输入框
    input_username = bro.find_element(By.XPATH, '//*[@id="u"]')
    input_password = bro.find_element(By.XPATH, '//*[@id="p"]')
    # 标签交互(输入用户名/密码)
    input_username.send_keys('username')
    sleep(1)
    input_password.send_keys('password')
    sleep(1)
    # 提交用户名/密码
    button = bro.find_element(By.XPATH, '//*[@id="login_button"]')
    button.click()
    # 退出浏览器
    sleep(3)
    bro.quit()


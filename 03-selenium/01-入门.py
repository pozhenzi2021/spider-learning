from selenium import webdriver
from selenium.webdriver.common.by import By


import time

# 1. pip install selenium安装selenium
# 2.1 https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/下载edge浏览器，解压出msedgedriver.exe放到PATH下
#     (根据需要，可能需要重命名为MicrosoftWebDriver.exe)
# 2.2 http://chromedriver.storage.googleapis.com/index.html下载谷歌浏览器驱动
# 3. 重启pycharm使生效
# 4. 编写基于浏览器自动化的操作代码
#    - 发起请求: get(url)
#    - 标签定位：find系列的方法
#    - 标签交互: send_keys('xxx')
#    - 执行js程序: execute_script('jsCode')
#    - 前进、后退: back(), forward()
#    - 关闭浏览器: quit()
# 5. selenium处理ifram
#    - 如果定位的标签存在于iframe标签之中，必须使用switch_to.frame(id)
#    - 动作链(拖动): from selenium.webdriver import ActionChains
#       - 实例化一个动作链对象: action = ActionChains(bro)
#       - click_and_hold(div)  长按且点击操作
#       - move_by_offset(x,y)
#       - perform()让动作链立即执行
#       - action.release()释放动作链对象
if __name__ == '__main__':
    driver = webdriver.Edge()
    driver.get('https://bing.com')
    element = driver.find_element(By.ID, 'sb_form_q')
    element.send_keys('WebDriver')
    element.submit()
    time.sleep(5)
    driver.quit()

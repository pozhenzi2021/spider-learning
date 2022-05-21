from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# 要求selenium版本在4.0.0以上，否则webdriver没有EdgeOptions()选项
def get_driver():
    # 构造请求头参数
    options = webdriver.EdgeOptions()
    options.add_argument('DNT=1')
    # 实例化一个浏览器对象
    driver = webdriver.Edge(options=options)
    return driver


if __name__ == '__main__':
    bro = get_driver()
    bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    # 如果定位的标签存在于iframe标签之中则必须通过如下操作进行标签定位: 切换浏览器标签定位的作用域
    bro.switch_to.frame('iframeResult')
    div = bro.find_element(By.ID, 'draggable')

    # 动作链
    action = ActionChains(bro)
    # 点击长按指定的标签
    action.click_and_hold(div)
    for i in range(5):
        # perform()立即执行动作链操作
        action.move_by_offset(17, 0).perform()
        sleep(0.5)
    action.release()
    bro.quit()

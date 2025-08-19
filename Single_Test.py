import time
import json
import random
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from Config import *
from ZM_IP import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def get_driver(config):  # 添加config参数
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 使用Service对象来指定ChromeDriver的路径
    service = Service(executable_path=ChromeDriverManager().install())
    # 使用Service对象创建WebDriver实例
    driver = webdriver.Chrome(service=service, options=options)
    # 防止自动化检测
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                           {'source': 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined})'})
    return driver

def vaification():
    # 可能会出现也可能不出现的验证，利用try-except不影响其他代码运行
    # 情况一
    try:
        # 点击智能验证
        driver.find_element(By.XPATH, '//*[@id="SM_BTN_1"]/div[1]/div[4]').click()
        time.sleep(3)
        # 获取滑块位置
        sour = driver.find_element(By.CSS_SELECTOR, '#nc_1_n1z')
        # 获取滑条
        ele = driver.find_element(By.CSS_SELECTOR, '#nc_1__scale_text > span')
        # 拖动滑块滑条末尾
        ActionChains(driver).drag_and_drop_by_offset(sour, ele.size['width'], -sour.size['height']).perform()
        # 点击确定，再次点击提交
        driver.find_element(By.XPATH, '//*[@id="alert_box"]/div[2]/div[2]/button').click()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, '//*[@id="ctlNext"]').click()
    except:
        print('本次无滑块验证')

    # 情况二
    try:
        # 先点击确定，再点击智能验证
        driver.find_element(By.XPATH, '//*[@id="alert_box"]/div[2]/div[2]/button').click()
        driver.find_element(By.XPATH, '//*[@id="SM_BTN_1"]/div[1]/div[4]').click()
    except:
        print('本次是滑块验证')


if __name__ == '__main__':
    # 1.问卷星url,只能是vm,不能是vj
    url = '你的网址信息'
    # 2.连接Cofig.py
    config = Config.Config()
    # 3.获取dirver
    driver = get_driver(config)
    # 4.打开网页
    driver.get(url)

    # 尝试关闭可能覆盖在“开始作答”按钮上的元素
    try:
        # 等待“开始作答”按钮可见
        start_button = driver.find_element(By.CLASS_NAME, "slideChunkWord")
        if start_button.is_displayed():
            start_button.click()
    except NoSuchElementException:
        print("未找到‘开始作答’按钮")

    # 提取所有题目,elements.type = <list>
    elements = driver.find_elements(By.XPATH, '//*[@id="divContent"]//div[@class="field ui-field-contain"]')

    # 答案汇总字典
    choices = {}
    # 遍历每个题目并选择答案
    for question in config.questions:
        id = question['id']
        # 获取选项列表
        lis = elements[id - 1].find_elements(By.CSS_SELECTOR, f'#div{id} > div.ui-controlgroup > div:nth-child(n+1)')
        # 生成答案
        if question['type'] == 'Simple':
            answers = select_Simple(question, choices)
            driver.find_element(By.XPATH, f'//*[@id="div{id}"]/div[2]/div[{answers[0]}]').click()

        elif question['type'] == 'Multiple':
            answers = select_Multiple(question, choices)
            for i in answers:
                driver.find_element(By.XPATH, f'//*[@id="div{id}"]/div[2]/div[{i}]').click()

        elif question['type'] == 'Sort':
            answer = select_Sort(config.questions[3], choices)
            answers = answer[:]
            for i in range(len(answer)):
                now_value = answer[0]
                driver.find_element(By.XPATH, f'//*[@id="div{id}"]/ul/li[{now_value}]/div[{1}]').click()
                answer.pop(0)
                for k in range(len(answer)):
                    if answer[k] < now_value:
                        answer[k] += 1
                time.sleep(0.5)

        elif question['type'] == 'Scale':
            answers = select_Scale(question, choices)
            driver.find_element(By.XPATH, f'//*[@id="div{id}"]/div[2]/div/ul/li[{answers[0]}]/a').click()

        elif question['type'] == 'Gap':
            answers = input_Gap(question, choices)
           # driver.find_element(By.XPATH, '//*[@id="q6"]').send_keys(answers[0])
            # 检查answers是否为列表并且不为空
            if isinstance(answers, list) and answers:
                # 取列表中的第一个答案
                answer = answers[0]

                # 定位填空题元素
                try:
                    input_element = driver.find_element(By.XPATH, '//*[@id="q31"]')
                    # 检查元素是否可交互
                    if input_element.is_displayed() and input_element.is_enabled():
                        # 输入答案
                        input_element.send_keys(answer)
                    else:
                        print("填空题元素不可交互或不可见")
                except NoSuchElementException:
                    print("未找到填空题元素")
            else:
                print("Gap题没有有效答案")


        # 填充列表
        choices[f'{id}'] = answers
        print(f"For question {id}, the selected answer is: {answers}")
    print('Question selection presentation：', choices)

    # 点击提交
    driver.find_element(By.XPATH, '//*[@id="ctlNext"]').click()

    # 智能验证模块
    vaification()


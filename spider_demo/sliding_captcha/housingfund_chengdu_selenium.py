# https://www.cdzfgjj.gov.cn:9802/cdnt/login.jsp#per
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

options = webdriver.ChromeOptions()

options.add_argument('--window-position=0,0')  # chrome 启动初始位置

options.add_argument('--window-size=1080,800')  # chrome 启动初始大小

options.add_argument('--no-sandbox')

options.add_argument('--headless')

options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.cdzfgjj.gov.cn:9802/cdnt/login.jsp#per')

action = ActionChains(driver)

dragger = driver.find_element_by_class_name('ui-draggable')

action.click_and_hold(dragger).perform()

action.reset_actions()

for index in range(20):
    action.move_by_offset(random.choice((3, 9, 15, 34, 43)), random.choice((0.3, 0.4, 0.5))).perform()  # 移动一个位移

    action.reset_actions()

    time.sleep(random.choice((0.3, 0.4, 0.5)))  # 等待停顿时间

action.release().perform()

action.reset_actions()

driver.find_element_by_xpath('//select[@id="aType"]/option[@value=4]').click()

driver.find_element_by_id('j_username').send_keys('513821198802199010')

driver.find_element_by_id('j_password').send_keys('88051111')

driver.find_element_by_id('btn-login').click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'u-name'))
)

print(driver.page_source)

cookies = {i['name']: i['value'] for i in driver.get_cookies()}

driver.close()
driver.quit()
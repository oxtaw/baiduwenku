from selenium import webdriver
from  selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random,time,re

url='https://wenku.baidu.com/view/dfacebff910ef12d2af9e735'

def over_judge(driver):     #获得展开文档进度
    try:
        #ele=driver.find_element_by_class_name('pagerwg-schedule')
        time.sleep(random.uniform(0,0.5))
        ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "pagerwg-schedule")))
        return ele.text
    except Exception as e:
        print('Exception:{}'.format(e))
        print('进度未获得。。。')
        return False


def get_page(url):      #将文档打开并且全部展开
    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(10)
    driver.get(url)
    time.sleep(1)
    driver.maximize_window()
    try:        #点击继续阅读
        action = ActionChains(driver)
        ele=driver.find_element_by_class_name('foldpagewg-text')
        action.move_to_element(ele).send_keys(Keys.ARROW_DOWN,Keys.ARROW_DOWN).perform()
        time.sleep(1.5)
        driver.find_element_by_class_name('foldpagewg-text').click()
        print('进度：',over_judge(driver))
    except Exception as e:
        print('展开出错')
        print('Exception:{}'.format(e))

    while over_judge(driver):       #进度返回时，加载更多
        try:
            #ele=driver.find_element_by_class_name('pagerwg-button')
            ele=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "pagerwg-button")))
            action = ActionChains(driver)
            action.move_to_element(ele).send_keys(Keys.ARROW_DOWN, Keys.ARROW_DOWN).perform()
            time.sleep(random.uniform(1,1.5))
            driver.find_element_by_class_name('pagerwg-button').click()
            #time.sleep(random.uniform(1, 1.5))
            print('进度：',over_judge(driver))
        except Exception as e:
            print('Exception:{}'.format(e))
            print('进度：',over_judge(driver),'repeat')
    return driver

def total_paper(url):       #对已经打开的整个文档页进行分析
    driver=get_page(url)
    all_paper=driver.find_elements_by_class_name('content singlePage wk-container')
    for i in all_paper:
        print(i.find_element_by_class_name('pic'))


if __name__=='__main__':
    driver=get_page(url)


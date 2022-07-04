# 该包是用来获取cookie的
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
import json
PLATFORM = {"tengxunweishi":'https://media.weishi.qq.com/'}
KEY = {"tengxunweishi":'进入官网'}
def login(platform):
    s = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    # 记得写完整的url 包括http和https
    driver.get(PLATFORM.get(platform))
    html = driver.page_source
    while(True):
        print("a")
        html = driver.page_source
        if(KEY[platform] not in html):
            break
        sleep(1)
    print("b")
    with open(platform+'_cookies.txt','w') as f:
        # 将cookies保存为json格式
        f.write(json.dumps(driver.get_cookies()))
    return driver

def check_state(platform):
    s = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get(PLATFORM.get(platform))
    # 读取cookie写入浏览器
    with open(platform+'_cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
    for cookie in listCookies:
        driver.add_cookie(cookie)
    driver.refresh()
    html = driver.page_source
    if(KEY[platform] not in html):
        return driver
    else:
        return 0
def get_driver(platform):
    s = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get(PLATFORM.get(platform))
    # 读取cookie写入浏览器
    with open(platform+'_cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
    for cookie in listCookies:
        driver.add_cookie(cookie)
    driver.refresh()
    return driver
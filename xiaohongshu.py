from lib2to3.pgen2 import driver
from pdb import post_mortem
import requests
from selenium.webdriver.common.by import By
from time import sleep
import cookie
import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Xiaohongshu:
    def __init__(self):
        self.is_start = False
        self.progress = '0%'
        self.platform = "xiaohongshu"
        cookie.proxy.new_har(options={
            'captureContent': True,
            'captureHeaders': True
        })
        self.login()
    def login(self):
        state = cookie.check_state(self.platform)
        if(state!=0):
            driver = state
        else:   
            driver = cookie.login(self.platform)
        self.driver = driver
        sleep(1)
        self.driver.refresh()
        print("登陆成功")
    def upload_file(self,filepath):
        input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input")))
        input.send_keys(filepath)
        # //div[contains(text(),'%')]
    def replace_cover(self,filepath):
        bt = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='编辑封面']")))
        bt.click()
        bt = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='上传封面']")))
        bt.click()
        input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='upload-wrapper']/input")))
        input.send_keys(filepath)
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[text()=' 设置默认封面']/../../../div[3]/div/button[2]")))
        button.click()
    def add_title(self,title):
        input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='c-input titleInput']/input")))
        input.send_keys(Keys.CONTROL+'a')
        input.send_keys(title)
    def add_describe(self,content):
        textarea = self.driver.find_element(By.XPATH,"//div[@class='topic-container']/p")
        textarea.send_keys(content)
    def add_tag(self,tags):
        input = self.driver.find_element(By.XPATH,"//div[@class='topic-container']/p")
        for tag in tags:
            input.send_keys('#')
            input.send_keys(tag)
            sleep(1)
            input.send_keys(Keys.ENTER)

    def publish(self):
        sleep(1)
        button = self.driver.find_element(By.XPATH,"//span[text()='发布']/..")
        button.click()
    def success(self):
        json = requests.get('https://creator.xiaohongshu.com/api/galaxy/creator/note/user/posted?tab=0',cookies=cookie.get_cookie(self.platform)).json()
        id = json['data']['notes'][0]['id']
        return id
xhs = Xiaohongshu()
xhs.upload_file(r"C:\Users\1\Pictures\序列 01.mp4")
xhs.replace_cover(r"C:\Users\1\Pictures\3.png")
xhs.add_title("为nmddddss奇go")
xhs.add_describe("sadsadsad华东师范ishi")
xhs.add_tag(["配音","王者荣耀"])
xhs.publish()
video_id = xhs.success()
input()
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
class Zhihu:
    def __init__(self):
        self.is_start = False
        self.progress = '0%'
        self.platform = "zhihu"
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
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='VideoUploadButton-fileInput']")))
        input = self.driver.find_element(By.XPATH,"//input[@class='VideoUploadButton-fileInput']")
        input.send_keys(filepath)
        # //div[contains(text(),'%')]
    def replace_cover(self,filepath):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='选择视频封面']")))
        bt = self.driver.find_element(By.XPATH,"//div[text()='选择视频封面']")
        bt.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='本地上传']")))
        bt = self.driver.find_element(By.XPATH,"//div[text()='本地上传']")
        bt.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@accept='image/png,image/jpeg,image/jpg']")))
        input = self.driver.find_element(By.XPATH,"//input[@accept='image/png,image/jpeg,image/jpg']")
        input.send_keys(filepath)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='确认选择']")))
        button = self.driver.find_element(By.XPATH,"//button[text()='确认选择']")    
        button.click()
    def add_title(self,title):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='输入视频标题']")))
        input = self.driver.find_element(By.XPATH,"//input[@placeholder='输入视频标题']") 
        input.send_keys(Keys.CONTROL+'a')
        input.send_keys(title)
    def add_tag(self,tags):
        button = self.driver.find_element(By.XPATH,"//button[@class='Button TopicInputAlias-placeholderButton Button--plain Button--blue Button--withIcon Button--withLabel']")
        button.click()
        input = self.driver.find_element(By.XPATH,"//div[@class='TopicInputAlias-autocomplete']//input")
        for tag in tags:
            input.send_keys(tag)
            sleep(1)
            input.send_keys(Keys.ENTER)
    def add_describe(self,content):
        textarea = self.driver.find_element(By.XPATH,"//textarea")
        textarea.send_keys(content)
    def original(self):
        button = self.driver.find_element(By.XPATH,"//label[text()='原创']")
        button.click()
    def add_type(self,types):
        button = self.driver.find_element(By.XPATH,"//div[@class='VideoUploadForm-selectContainer']/div[1]")
        button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='Select-list VideoUploadForm-selectList']/button[text()='{0}']".format(types[0]))))
        button = self.driver.find_element(By.XPATH,"//*[@class='Select-list VideoUploadForm-selectList']/button[text()='{0}']".format(types[0]))
        button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='VideoUploadForm-selectContainer']/div[2]")))
        button = self.driver.find_element(By.XPATH,"//div[@class='VideoUploadForm-selectContainer']/div[2]")
        button.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='Select-list VideoUploadForm-selectList']/button[text()='{0}']".format(types[1]))))
        button = self.driver.find_element(By.XPATH,"//*[@class='Select-list VideoUploadForm-selectList']/button[text()='{0}']".format(types[1]))
        button.click()
    def publish(self):
        sleep(1)
        button = self.driver.find_element(By.XPATH,"//button[text()='发布视频']")
        button.click()
    def success(self):
        for entry in cookie.proxy.har['log']['entries']:
            request = entry['request']
            response = entry['response']
            if('https://www.zhihu.com/api/v4/zvideos/drafts' in request['url'] and request['method']=="GET"):
                video_id = request['url'].split('/')[-1]
                return video_id
        
zh = Zhihu()
zh.upload_file(r"C:\Users\1\Pictures\序列 01.mp4")
zh.replace_cover(r"C:\Users\1\Pictures\3.png")
zh.add_title("为nmddddss奇go")
zh.add_tag(["配音","王者荣耀"])
zh.add_describe("sadsadsad华东师范ishi")
zh.add_type(["职场","其他职场"])
zh.original()
zh.publish()
video_id = zh.success()
# dy.publish()
input()
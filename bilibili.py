from pdb import post_mortem
import requests
from selenium.webdriver.common.by import By
from time import sleep
import cookie
import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class Bilibili:
    def __init__(self):
        self.is_start = False
        self.progress = '0%'
        self.platform = "bilibili"
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
        self.driver.get("https://member.bilibili.com/york/videoup?new")
        sleep(1)
        self.driver.refresh()
        print("登陆成功")
    def upload_file(self,filepath):
        while(True):
            try:    
                input_bt = self.driver.find_element(By.XPATH,"//div[@class='bcc-upload-wrapper']/input")
                break
            except:
                sleep(1)
                print("无")
        input_bt.send_keys(filepath)
        self.is_start = True
        print("文件上传")

    def replace_cover(self,filepath):
        while(True):
            try:    
                bt = self.driver.find_element(By.XPATH,"//*[contains(text(),'更改封面')]")
                print("设置封面")
                break
            except:
                try:
                    text = self.driver.find_element(By.XPATH,"//span[contains(text(),'%')]")
                    print(text.text)
                    self.progress = text.text
                    sleep(0.5)
                except:
                    sleep(0.5)
        ActionChains(self.driver).move_to_element(bt).click(bt).perform()
        sleep(1)
        # bt.click()
        while(True):
            try:    
                bt = self.driver.find_element(By.XPATH,"//div[contains(text(),'上传封面')]")
                break
            except:
                print("还没有2")
                sleep(1)
        while(True):
            try:    
                bt.click()
                break
            except:
                sleep(1)

        while(True):
            try:    
                bt = self.driver.find_element(By.XPATH,"//div[@class='cover-cut-content-upload-box']/../input")
                break
            except:
                print("还没有A")
                sleep(1)
        bt.send_keys(filepath)
        while(True):
            try:    
                bt = self.driver.find_element(By.XPATH,"//div[@class='cover-cut-footer-pick']/button[2]")
                break
            except:
                print("还没有B")    
                sleep(1)
        while(True):
            try:    
                bt.click()
                break
            except:
                sleep(1)
    
    def add_title(self,title):
        while(True):
            try:    
                input_bt = self.driver.find_element(By.XPATH,"//div[@class='form']/div[3]/div/div[2]/div/input")
                break
            except:
                sleep(1)
                print("无")
        # ActionChains(self.driver).move_to_element(bt).click(bt).perform()
        input_bt.send_keys(Keys.CONTROL+'a')
        input_bt.send_keys(title)
    def add_type(self,father_type,child_type):
        while(True):
            try:    
                input_bt = self.driver.find_element(By.XPATH,"//div[@class='form']/div[5]/div/div[2]")
                break
            except:
                sleep(1)
                print("无") 
        while(True):
            try:    
                ActionChains(self.driver).move_to_element(input_bt).perform()
                input_bt.click()
                break
            except:
                sleep(1)
                print("无") 
        while(True):
            try:    
                input_bt = self.driver.find_element(By.XPATH,"//div[@class='drop-f-wrp']//p[text()='{0}']".format(father_type))
                input_bt.click()
                break
            except:
                sleep(1)
                print("无") 
        while(True):
            try:    
                input_bt = self.driver.find_element(By.XPATH,"//div[@class='drop-t-wrp']//p[text()='{0}']".format(child_type))
                input_bt.click()
                break
            except:
                sleep(1)
                print("无") 

    def add_tag(self,tags):
       
        while(True):
            try:    
                input_bt = self.driver.find_element(By.XPATH,"//div[@class='form']/div[6]//input")
                break
            except:
                sleep(1)
                print("无")
        
        
        for item in tags:
            ActionChains(self.driver).move_to_element(input_bt).perform()
            input_bt.send_keys(item)
            input_bt.send_keys(Keys.ENTER)
    def add_describe(self,content):
        while(True):
            try:    
                input_bt = self.driver.find_element(By.XPATH,"//div[@class='form']/div[7]//div[@class='ql-editor ql-blank']")
                break
            except:
                sleep(1)
                print("无")
        ActionChains(self.driver).move_to_element(input_bt).perform()
        input_bt.send_keys(content)
    def publish(self):
        while(True):
            try:    
                input_bt = self.driver.find_element(By.XPATH,"//span[@class='submit-add']")
                break
            except:
                sleep(1)
                print("无")
        ActionChains(self.driver).move_to_element(input_bt).perform()
        input_bt.click()
    def success(self):
        list = self.get_data()
        video = sorted(list,key = lambda x:x['ptime'],reverse=True)[0]
        return video["bvid"]

    def publish(self):
        self.upload_file(r"C:\Users\1\Pictures\序列 01.mp4")
        self.replace_cover(r"C:\Users\1\Pictures\3.png")
        self.add_title("为nmddddss奇go")
        self.add_type('生活','出行')
        self.add_tag(["sadas","dsd","wqeqw得到"])
        self.add_describe("我爱你")
        self.publish()
        bvid = self.success()
        return bvid

    def process_data(self,raw_data_list):
        '''
            用来处理get——data传过来的json列表，拿到每个视频的标题、封面、bvid、播放量、点赞量、收藏量
        '''
        data_list = []
        for item in raw_data_list:
            title = item.get("Archive").get("title")
            cover = item.get("Archive").get("cover")
            bvid = item.get("Archive").get("bvid")
            view = item.get("stat").get("view")
            like = item.get("stat").get("like")
            collect = item.get("stat").get("favorite")
            ptime= item.get("Archive").get("ptime")
            audio = {
                "title":title,
                "cover":cover,
                "bvid":bvid,
                "view":view,
                "like":like,
                "collect":collect,
                "ptime":ptime
            }
            data_list.append(audio)
        return data_list

    def get_data(self):
        params = {
            'status': 'is_pubing,pubed,not_pubed',
            'pn': '1', 
            'ps': '10', 
            'coop': '1',
            'interactive': '1',
        }
        cookies = cookie.get_cookie(self.platform)
        response = requests.get('https://member.bilibili.com/x/web/archives', params=params, cookies=cookies)
        page = int(response.json().get("data").get("page").get("count"))//10+1 #页数
        # 循环获取数据
        audio_data_list = []
        for cur_page in range(1,page+1):
            params = {
                'status': 'is_pubing,pubed,not_pubed',
                'pn': str(cur_page), #页数
                'ps': '10', 
                'coop': '1',
                'interactive': '1',
            }
            response = requests.get('https://member.bilibili.com/x/web/archives', params=params, cookies=cookies)
            #获取数据
            audio_data = response.json().get("data").get("arc_audits")
            # 数据加到总列表中
            for item in audio_data:
                audio_data_list.append(item)
            # 数据处理
            new_audio_data_list = self.process_data(audio_data_list)
        return new_audio_data_list
    @staticmethod
    def get_typelist():
        cookies = cookie.get_cookie("bilibili")
        json = requests.get("https://member.bilibili.com/x/vupre/web/archive/pre",cookies=cookies).json()["data"]["typelist"]
        return json
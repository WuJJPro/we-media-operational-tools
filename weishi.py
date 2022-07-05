
from selenium.webdriver.common.by import By
from time import sleep
import cookie
import json
from selenium.webdriver.common.action_chains import ActionChains

class Tengxunweishi:
    def __init__(self):
        self.is_start = False
        self.progress = '0%'
        self.platform = "tengxunweishi"
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
        print("登陆成功")
    def upload_file(self,filepath):
        while(True):
            try:    
                input_bt = self.driver.find_element(By.XPATH,"//*[@id='content-container']/div/div/div[1]/input")
                break
            except:
                sleep(1)
        input_bt.send_keys(filepath)
        self.is_start = True
        print("文件上传")
    def add_describe(self,content):
        while(True):
            try:    
                text_area = self.driver.find_element(By.XPATH,"//textarea")
                break
            except:
                sleep(1)
        text_area.send_keys(content)
    def replace_cover(self,filepath):
        while(True):
            try:    
                bt = self.driver.find_element(By.XPATH,"//div[contains(text(),'设置封面')]")
                print("设置封面")
                break
            except:
                try:
                    text = self.driver.find_element(By.XPATH,"//span[contains(text(),'%')]/..")
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
                bt = self.driver.find_element(By.XPATH,"//div[contains(text(),'图片上传')]//..")
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
                bt = self.driver.find_element(By.XPATH,"//*[@id='rc-tabs-1-panel-imgUpload']/div/div/span/div/span/input")
                break
            except:
                print("还没有A")
                sleep(1)
        bt.send_keys(filepath)
        while(True):
            try:    
                bt = self.driver.find_element(By.XPATH,"//div[@class='ant-btn ant-btn-primary']")
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
    def publish(self):
        while(True):
            try:    
                bt = self.driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']")
                bt.click()
                break
            except:
                print("还没有")
                sleep(1)
        while(True):
            try:    
                bt = self.driver.find_element(By.XPATH,"//button[@class='ant-btn ant-btn-primary']")
                bt.click()
            except:
                break    
    def success(self):
        for entry in cookie.proxy.har['log']['entries']:
            request = entry['request']
            response = entry['response']
            if('https://videotranspond.3g.qq.com/busiproxy/notify' in request['url'] and request['method']=="POST"):
                video_id = json.loads(request['postData']['text'])['videoId']
                return video_id
    def upload(self,video):
        self.upload_file(video["filpath"])
        self.add_describe(video["describe"])
        self.replace_cover(video["cover"])
        self.publish()
        json = self.success()
        return json
    
    def get_data(self):
        self.driver.get("https://media.weishi.qq.com/media/video-manage")
        while(True):
            try:
                bt = self.driver.find_element(By.XPATH,"//div[contains(text(),'没有更多视频')]")
                break
            except:
                try:
                    bt = self.driver.find_element(By.XPATH,"//div[contains(text(),'点击加载更多视频')]")
                    bt.click()
                    print("点了")
                except:
                    sleep(0.1) 
        video_list = []
        for entry in cookie.proxy.har['log']['entries']:
            request = entry['request']
            response = entry['response']

            if("https://media.weishi.qq.com/media-api/getVideoList" in request['url']):
                result = json.loads(response['content']['text'])['feedDetailList']
                for item in result:
                    video_list.append(item)
        return video_list
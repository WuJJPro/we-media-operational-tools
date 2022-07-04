from platform import platform
from selenium.webdriver.common.by import By
from time import sleep
import cookie
from selenium.webdriver.common.action_chains import ActionChains
# 无头浏览器的配置
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
class Tengxunweishi:
    def __init__(self):
        self.is_start = False
        self.progress = '0%'
        self.platform = "tengxunweishi"
        self.login()
    def login(self):
        state = cookie.check_state(self.platform)
        if(state!=0):
            driver = state
        else:   
            driver = cookie.login(self.platform)
        self.driver = driver
    def upload_file(self,filepath):
        while(True):
            try:    
                input_bt = self.driver.find_element(By.XPATH,"//*[@id='content-container']/div/div/div[1]/input")
                break
            except:
                print("还没有")
                sleep(1)
        input_bt.send_keys(filepath)
        self.is_start = True
    def add_describe(self,content):
        while(True):
            try:    
                text_area = self.driver.find_element(By.XPATH,"//textarea")
                break
            except:
                print("还没有")
                sleep(1)
        text_area.send_keys(content)
    def replace_cover(self,filepath):
        while(True):
            try:    
                bt = self.driver.find_element(By.XPATH,"//div[contains(text(),'设置封面')]")
                break
            except:
                try:
                    text = self.driver.find_element(By.XPATH,"//span[contains(text(),'%')]/..")
                    print(text.text)
                    self.progress = text.text
                    sleep(0.5)
                except:
                    print("shipai")
                    sleep(0.5)
        ActionChains(self.driver).move_to_element(bt).click(bt).perform()
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
                print("还没有")
                sleep(1)
        bt.send_keys(filepath)
        while(True):
            try:    
                bt = self.driver.find_element(By.XPATH,"//div[@class='ant-btn ant-btn-primary']")
                break
            except:
                print("还没有")
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
                break
            except:
                print("还没有")
                sleep(1)
        while(True):
            try:    
                bt.click()
                break
            except:
                sleep(1)
pf = Tengxunweishi()
pf.upload_file(r"E:\快把满分带走\意象\高考古诗词常见意象整理Part 4 自然现象.mp4")
pf.add_describe("#gugu #uu #joj")
pf.replace_cover(r"C:\Users\1\Pictures\1.png")
pf.publish()
a = input()
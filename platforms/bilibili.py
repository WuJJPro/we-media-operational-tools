# 启动playwright
# playwright install
import json

from common.web import Browser

browser = Browser()
page = browser.get_page()
page.goto("https://www.bilibili.com/")

# 读取cookie
with open("bilibili_cookies.json", "r") as f:
    cookie = json.load(f)

# 设置cookie
browser.set_cookie(cookie)
page.goto("https://member.bilibili.com/platform/upload/video/frame?page_from=creative_home_top_upload")

# xpath定位
input_file = page.query_selector("//div[@class='bcc-upload-wrapper']//input")
input_file.set_input_files("test.mp4")

print(2)
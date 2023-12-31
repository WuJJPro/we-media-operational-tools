import threading

from playwright.sync_api import sync_playwright


class BrowserMeta(object):
    """
        Playwright browser class
        单例模式, 保证只有一个浏览器实例
        所有接口方法都是同步的
    """

    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__new__(cls)
                    cls.__instance.__init()
        return cls.__instance

    def __init(self):
        self.__browser = None
        self.__context = None
        self.__page = None

    def __init(self):
        self.__browser = None
        self.__context = None
        self.__page = None

    def __init_browser(self):
        self.p = sync_playwright().start()
        self.__browser = self.p.chromium.launch(headless=False)
        self.__context = self.__browser.new_context()
        self.__page = self.__context.new_page()

    def __del__(self):
        if self.__browser is not None:
            self.__browser.close()
            self.p.stop()


    def get_browser(self):
        if self.__browser is None:
            self.__init_browser()
        return self.__browser

    def get_context(self):
        if self.__context is None:
            self.__init_browser()
        return self.__context

    def get_page(self):
        if self.__page is None:
            self.__init_browser()
        return self.__page


class Browser(BrowserMeta):
    """
        Playwright browser class
        单例模式, 保证只有一个浏览器实例
        所有接口方法都是同步的
    """

    def get_cookie(self):
        """
            获取cookie
        """
        return self.get_context().cookies()

    def set_cookie(self, dict_cookie):
        """
            设置cookie
        """
        self.get_context().add_cookies(dict_cookie)



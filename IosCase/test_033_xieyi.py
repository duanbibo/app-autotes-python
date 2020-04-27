import unittest
from time import sleep
from util.driver import Driver
from util.image import Appium_Extend


class Case(unittest.TestCase):
    # 服务隐私协议
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_xieyi(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_accessibility_id("注册/登录即代表已阅读并同意《用户协议及隐私条款》").click()
        sleep(5)
        self.assertIn("产品和服务说明", driver.page_source)


    def tearDown(self):
        if "back" in self.driver.page_source:
            self.driver.find_element_by_accessibility_id("back").click()
        else:
            sleep(2)



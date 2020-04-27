import unittest
from time import sleep
from util.driver import Driver
from util.image import Appium_Extend


class Case(unittest.TestCase):
    # 退出登录
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_logout(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_accessibility_id("我的").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='设置']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='退出登录']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='确定']").click()
        sleep(2)
        self.assertIn("欢迎登录", driver.page_source)


    def tearDown(self):
        if "back" in self.driver.page_source:
            self.driver.find_element_by_accessibility_id("back").click()
        else:
            sleep(2)



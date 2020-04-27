import unittest
from time import sleep
from util.driver import Driver
from util.image import Appium_Extend

class Case(unittest.TestCase):
    # 购买服务
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_fuwu(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_accessibility_id("我的").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='购买服务']").click()
        sleep(3)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='确认支付']").click()
        sleep(2)
        self.assertIn("微信",driver.page_source)
        self.assertIn("支付宝",driver.page_source)
        sleep(1)
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='close']").click()
        sleep(1)
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='back']").click()

    def tearDown(self):
        if "back" in self.driver.page_source:
            self.driver.find_element_by_accessibility_id("back").click()
        else:
            sleep(2)



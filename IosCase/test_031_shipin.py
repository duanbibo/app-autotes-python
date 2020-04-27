import unittest
from time import sleep
from util.driver import Driver
from util.image import Appium_Extend


class Case(unittest.TestCase):
    # 视频
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_shipin(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_accessibility_id("我的").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='视频语音']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='视频:1元/10分钟']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='08:00-12:00'][1]").click()
        sleep(1)

        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='确定']").click()
        sleep(2)
        self.assertIn("微信支付", driver.page_source)
        self.assertIn("支付宝", driver.page_source)
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='back']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='back']").click()

    def tearDown(self):
        if "back" in self.driver.page_source:
            self.driver.find_element_by_accessibility_id("back").click()
        else:
            sleep(2)



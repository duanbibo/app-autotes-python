import unittest
from time import sleep
from util.driver import Driver
from util.image import Appium_Extend

class Case(unittest.TestCase):
    # 门诊就诊
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_menzhen(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_accessibility_id("我的").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='门诊就诊']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='预约就诊(门诊)']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='我的签约医生']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='上午']").click()
        sleep(1)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='确定']").click()
        sleep(2)
        self.assertIn("电饭锅",driver.page_source)
        self.assertIn("预约中",driver.page_source)
        sleep(1)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='取消就诊']").click()
        sleep(1)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='确定取消']").click()
        sleep(2)
        self.assertNotIn("预约中",driver.page_source)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='预约历史']").click()
        sleep(2)
        self.assertIn("已取消", driver.page_source)
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='back']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='back']").click()

    def tearDown(self):
        if "back" in self.driver.page_source:
            self.driver.find_element_by_accessibility_id("back").click()
        else:
            sleep(2)



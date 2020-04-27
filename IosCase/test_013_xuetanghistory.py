from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver


class Case(unittest.TestCase):
    # 血糖历史
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_historyxuetang(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_accessibility_id("达标").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='用药达标']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='血糖']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='历史']").click()
        sleep(2)
        self.assertIn("空腹", driver.page_source)
        self.assertIn("5.1", driver.page_source)
        sleep(2)
        # 全屏有bug，暂时不做
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='表格图']").click()
        sleep(2)
        self.assertIn("5.1", driver.page_source)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='至']").click()
        sleep(2)
        self.assertIn("开始时间", driver.page_source)
        self.assertIn("结束时间", driver.page_source)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='取消']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='back']").click()
        sleep(2)

    def tearDown(self):
        if "back" in self.driver.page_source:
            self.driver.find_element_by_accessibility_id("back").click()
        else:
            sleep(2)



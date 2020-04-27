from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver


class Case(unittest.TestCase):
    #添加血糖
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_historyxueya(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_accessibility_id("达标").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='用药达标']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='血糖']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='手动上传']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField").clear()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField").send_keys("5.1")
        sleep(2)
        kongfuxuetang=driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField").text
        sleep(2)
        driver.find_element_by_accessibility_id("请左右滑动调整您的数据").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='保存']").click()
        sleep(5)
        html=driver.page_source
        cishu=html.count(kongfuxuetang)
        self.assertTrue(cishu>=4)

    def tearDown(self):
        if "back" in self.driver.page_source:
            self.driver.find_element_by_accessibility_id("back").click()
        else:
            sleep(2)



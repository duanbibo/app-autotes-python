import unittest
from time import sleep
from util.driver import Driver
from util.image import Appium_Extend


class Case(unittest.TestCase):
    # 创建账号修改密码
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_cjxg(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_accessibility_id("没有账号？创建一个").click()
        sleep(1)
        driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTextField").send_keys("13800138000")
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='发送验证码']").click()
        sleep(4)
        self.assertIn("已发送成功", driver.page_source)
        sleep(1)
        driver.find_element_by_accessibility_id("login back").click()
        sleep(1)
        driver.find_element_by_accessibility_id("login close").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='忘记密码']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeTextField").send_keys("15600576351")
        sleep(1)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='发送验证码']").click()
        sleep(2)
        self.assertIn("已发送成功",driver.page_source)

    def tearDown(self):
        self.driver.find_element_by_accessibility_id("login back").click()
        sleep(1)
        self.driver.find_element_by_accessibility_id("login close").click()



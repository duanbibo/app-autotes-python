from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver
import time

class Case(unittest.TestCase):
 #我的页面底部设备+客服+设置
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_setting(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("我的").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='设备管理']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='扫描绑定']").click()
    self.assertIn("开头的商品码",driver.page_source)
    driver.find_element_by_xpath("//XCUIElementTypeButton[@name='back']").click()
    driver.find_element_by_xpath("//XCUIElementTypeButton[@name='back']").click()
    sleep(2)
    driver.find_element_by_accessibility_id("客服").click()
    sleep(2)
    self.assertIn("6800 5697‬",driver.page_source)
    sleep(2)
    driver.find_element_by_accessibility_id("取消").click()
    sleep(1)
    driver.find_element_by_accessibility_id("设置").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='重置密码']").click()
    sleep(2)
    self.assertIn("旧密码",driver.page_source)
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeButton[@name='back']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='关于我们']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='服务热线：01068005697']").click()
    sleep(2)
    self.assertIn("6800 5697‬", driver.page_source)
    sleep(2)
    driver.find_element_by_accessibility_id("取消").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='使用条款和隐私协议']").click()
    sleep(7)
    self.assertIn("用户在注册账号前", driver.page_source)
    sleep(2)
    for ba in range(0,3):
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='back']").click()
        sleep(2)


  def tearDown(self):
    if "back" in self.driver.page_source:
      self.driver.find_element_by_accessibility_id("back").click()
    else:
      sleep(2)



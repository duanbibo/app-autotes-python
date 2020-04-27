from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver
import time

class Case(unittest.TestCase):
 #我的订单
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_dingdan(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("我的").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='我的订单']").click()
    sleep(2)
    self.assertIn("订单编号", driver.page_source)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='未完成']").click()
    sleep(2)
    self.assertIn("进行中", driver.page_source)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='已完成']").click()
    sleep(2)
    if "已取消" in driver.page_source:
        self.assertIn("已取消",driver.page_source)
    elif "已完成" in driver.page_source:
        self.assertIn("已完成",driver.page_source)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='退款']").click()
    sleep(2)
    self.assertIn("退款成功", driver.page_source)
    driver.find_element_by_accessibility_id("back").click()

  def tearDown(self):
    if "back" in self.driver.page_source:
       self.driver.find_element_by_accessibility_id("back").click()
    else:
       sleep(2)



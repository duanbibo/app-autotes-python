from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver
import time

class Case(unittest.TestCase):
 #我的积分
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_jifen(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("我的").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='我的积分']").click()
    sleep(2)
    self.assertIn("今日获取分数", driver.page_source)
    self.assertIn("兑换规则请以兑换活动为准", driver.page_source)
    driver.find_element_by_xpath("//XCUIElementTypeButton[@name='back']").click()
    sleep(2)


  def tearDown(self):
    if "back" in self.driver.page_source:
      self.driver.find_element_by_accessibility_id("back").click()
    else:
      sleep(2)



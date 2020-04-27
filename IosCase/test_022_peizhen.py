from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver
import time

class Case(unittest.TestCase):
 #陪诊服务-3。5。5版本取消，暂时不执行
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_peizhen(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("我的").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='陪诊服务']").click()
    sleep(2)
    driver.find_element_by_accessibility_id("门诊陪诊").click()
    sleep(6)
    self.assertIn("挂号网", driver.page_source)
    if "不允许" in driver.page_source:
        driver.find_element_by_accessibility_id("好").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='关闭']").click()
    sleep(2)
    driver.find_element_by_accessibility_id("护士上门").click()
    sleep(6)
    self.assertIn("保胎针", driver.page_source)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='关闭']").click()
    sleep(2)
    driver.find_element_by_accessibility_id("back").click()

  def tearDown(self):
    if "back" in self.driver.page_source:
       self.driver.find_element_by_accessibility_id("back").click()
    else:
       sleep(2)



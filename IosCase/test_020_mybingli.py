from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver
import time

class Case(unittest.TestCase):
 #我的积分
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_mybingli(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("我的").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='我的病历']").click()
    sleep(2)
    self.assertIn("基本信息", driver.page_source)
    self.assertIn("肾功能不全", driver.page_source)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='我的单据']").click()
    sleep(2)
    driver.find_element_by_accessibility_id("back").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='化验检查']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='生化全项']").click()
    sleep(2)
    self.assertIn("合格", driver.page_source)
    driver.find_element_by_accessibility_id("back").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='检查单']").click()
    sleep(2)
    self.assertIn("大病历", driver.page_source)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='我的图片']").click()
    sleep(2)
    self.assertIn("合格", driver.page_source)
    sleep(2)

  def tearDown(self):
    if "back" in self.driver.page_source:
      self.driver.find_element_by_accessibility_id("back").click()
    else:
      sleep(2)



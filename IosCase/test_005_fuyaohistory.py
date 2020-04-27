from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver
from appium.webdriver.common.touch_action import TouchAction

class Case(unittest.TestCase):
 #查看服药历史
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_fyhistory(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("服药").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='服药完成率']").click()
    sleep(2)
    self.assertIn("13",driver.page_source)
    driver.find_element_by_accessibility_id("总览").click()
    sleep(2)
    self.assertIn("2周", driver.page_source)
    self.assertIn("1月", driver.page_source)
    driver.find_element_by_accessibility_id("back").click()
    sleep(2)
    driver.find_element_by_accessibility_id("back").click()


  def tearDown(self):
    if "back" in self.driver.page_source:
      self.driver.find_element_by_accessibility_id("back").click()
    else:
      sleep(2)



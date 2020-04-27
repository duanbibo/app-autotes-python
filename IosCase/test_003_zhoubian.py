from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver

class Login(unittest.TestCase):
 #周边推荐
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_dsjnews(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("对话").click()
    sleep(2)
    driver.find_element_by_accessibility_id("icon toolview add normal").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeButton[@name='周边推荐']").click()
    sleep(2)
    if "不允许" in driver.page_source:
        driver.switch_to.alert.accept()
    sleep(1)
    tab=['医院','体检','药店']
    for asser in tab:
        self.assertIn(asser,driver.page_source)
    sleep(2)


  def tearDown(self):
    if "back" in self.driver.page_source:
      self.driver.find_element_by_accessibility_id("back").click()
    else:
      sleep(2)



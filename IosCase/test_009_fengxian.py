from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver

class Case(unittest.TestCase):
 #风险评估
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_fengxian(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("达标").click()
    sleep(2)
    if "不允许" in driver.page_source:
        driver.find_element_by_accessibility_id("不允许").click()
        sleep(2)
        driver.find_element_by_accessibility_id("好").click()
        sleep(1)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='风险评估']").click()
    sleep(2)
    self.assertIn("吸烟史",driver.page_source)
    sleep(2)
    driver.find_element_by_accessibility_id("back").click()


  def tearDown(self):
    if "back" in self.driver.page_source:
      self.driver.find_element_by_accessibility_id("back").click()
    else:
      sleep(2)



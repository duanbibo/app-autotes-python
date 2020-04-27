from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver

class Case(unittest.TestCase):
 #说明书+删除服药
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_delyao(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("服药").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='蒙诺 | 福辛普利钠']").click()
    sleep(2)
    driver.find_element_by_accessibility_id("药品说明书").click()
    sleep(8)
    self.assertIn("可与利尿剂合用",driver.page_source)
    sleep(1)
    driver.find_element_by_accessibility_id("back").click()
    sleep(1)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='蒙诺 | 福辛普利钠']").click()
    sleep(2)
    driver.find_element_by_accessibility_id("修改服药计划").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='删除']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeButton[@name='删除']").click()
    sleep(5)
    self.assertNotIn("福辛普利钠",driver.page_source)

  def tearDown(self):
    if "back" in self.driver.page_source:
      self.driver.find_element_by_accessibility_id("back").click()
    else:
      sleep(2)



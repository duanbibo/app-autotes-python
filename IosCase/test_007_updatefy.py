from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver

class Case(unittest.TestCase):
 #修改服药
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_upyao(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("服药").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='蒙诺 | 福辛普利钠']").click()
    sleep(2)
    driver.find_element_by_accessibility_id("修改服药计划").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='修改']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeButton[@name='早上'][1]").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeButton[@name='中午'][1]").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeButton/XCUIElementTypeStaticText").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeButton[@name='晚上'][1]").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeButton/XCUIElementTypeStaticText").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='保存']").click()
    sleep(3)
    self.assertIn("12:00",driver.page_source)
    self.assertIn("19:00", driver.page_source)

  def tearDown(self):
    if "back" in self.driver.page_source:
      self.driver.find_element_by_accessibility_id("back").click()
    else:
      sleep(2)



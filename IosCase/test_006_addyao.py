from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver

class Case(unittest.TestCase):
 #添加服药
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_addyao(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("服药").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=' + 添加新药']").click()
    sleep(3)
    if "不允许" in driver.page_source:
      driver.switch_to.alert.accept()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField").click()
    sleep(2)
    driver.find_element_by_accessibility_id("蒙诺").click()
    sleep(2)
    driver.find_element_by_accessibility_id("福辛普利钠片 (蒙诺)").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeButton[@name='14片']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeButton[@name='选中']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='保存']").click()
    sleep(2)
    if "知道了" in driver.page_source:
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='知道了']").click()
    sleep(2)
    self.assertIn("福辛普利钠片",driver.page_source)
    self.assertIn("07:00", driver.page_source)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='服药状态']").click()
    sleep(2)
    self.assertIn("下次服药", driver.page_source)
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='服药计划']").click()

  def tearDown(self):
    if "back" in self.driver.page_source:
      self.driver.find_element_by_accessibility_id("back").click()
    else:
      sleep(2)



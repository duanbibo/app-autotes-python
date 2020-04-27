from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver
import time

class Case(unittest.TestCase):
 #添加运动
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_addreport(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("达标").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='生活达标']").click()
    sleep(2)
    driver.find_element_by_accessibility_id("上传运动情况").click()
    sleep(8)
    driver.find_element_by_xpath("//XCUIElementTypeOther[@name='运动调查表']/XCUIElementTypeOther[2]/XCUIElementTypeStaticText").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='散步']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='0.5-1小时']").click()
    sleep(1)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='大汗']").click()
    sleep(1)
    driver.find_element_by_xpath("//XCUIElementTypeOther[@name='运动调查表']/XCUIElementTypeOther[34]/XCUIElementTypeStaticText").click()
    sleep(1)
    driver.find_element_by_accessibility_id("上传").click()
    sleep(8)
    riqi=time.strftime('%Y-%m-%d', time.localtime(time.time())) #获取当前的年月日
    sleep(2)
    self.assertIn(riqi,driver.page_source)
    self.assertIn("散步", driver.page_source)



  def tearDown(self):
    if "back" in self.driver.page_source:
      self.driver.find_element_by_accessibility_id("back").click()
    else:
      sleep(2)



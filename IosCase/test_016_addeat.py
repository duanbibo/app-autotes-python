from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver
import time

class Case(unittest.TestCase):
 #添加饮食
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_addreport(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("达标").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='生活达标']").click()
    sleep(2)
    driver.find_element_by_accessibility_id("饮食").click()
    sleep(1)
    driver.find_element_by_accessibility_id("上传饮食情况").click()
    sleep(8)
    driver.find_element_by_accessibility_id("<1碗").click()
    sleep(1)
    driver.find_element_by_xpath("//XCUIElementTypeOther[@name='饮食调查表']/XCUIElementTypeOther[6]//XCUIElementTypeStaticText").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeOther[@name='饮食调查表']/XCUIElementTypeOther[9]//XCUIElementTypeStaticText").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeOther[@name='饮食调查表']/XCUIElementTypeOther[12]//XCUIElementTypeStaticText").click()
    sleep(1)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='淡']").click()
    sleep(1)
    driver.find_element_by_xpath("//XCUIElementTypeOther[@name='饮食调查表']/XCUIElementTypeOther[18]//XCUIElementTypeStaticText").click()
    sleep(1)
    driver.find_element_by_xpath("//XCUIElementTypeOther[@name='饮食调查表']/XCUIElementTypeOther[21]//XCUIElementTypeStaticText").click()
    sleep(1)
    driver.find_element_by_xpath("//XCUIElementTypeOther[@name='饮食调查表']/XCUIElementTypeOther[24]//XCUIElementTypeStaticText").click()
    driver.find_element_by_accessibility_id("上传").click()
    sleep(8)
    riqi=time.strftime('%Y-%m-%d', time.localtime(time.time())) #获取当前的年月日
    sleep(2)
    self.assertIn(riqi,driver.page_source)
    self.assertIn("1碗", driver.page_source)



  def tearDown(self):
    if "back" in self.driver.page_source:
      self.driver.find_element_by_accessibility_id("back").click()
    else:
      sleep(2)



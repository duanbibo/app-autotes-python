from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver
import time

class Case(unittest.TestCase):
 #添加睡眠
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_addreport(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("达标").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='生活达标']").click()
    sleep(2)
    driver.find_element_by_accessibility_id("睡眠").click()
    sleep(1)
    driver.find_element_by_accessibility_id("上传睡眠情况").click()
    sleep(8)
    driver.find_element_by_accessibility_id("优").click()
    sleep(2)
    driver.find_element_by_accessibility_id("轻").click()
    sleep(2)
    driver.find_element_by_accessibility_id("偶尔").click()
    sleep(1)
    driver.find_element_by_xpath("//XCUIElementTypeOther[@name='睡眠调查表']/XCUIElementTypeOther[14]/XCUIElementTypeStaticText").click()
    sleep(1)
    driver.find_element_by_xpath("//XCUIElementTypeOther[@name='睡眠调查表']/XCUIElementTypeOther[17]/XCUIElementTypeStaticText").click()
    sleep(1)
    driver.find_element_by_accessibility_id("上传").click()
    sleep(8)
    riqi=time.strftime('%Y-%m-%d', time.localtime(time.time())) #获取当前的年月日
    sleep(2)
    self.assertIn(riqi,driver.page_source)
    self.assertIn("偶尔", driver.page_source)



  def tearDown(self):
    if "back" in self.driver.page_source:
      self.driver.find_element_by_accessibility_id("back").click()
    else:
      sleep(2)



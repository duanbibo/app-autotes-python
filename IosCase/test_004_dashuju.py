from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver
from appium.webdriver.common.touch_action import TouchAction

class Login(unittest.TestCase):
 #大数据提醒+健康咨询
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_dsjnews(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("对话").click()
    sleep(3)
    driver.find_element_by_accessibility_id("提醒").click()
    sleep(2)
    self.assertIn("您好",driver.page_source)
    sleep(2)
    driver.find_element_by_accessibility_id("back").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeButton[@name='健康资讯']").click()
    sleep(2)
    for i in range(0,11):
        hd = huadong()
        hd.swipeDown(2000)
    sleep(4)
    driver.find_element_by_accessibility_id("搭桥手术的时间和过程").click()
    sleep(8)
    self.assertIn("家属需耐心等待", driver.page_source)
    sleep(2)



  def tearDown(self):
    if "back" in self.driver.page_source:
      self.driver.find_element_by_accessibility_id("back").click()
    else:
      sleep(2)



from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver
from util.swipe import huadong

class Case(unittest.TestCase):
 #添加亲友
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_qinyou(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("我的").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='我的亲友']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='添加']").click()
    sleep(2)
    if "保存" not in driver.page_source:
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='del']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='删除']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='添加']").click()
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='头像']").click()
    driver.find_element_by_accessibility_id("拍照").click()
    driver.find_element_by_accessibility_id("PhotoCapture").click()
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='使用照片']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField").send_keys("自动化测试")
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeTextField").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeTextField").send_keys("15666111111")
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='配偶']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[5]").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='确定']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='保存']").click()
    sleep(2)
    if "自动化测试" not in driver.page_source:
        aaa=huadong()
        for h in range(0,2):
          aaa.swipLeft(2000)
          sleep(1)
    self.assertIn("自动化测试",driver.page_source)
    sleep(1)


  def tearDown(self):
    if "back" in self.driver.page_source:
       self.driver.find_element_by_accessibility_id("back").click()
    else:
       sleep(2)



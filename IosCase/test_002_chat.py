
import unittest
from time import sleep
from util.driver import Driver
from appium.webdriver.common.touch_action import TouchAction

class Login(unittest.TestCase):
 #对话发送语音+文字
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_chat(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("对话").click()
    sleep(2)
    # driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView").click()
    # sleep(2)
    # driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView").send_keys("ios自动化测试发送")
    # sleep(2)
    # driver.find_element_by_accessibility_id("Send").click()
    # sleep(2)
    # input=driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeScrollView").text
    # self.assertEqual(input,"")
    driver.find_element_by_accessibility_id("发语音").click()
    sleep(2)
    if "不允许" in driver.page_source:
       driver.switch_to.alert.accept()
    sleep(2)
    element=driver.find_element_by_xpath("//XCUIElementTypeButton[@name='按住说话']")
    action = TouchAction(driver)
    action.long_press(element, None, None, 2000).wait(1000).release().perform()
    sleep(2)
    if "2" in driver.page_source:
      self.assertIn('2',driver.page_source)
    elif "3" in driver.page_source:
      self.assertIn('3', driver.page_source)
    elif "4" in driver.page_source:
      self.assertIn("4",driver.page_source)
    else:
      self.assertEqual(1,2)

  def tearDown(self):
    if "back" in self.driver.page_source:
      self.driver.find_element_by_accessibility_id("back").click()
    else:
      sleep(2)



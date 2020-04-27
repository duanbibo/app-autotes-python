
import unittest
from time import sleep
from util.driver import Driver


class Login(unittest.TestCase):

  def setUp(self):
    self.driver = Driver.DRIVER


  def test_login(self):
    driver = self.driver
    sleep(2)
    for i in range(0,4):
      if "不允许" in driver.page_source:
        driver.switch_to.alert.accept()
      else:
        sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeButton[@name='login close']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeButton[@name='手机登录']").click()
    sleep(2)
    driver.find_element_by_class_name("XCUIElementTypeTextField").send_keys("15600576351")
    sleep(1)
    driver.find_element_by_class_name("XCUIElementTypeSecureTextField").send_keys("111111")
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeButton[@name='登录']").click()
    sleep(8)
    self.assertIn("对话", driver.page_source)

  def tearDown(self):
    pass


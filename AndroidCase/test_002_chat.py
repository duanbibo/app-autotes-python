import unittest
from time import sleep
from util.driver import Driver
from appium.webdriver.common.touch_action import TouchAction

class chat(unittest.TestCase):

  def setUp(self):
    self.driver = Driver.DRIVER


  def test_login(self):
    driver = self.driver
    sleep(2)
    page_source = driver.page_source
    self.assertIn("电饭锅" or "上级医生" or "下级医生" or "护士", page_source)
    driver.find_element_by_id("cn.xinzhili.core:id/buttonAudioMessage").click()
    sleep(1)
    element=driver.find_element_by_id("cn.xinzhili.core:id/audioRecord")
    action=TouchAction(driver)
    action.long_press(element,None,None,2000).wait(2000).perform()
    if "拒绝" in driver.page_source:
      driver.switch_to.alert.accept()
      sleep(3)
      action.long_press(element, None, None, 2000).wait(2000).perform()
    sleep(2)
    if "2" in driver.page_source:
      self.assertIn('2',driver.page_source)
    elif "3" in driver.page_source:
      self.assertIn('3', driver.page_source)
    else:
      self.assertEqual(1,2)


  def tearDown(self):
    pass
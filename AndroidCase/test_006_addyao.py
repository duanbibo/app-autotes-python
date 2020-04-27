import unittest
from time import sleep
from util.driver import Driver
from util.swipe import huadong
from util.isElement import iselement

class addyao(unittest.TestCase):
#添加服药
  def setUp(self):
    self.driver = Driver.DRIVER

  def test_addyao(self):
    driver = self.driver
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[2]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='+添加新药']").click()
    sleep(2)
    if "允许" in driver.page_source:
      driver.switch_to.alert.accept()
      sleep(2)
    driver.find_element_by_xpath("//*[@text='药品名（选填）']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='蒙诺']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='福辛普利钠片']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='14片']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='选中']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='保存']").click()
    sleep(2)
    self.assertIn('07:00',driver.page_source)
    sleep(2)
    driver.find_element_by_xpath("//*[@text='服药状态']").click()
    sleep(1)
    self.assertIn('下次服药'or'错过服药',driver.page_source)
    sleep(1)

  def tearDown(self):
    self.driver = Driver.DRIVER
    exit = iselement()
    back = exit.findelementid("cn.xinzhili.core:id/iv_title_back")
    back2 = exit.findelementid("cn.xinzhili.core:id/iv_title_left")
    if back is True:
      self.driver.find_element_by_id("cn.xinzhili.core:id/iv_title_back").click()
    else:
      sleep(2)
    if back2 is True:
      self.driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left").click()
    else:
      sleep(2)
import unittest
from time import sleep
from util.driver import Driver
from util.swipe import huadong
from util.isElement import iselement

class fuyaolishi(unittest.TestCase):
#服药历史
  def setUp(self):
    self.driver = Driver.DRIVER

  def test_fuyaolishi(self):
    driver = self.driver
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[2]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='服药完成率']").click()
    sleep(2)
    self.assertIn('16',driver.page_source)
    sleep(2)
    driver.find_element_by_xpath("//*[@text='总览']").click()
    sleep(1)
    self.assertIn('全部已服'and'服药总览',driver.page_source)
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left").click()
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left").click()


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
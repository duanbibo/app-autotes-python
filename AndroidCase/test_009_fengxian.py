import unittest
from time import sleep
from util.driver import Driver
from util.swipe import huadong
from util.isElement import iselement

class delyao(unittest.TestCase):
#查看风险评估
  def setUp(self):
    self.driver = Driver.DRIVER

  def test_fengxian(self):
    driver = self.driver
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[3]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='冠心病']").click()
    sleep(2)
    hua = huadong()
    for i in range(0,2):
        if '痛风' in driver.page_source:
            self.asserIn('风险因素', driver.page_source)
            break
        else:
           hua.swipeUp(2000)
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
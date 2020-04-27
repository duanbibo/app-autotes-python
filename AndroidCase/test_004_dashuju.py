import unittest
from time import sleep
from util.driver import Driver
from util.swipe import huadong
from util.isElement import iselement

class dashuju(unittest.TestCase):

  def setUp(self):
    self.driver = Driver.DRIVER

  def test_zixun(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/iv_remind").click()
    sleep(2)
    if("医生通知" in driver.page_source):
        self.assertIn("医生通知", driver.page_source)
    else:
        hd = huadong()
        for h in range(0,4):
            hd.swipeUp(2000)
            if("医生通知" in driver.page_source):
                self.assertIn("医生通知", driver.page_source)
            break


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
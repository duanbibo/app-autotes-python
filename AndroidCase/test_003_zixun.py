import unittest
from time import sleep
from util.driver import Driver
from util.swipe import huadong
from util.isElement import iselement

class zixun(unittest.TestCase):

  def setUp(self):
    self.driver = Driver.DRIVER

  def test_zixun(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_xpath("//*[@text='健康资讯']").click()
    sleep(2)
    for h in range(0,4):
        if("起搏器植入" in driver.page_source):
            driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/rv_health_news']/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.TextView").click()
            break
        else:
            hd = huadong()
            hd.swipeUp(2000)
    sleep(5)
    page_source2 = driver.page_source
    self.assertIn("局部出血"or"事件的发生"or"危险因素",page_source2)

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

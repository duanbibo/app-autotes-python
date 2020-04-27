import unittest
from time import sleep
from util.driver import Driver
from util.swipe import huadong
from util.isElement import iselement

class delyao(unittest.TestCase):
#查看说明书后删除服药
  def setUp(self):
    self.driver = Driver.DRIVER

  def test_delyao(self):
    driver = self.driver
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[2]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='服药计划']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='蒙诺 | 福辛普利钠']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='药品说明书']").click()
    sleep(5)
    self.assertIn('用法用量',driver.page_source)
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='蒙诺 | 福辛普利钠']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='修改服药计划']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='删除']").click()
    sleep(1)
    driver.find_element_by_xpath("//*[@text='删除']").click()
    sleep(3)
    self.assertNotIn('福辛普利钠',driver.page_source)

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
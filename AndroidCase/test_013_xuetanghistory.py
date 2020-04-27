import unittest
from time import sleep
from util.driver import Driver
from util.swipe import huadong
from util.isElement import iselement


class xuetanghistory(unittest.TestCase):
#查看血糖历史
  def setUp(self):
    self.driver = Driver.DRIVER

  def test_xuetanghistory(self):
    driver = self.driver
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[3]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='血压']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='血糖']").click()
    sleep(1)
    driver.find_element_by_xpath("//*[@text='历史']").click()
    sleep(2)
    self.assertIn("血糖历史",driver.page_source)
    sleep(2)
    driver.find_element_by_xpath("//*[@text='全屏']").click()
    sleep(2)
    self.assertIn("血糖曲线"and"空腹",driver.page_source)
    sleep(2)
    driver.find_element_by_xpath("//*[@text='关闭']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='表格图']").click()
    sleep(2)
    self.assertIn("日期" and "睡前", driver.page_source)
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/btn_select_date").click()
    sleep(2)
    self.assertIn("开始时间" and "结束时间", driver.page_source)
    sleep(2)
    driver.find_element_by_xpath("//*[@text='确定']").click()
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
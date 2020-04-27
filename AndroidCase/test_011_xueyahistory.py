import unittest
from time import sleep
from util.driver import Driver
from util.swipe import huadong
from util.isElement import iselement


class delyao(unittest.TestCase):
#查看血压历史
  def setUp(self):
    self.driver = Driver.DRIVER

  def test_xueyahistory(self):
    driver = self.driver
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[3]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='血压']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='历史']").click()
    sleep(2)
    self.assertIn("趋势图"and"表格图",driver.page_source)
    exit = iselement()
    jieguo1=exit.findelementid("cn.xinzhili.core:id/line_view_blood")
    jieguo2=exit.findelementid("cn.xinzhili.core:id/line_view_heart_rate")
    sleep(2)
    self.assertEqual(jieguo1 and jieguo2,True)
    sleep(2)
    driver.find_element_by_xpath("//*[@text='全屏']").click()
    sleep(2)
    self.assertIn('曲线',driver.page_source)
    sleep(2)
    driver.find_element_by_xpath("//*[@text='关闭']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='表格图']").click()
    sleep(2)
    self.assertIn('日期'and'高压' and '低压', driver.page_source)
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/btn_select_date").click()
    sleep(2)
    self.assertIn('开始时间' and '结束时间', driver.page_source)
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
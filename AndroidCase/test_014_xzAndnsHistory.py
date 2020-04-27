import unittest
from time import sleep
from util.driver import Driver
from util.swipe import huadong
from util.isElement import iselement


class xuezhiniaosuanistory(unittest.TestCase):
#查看血脂，尿酸历史
  def setUp(self):
    self.driver = Driver.DRIVER

  def test_xznshistory(self):
    driver = self.driver
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[3]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='血压']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='血脂']").click()
    sleep(2)
    self.assertIn("最后一次记录"and"甘油三酯",driver.page_source)
    sleep(2)
    driver.find_element_by_xpath("//*[@text='历史']").click()
    sleep(2)
    self.assertIn("血脂历史"and"低密度脂蛋白",driver.page_source)
    sleep(3)
    driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left")
    sleep(3)
    driver.find_element_by_xpath("//*[@text='尿酸']").click()
    sleep(2)
    self.assertIn("最后一次记录" and "尿酸", driver.page_source)
    sleep(2)
    driver.find_element_by_xpath("//*[@text='历史']").click()
    sleep(2)
    self.assertIn("血尿酸" and "尿酸历史", driver.page_source)
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left")
    sleep(2)


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
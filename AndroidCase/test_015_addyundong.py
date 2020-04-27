import unittest
from time import sleep
from util.driver import Driver
from util.swipe import huadong
from util.isElement import iselement


class addyundong(unittest.TestCase):
#增加运动记录
  def setUp(self):
    self.driver = Driver.DRIVER

  def test_addyundong(self):
    driver = self.driver
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[3]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='运动']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='上传运动情况']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='有'][1]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='无'][2]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='散步']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='<30分钟']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='微微出汗']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='上传']").click()
    sleep(6)
    self.assertIn("规律运动"and"微微出汗",driver.page_source)
    driver.find_element_by_id("cn.xinzhili.core:id/iv_title_back")
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
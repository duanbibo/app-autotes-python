import unittest
from time import sleep
from util.driver import Driver
from util.swipe import huadong
from util.isElement import iselement


class addxuetang(unittest.TestCase):
#增加血糖
  def setUp(self):
    self.driver = Driver.DRIVER

  def test_addxuetang(self):
    driver = self.driver
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[3]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='血压']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='血糖']").click()
    sleep(1)
    driver.find_element_by_xpath("//*[@text='手动上传']").click()
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/tv_tab_before_breakfast").click()
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/et_sugar_measure").clear()
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/et_sugar_measure").send_keys("6.1")
    sleep(2)
    kongfuxuetang = driver.find_element_by_id("cn.xinzhili.core:id/et_sugar_measure").text
    sleep(2)
    driver.find_element_by_xpath("//*[@text='保存']").click()
    sleep(5)
    self.assertIn(kongfuxuetang,driver.page_source)
    exit = iselement()
    quxiantu=exit.findelementid("cn.xinzhili.core:id/line_view_sugar")
    sleep(2)
    self.assertEqual(quxiantu,True)
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/iv_title_back").click()

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
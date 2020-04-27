import unittest
from time import sleep
from util.driver import Driver
from util.swipe import huadong
from util.isElement import iselement

class delyao(unittest.TestCase):
#提交血压
  def setUp(self):
    self.driver = Driver.DRIVER

  def test_xueya(self):
    driver = self.driver
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[3]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='血压']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='手动上传']").click()
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/et_pressure_measure_high").clear()
    sleep(1)
    driver.find_element_by_id("cn.xinzhili.core:id/et_pressure_measure_high").send_keys("151")
    sleep(1)
    driver.find_element_by_id("cn.xinzhili.core:id/et_pressure_measure_low").clear()
    sleep(1)
    driver.find_element_by_id("cn.xinzhili.core:id/et_pressure_measure_low").send_keys("91")
    sleep(1)
    driver.find_element_by_id("cn.xinzhili.core:id/et_heart_rate").clear()
    sleep(1)
    driver.find_element_by_id("cn.xinzhili.core:id/et_heart_rate").send_keys("91")
    sleep(1)
    gaoya= driver.find_element_by_id("cn.xinzhili.core:id/et_pressure_measure_high").text
    diya= driver.find_element_by_id("cn.xinzhili.core:id/et_pressure_measure_low").text
    xinlv= driver.find_element_by_id("cn.xinzhili.core:id/et_heart_rate").text
    driver.find_element_by_xpath("//*[@text='保存']").click()
    sleep(5)
    self.assertIn(gaoya and diya and xinlv ,driver.page_source)
    sleep(1)

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
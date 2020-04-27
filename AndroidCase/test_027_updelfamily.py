import unittest
from time import sleep
from util.driver import Driver
from util.isElement import iselement
from util.swipe import huadong
class Login(unittest.TestCase):
#修改删除我的亲友
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_updelqinyou(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[4]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='我的亲友']").click()
    sleep(3)
    hd = huadong()
    for i in range(0,2):
      if "自动家属" in driver.page_source:
        driver.find_element_by_id("cn.xinzhili.core:id/iv_relative_edit").click()
        sleep(1)
        driver.find_element_by_xpath("//*[@text='自动家属']").clear()
        sleep(1)
        driver.find_element_by_xpath("//*[@text='未填写']").send_keys("修改后")
        sleep(1)
        driver.find_element_by_xpath("//*[@text='13818899999']").clear()
        sleep(1)
        driver.find_element_by_xpath("//*[@text='必填项']").send_keys("13776666666")
        sleep(1)
        driver.find_element_by_xpath("//*[@text='配偶']").click()
        sleep(1)
        driver.find_element_by_xpath("//*[@text='保存']").click()
        self.assertIn("13776666666", driver.page_source)
        self.assertIn("修改后", driver.page_source)
        sleep(2)
        driver.find_element_by_id("cn.xinzhili.core:id/iv_relative_delete").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='确定']").click()
        sleep(2)
        self.assertNotIn("13776666666", driver.page_source)
        self.assertNotIn("修改后", driver.page_source)
        break
    else:
       hd.swipLeft(2000)


  def tearDown(self):
    self.driver = Driver.DRIVER
    exit=iselement()
    back=exit.findelementid("cn.xinzhili.core:id/iv_title_back")
    back2=exit.findelementid("cn.xinzhili.core:id/iv_title_left")
    if back is True:
        self.driver.find_element_by_id("cn.xinzhili.core:id/iv_title_back").click()
    else:
        sleep(2)
    if back2 is True:
        self.driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left").click()
    else:
        sleep(2)

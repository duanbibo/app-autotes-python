import unittest
from time import sleep
from util.driver import Driver
from util.isElement import iselement

class Login(unittest.TestCase):
#陪诊服务-3.5.5隐藏
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_peizhen(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[4]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='陪诊服务']").click()
    sleep(3)
    driver.find_element_by_xpath("//*[@text='门诊陪诊']").click()
    sleep(10)
    aaa=driver.contexts
    driver.switch_to.context("WEBVIEW_cn.xinzhili.core")
    sleep(3)
    self.assertIn("推荐医院",driver.page_source)
    sleep(3)
    driver.switch_to.context("NATIVE_APP")
    sleep(2)
    driver.find_element_by_xpath("//*[@text='关闭']").click()
    sleep(3)
    driver.find_element_by_xpath("//*[@text='护士上门']").click()
    sleep(10)
    driver.switch_to.context("WEBVIEW_cn.xinzhili.core")
    sleep(3)
    self.assertIn("静脉采血", driver.page_source)
    sleep(3)
    driver.switch_to.context("NATIVE_APP")
    sleep(2)
    driver.find_element_by_xpath("//*[@text='关闭']").click()
    sleep(2)

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

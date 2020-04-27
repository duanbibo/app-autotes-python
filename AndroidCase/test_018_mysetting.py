
import unittest
from time import sleep
from util.driver import Driver
from util.isElement import iselement

class Login(unittest.TestCase):
#设置里的设备管理，客服，设置
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_mysetting(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[4]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='设备管理']").click()
    sleep(2)
    if "解除绑定" in driver.page_source:
        driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left").click()
        sleep(2)
    else:
        driver.find_element_by_xpath("//*[@text='扫码绑定']").click()
        sleep(2)
        if "允许" in driver.page_source:
          driver.find_element_by_xpath("//*[@text='允许']").click()
          sleep(2)
          self.assertIn("扫一扫", driver.page_source)
          for back in range(0,2):
            driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left").click()
            sleep(2)
    driver.find_element_by_xpath("//*[@text='客服']").click()
    sleep(1)
    self.assertIn("68005697", driver.page_source)
    sleep(1)
    self.assertIn("68005697", driver.page_source)
    driver.find_element_by_xpath("//*[@text='取消']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='设置']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='重置密码']").click()
    sleep(1)
    self.assertIn("确认新密码", driver.page_source)
    sleep(1)
    self.assertIn("确认新密码", driver.page_source)
    driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='关于我们']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='服务热线:010-68005697']").click()
    sleep(1)
    self.assertIn("68005697", driver.page_source)
    driver.find_element_by_xpath("//*[@text='取消']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='使用条款和隐私协议']").click()
    sleep(6)
    self.assertIn("用户在注册账号前", driver.page_source)
    driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left").click()
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left").click()
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
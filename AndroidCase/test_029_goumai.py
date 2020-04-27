import unittest
from time import sleep
from util.driver import Driver
from util.isElement import iselement
from util.swipe import huadong
class Login(unittest.TestCase):
#购买服务
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_goumaifuwu(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[4]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='购买服务']").click()
    sleep(3)
    driver.find_element_by_xpath("//*[@text='确认支付']").click()
    sleep(3)
    driver.find_element_by_xpath("//*[@text='确定']").click()
    sleep(5)
    self.assertIn("登录微信",driver.page_source)
    driver.find_element_by_id("com.tencent.mm:id/m1").click()
    sleep(3)
    driver.find_element_by_xpath("//*[@text='确认支付']").click()
    sleep(3)
    driver.find_element_by_xpath("//*[@text='支付宝']").click()
    sleep(3)
    driver.find_element_by_xpath("//*[@text='确定']").click()
    sleep(5)
    self.assertIn("输入手机号",driver.page_source)
    sleep(3)
    driver.press_keycode(4)
    sleep(3)
    self.assertIn("购买服务", driver.page_source)
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

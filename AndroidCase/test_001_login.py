
import unittest
from time import sleep
from util.driver import Driver


class Login(unittest.TestCase):

  def setUp(self):
    self.driver = Driver.DRIVER


  def test_login(self):
    driver = self.driver
    sleep(2)
    if "拒绝" in driver.page_source:
      driver.switch_to.alert.accept()
      sleep(3)
    driver.find_element_by_id("cn.xinzhili.core:id/tv_user_login").click()
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/et_telephone_content").send_keys("15600576351")
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/et_pwd_content").send_keys("111111")
    sleep(1)
    driver.find_element_by_xpath("//*[@text='登录']").click()
    sleep(5)
    if "允许" in driver.page_source:
      driver.find_element_by_xpath("//*[@text='允许']").click()
      sleep(2)
    self.assertIn("对话", driver.page_source)

  def tearDown(self):
    pass


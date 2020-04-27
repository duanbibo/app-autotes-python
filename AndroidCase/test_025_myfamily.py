import unittest
from time import sleep
from util.driver import Driver
from util.isElement import iselement
from util.swipe import huadong
class Login(unittest.TestCase):
#我的亲友
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_peizhen(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[4]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='我的亲友']").click()
    sleep(3)
    driver.find_element_by_xpath("//*[@text='添加']").click()
    sleep(2)
    if "头像" not in driver.page_source:
        driver.find_element_by_id("cn.xinzhili.core:id/iv_relative_delete").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='确定']").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='添加']").click()
    driver.find_element_by_xpath("//*[@text='头像']").click()
    sleep(1)
    driver.find_element_by_xpath("//*[@text='拍照']").click()
    if "允许" in driver.page_source:
      driver.find_element_by_xpath("//*[@text='允许']").click()
    driver.find_element_by_id("com.android.camera:id/v9_shutter_button_internal").click()
    sleep(4)
    driver.find_element_by_id("com.android.camera:id/inten_done_apply").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='确定']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='未填写']").send_keys("自动家属")
    sleep(1)
    driver.find_element_by_xpath("//*[@text='必填项']").send_keys("13818899999")
    sleep(1)
    driver.find_element_by_xpath("//*[@text='子女']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='出生日期']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='确定']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='保存']").click()
    sleep(2)
    hd = huadong()
    for hua in range(0,3):
      if "自动家属" in driver.page_source:
          self.assertIn("自动家属",driver.page_source)
          sleep(2)
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

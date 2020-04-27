import unittest
from time import sleep
from util.driver import Driver
from util.isElement import iselement

class Login(unittest.TestCase):
#我的病历
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_mybingli(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[4]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='我的病历']").click()
    sleep(3)
    self.assertIn("腰围"and"我的单据", driver.page_source)
    sleep(2)
    driver.find_element_by_xpath("//*[@text='化验检查']").click()
    sleep(2)
    self.assertIn("血常规", driver.page_source)
    sleep(2)
    driver.find_element_by_xpath("//*[@text='检查单']").click()
    sleep(2)
    self.assertIn("超声", driver.page_source)
    sleep(1)
    driver.find_element_by_xpath("//*[@text='我的图片']").click()
    sleep(3)
    ass=["待审核","合格","暂无上传单据"]
    if ass[0] in driver.page_source:
         self.assertIn("待审核", driver.page_source)
    elif ass[1] in driver.page_source:
         self.assertIn("合格", driver.page_source)
    else:
         self.assertIn("暂无上传单据", driver.page_source)
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/tv_edit").click()
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/tv_cancel").click()
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

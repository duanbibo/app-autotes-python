import unittest
from time import sleep
from util.driver import Driver
from util.isElement import iselement
from util.swipe import huadong
from util.image import Appium_Extend

class Login(unittest.TestCase):
#修改我的亲友开关
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_peizhen(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[4]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='我的亲友']").click()
    sleep(3)
    if "自动家属" not in driver.page_source:
        for i in range(0,2):
            hd = huadong()
            hd.swipLeft(2000)
    if "医生主动服药计划" not in driver.page_source:
        for h in range(0,3):
           hd.swipeUp(2000)
    element=driver.find_element_by_id("cn.xinzhili.core:id/sw_doctor_advice_switch")
    ima = Appium_Extend()
    linshi="/Users/yangxiaochen/PycharmProjects/app-autotest/linshi/qinyou.png"
    filepath="/Users/yangxiaochen/PycharmProjects/app-autotest/testimage/kgopen.png"
    ima.get_screenshot_by_element(linshi,filepath,element)
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/sw_doctor_advice_switch").click()
    sleep(2)
    ele2=driver.find_element_by_id("cn.xinzhili.core:id/sw_doctor_advice_switch")
    linshi2 = "/Users/yangxiaochen/PycharmProjects/app-autotest/linshi/qinyou2.png"
    filepath2 = "/Users/yangxiaochen/PycharmProjects/app-autotest/testimage/kgdown.png"
    ima.get_screenshot_by_element(linshi2, filepath2, ele2)
    sleep(2)
    jieguo=ima.same_as(filepath,filepath2)
    self.assertEqual(jieguo,False)

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

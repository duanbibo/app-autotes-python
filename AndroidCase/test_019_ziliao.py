from util.image import Appium_Extend
import unittest
from time import sleep
from util.driver import Driver
from util.isElement import iselement

class Login(unittest.TestCase):
#设置里修改个人资料
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_ziliao(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[4]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='本人识别码:']").click()
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/civ_user_portrait").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='拍照']").click()
    sleep(2)
    driver.find_element_by_id("com.huawei.camera:id/shutter_button").click()
    sleep(4)
    driver.find_element_by_id("com.huawei.camera:id/done_button").click()
    sleep(2)
    driver.find_element_by_id("com.android.gallery3d:id/head_select_right").click()
    sleep(1)
    self.assertIn("上传成功", driver.page_source)
    sleep(1)
    driver.find_element_by_id("cn.xinzhili.core:id/et_user_name").clear()
    sleep(1)
    driver.find_element_by_id("cn.xinzhili.core:id/et_user_name").send_keys("自动化test")
    sleep(2)
    driver.find_element_by_xpath("//*[@text='所在地区']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='上海']").click()
    sleep(1)
    driver.find_element_by_xpath("//*[@text='上海市']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='徐汇区']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='确定']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='详细地址']").click()
    sleep(2)
    driver.find_element_by_id("cn.xinzhili.core:id/detail_addr").clear()
    driver.find_element_by_id("cn.xinzhili.core:id/detail_addr").send_keys("自动化测试地址")
    sleep(2)
    driver.find_element_by_xpath("//*[@text='保存']").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='保存']").click()
    sleep(5)
    driver.find_element_by_xpath("//*[@text='本人识别码:']").click()
    sleep(1)
    self.assertIn("自动化test"and"自动化测试地址"and"徐汇", driver.page_source)
    sleep(1)
    driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left").click()
    sleep(1)
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/rl_user_qr_code']/android.widget.ImageView").click()
    ima=Appium_Extend()
    elemment=driver.find_element_by_id("cn.xinzhili.core:id/iv_user_qr_code")
    ima.get_screenshot_by_element("/Users/yangxiaochen/PycharmProjects/app-autotest/linshi/ewmlinshi.png","/Users/yangxiaochen/PycharmProjects/app-autotest/testimage/ewm2.png",elemment)
    duibijieguo=ima.same_as("/Users/yangxiaochen/PycharmProjects/app-autotest/testimage/ewm.png","/Users/yangxiaochen/PycharmProjects/app-autotest/testimage/ewm2.png")
    self.assertEqual(duibijieguo,True)



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

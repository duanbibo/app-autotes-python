import unittest
from time import sleep
from util.driver import Driver
from util.isElement import iselement


class Login(unittest.TestCase):
    # 视频语音
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_shipinyuyin(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_xpath(
            "//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[4]").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='视频语音']").click()
        sleep(2)
        driver.find_element_by_id("cn.xinzhili.core:id/tv_video").click()
        sleep(2)
        self.assertIn("确定", driver.page_source)
        driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tv_afternoon'][1]").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='确定']").click()
        sleep(2)
        self.assertIn("微信支付", driver.page_source)
        driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left").click()
        sleep(2)
        driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left").click()
        sleep(3)
        driver.find_element_by_id("cn.xinzhili.core:id/iv_closed").click()
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

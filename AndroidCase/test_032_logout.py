import unittest
from time import sleep
from util.driver import Driver
from util.isElement import iselement


class Login(unittest.TestCase):
    # 视频语音
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_menzhen(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_xpath(
            "//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[4]").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='设置']").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='退出登录']").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='确定']").click()
        sleep(3)
        self.assertIn("创建账号",driver.page_source)
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

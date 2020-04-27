import unittest
from time import sleep
from util.driver import Driver
from util.isElement import iselement


class Login(unittest.TestCase):
    # 我的积分
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_mydingdan(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_xpath(
            "//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[4]").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='我的积分']").click()
        sleep(3)
        jifen=driver.find_element_by_id("cn.xinzhili.core:id/tv_credit_score").text
        self.assertTrue(int(jifen)>=0)
        self.assertIn("当前兑换活动", driver.page_source)
        self.assertIn("兑换历史", driver.page_source)
        self.assertIn("积分规则", driver.page_source)
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

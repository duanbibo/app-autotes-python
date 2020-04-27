import unittest
from time import sleep
from util.driver import Driver
from util.isElement import iselement


class Login(unittest.TestCase):
    # 我的订单
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_mydingdan(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_xpath(
            "//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[4]").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='我的订单']").click()
        sleep(3)
        self.assertIn("订单编号", driver.page_source)
        driver.find_element_by_xpath("//*[@text='未完成']").click()
        sleep(2)
        if "进行中" in driver.page_source:
           self.assertIn("进行中", driver.page_source)
        elif "待支付" in driver.page_source:
           self.assertIn("待支付", driver.page_source)
        else:
           self.assertEqual(1,2)
        sleep(3)
        driver.find_element_by_xpath("//*[@text='已完成']").click()
        sleep(3)
        self.assertIn("已取消", driver.page_source)
        sleep(2)
        driver.find_element_by_xpath("//*[@text='退款']").click()
        sleep(2)
        self.assertIn("退款成功", driver.page_source)

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

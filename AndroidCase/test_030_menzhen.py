import unittest
from time import sleep
from util.driver import Driver
from util.isElement import iselement


class Login(unittest.TestCase):
    # 门诊就诊
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_menzhen(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_xpath(
            "//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[4]").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='门诊就诊']").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='预约就诊(门诊)']").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='我的签约医生']").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='上午']").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='确定']").click()
        sleep(2)
        self.assertIn("预约中", driver.page_source)
        driver.find_element_by_xpath("//*[@text='取消就诊']").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='确定取消']").click()
        sleep(2)
        self.assertNotIn("确定取消",driver.page_source)
        driver.find_element_by_xpath("//*[@text='历史']").click()
        sleep(5)
        self.assertIn("已取消", driver.page_source)
        sleep(3)
        driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left").click()
        sleep(3)

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

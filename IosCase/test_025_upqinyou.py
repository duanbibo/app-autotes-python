from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver
from util.swipe import huadong


class Case(unittest.TestCase):
    # 修改+删除亲友
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_upqinyou(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_accessibility_id("我的").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='我的亲友']").click()
        sleep(2)
        aaa = huadong()
        if "自动化测试" not in driver.page_source:
            for h in range(0, 2):
                aaa.swipLeft(2000)
                sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeSwitch[@name='短信通知']").click()
        value=driver.find_element_by_xpath("//XCUIElementTypeSwitch[@name='短信通知']").text
        self.assertEqual(value,"0")
        for h in range(0,3):
            aaa.swipeUp(2000)
            sleep(1)
        driver.find_element_by_xpath("//XCUIElementTypeSwitch[@name='医生主动医嘱, 医生给患者主动发送医嘱']").click()
        value=driver.find_element_by_xpath("//XCUIElementTypeSwitch[@name='医生主动医嘱, 医生给患者主动发送医嘱']").text
        self.assertEqual(value, "0")
        for h in range(0,3):
            aaa.swipeDown(2000)
            sleep(1)
        driver.find_element_by_accessibility_id("relative edit").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField").clear()
        sleep(1)
        driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeTextField").send_keys("修改")
        sleep(1)
        driver.find_element_by_xpath("//*[normalize-space(@value)='15666111111']").clear()
        sleep(1)
        driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeTextField").send_keys("15666111112")
        sleep(1)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='子女']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='保存']").click()
        sleep(2)
        self.assertIn("修改", driver.page_source)
        self.assertIn("15666111112",driver.page_source)
        sleep(1)
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='del']").click()
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='删除']").click()
        sleep(2)
        self.assertNotIn("修改测试",driver.page_source)
        sleep(2)

    def tearDown(self):
        if "back" in self.driver.page_source:
            self.driver.find_element_by_accessibility_id("back").click()
        else:
            sleep(2)



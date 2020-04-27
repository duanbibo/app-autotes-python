import unittest
from time import sleep
from util.driver import Driver
from util.image import Appium_Extend

class Case(unittest.TestCase):
    # 患者二维码和id
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_erweima(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_accessibility_id("我的").click()
        sleep(2)
        self.assertIn("本人识别码: 10000294",driver.page_source)
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='mine arCode']").click()
        sleep(2)
        self.assertIn("患者ID:10000294",driver.page_source)
        sleep(2)
        element=driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage[2]")
        im=Appium_Extend()
        im.get_screenshot_by_element("/Users/yangxiaochen/PycharmProjects/app-autotest/linshi/ewmlinshi.png",
                                      "/Users/yangxiaochen/PycharmProjects/app-autotest/testimage/iosewm2.png", element)
        jieguo=im.same_as("/Users/yangxiaochen/PycharmProjects/app-autotest/testimage/iosewm.png","/Users/yangxiaochen/PycharmProjects/app-autotest/testimage/iosewm2.png",)
        self.assertEqual(jieguo,True)
        sleep(1)

    def tearDown(self):
        if "back" in self.driver.page_source:
            self.driver.find_element_by_accessibility_id("back").click()
        else:
            sleep(2)



import unittest
from time import sleep
from util.driver import Driver
from util.image import Appium_Extend

class Case(unittest.TestCase):
    # 进入我的医生，如果没绑定则绑定，绑定了则解绑重新绑
    def setUp(self):
        self.driver = Driver.DRIVER

    def test_bind(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_accessibility_id("我的").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='我的医生']").click()
        sleep(3)
        if "解约医生" in driver.page_source:
            driver.find_element_by_xpath("//XCUIElementTypeButton[@name='解约医生']").click()
            sleep(2)
            driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='直接解约']").click()
            sleep(3)
        self.assertIn("智能医生",driver.page_source)
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='back']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='mine scan']").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeButton[@name='输入医生ID']").click()
        sleep(2)
        id=["1","0","0","4","6","2"]
        for i in range(1, 7):
            for ids in id:
                driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='请输入医生识别码关联医生']/following-sibling::XCUIElementTypeOther/XCUIElementTypeStaticText[{0}]".format(i)).send_keys(ids)
                i+=1
                sleep(2)
            break
        sleep(1)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='确认关联']").click()
        sleep(1)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='电饭锅']").click()
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='选中']").click()
        sleep(1)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='免费试用']").click()
        driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton/XCUIElementTypeStaticText").click()
        sleep(2)
        driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='我的医生']").click()
        sleep(3)
        self.assertIn("电饭锅",driver.page_source)
        sleep(2)

    def tearDown(self):
        for ba in range(0,2):
            if "back" in self.driver.page_source:
                self.driver.find_element_by_accessibility_id("back").click()
            else:
                sleep(2)



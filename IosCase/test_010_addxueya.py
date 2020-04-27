from util.swipe import huadong
import unittest
from time import sleep
from util.driver import Driver

class Case(unittest.TestCase):
 #添加血压
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_addxueya(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_accessibility_id("达标").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='用药达标']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='手动上传']").click()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField").clear()
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField").send_keys("131")
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeTextField").clear()
    sleep(1)
    driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeTextField").send_keys("61")
    sleep(1)
    driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTextField").clear()
    sleep(1)
    driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTextField").send_keys("71")
    sleep(2)
    driver.find_element_by_accessibility_id("请左右滑动调整您的数据").click()
    sleep(2)
    gaoya=driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextField").text
    diya=driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeTextField").text
    xinlv=driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='心之力']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeTextField").text
    sleep(2)
    driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='保存']").click()
    sleep(2)
    xueya=[gaoya,diya,xinlv]
    for i in xueya:
        self.assertIn("{0}".format(i),driver.page_source)
    html=driver.page_source
    count={
        "diyacount" : html.count(diya),
        "gaoyacount" : html.count(gaoya),
        "xinlvcount" : html.count(xinlv)
    }
    print(count)
    for a in count.values():
       self.assertTrue(a>=6)



  def tearDown(self):
    if "back" in self.driver.page_source:
      self.driver.find_element_by_accessibility_id("back").click()
    else:
      sleep(2)



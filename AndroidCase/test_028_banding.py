import unittest
from time import sleep
from util.driver import Driver
from util.isElement import iselement
from util.swipe import huadong
class Login(unittest.TestCase):
#绑定医生
  def setUp(self):
    self.driver = Driver.DRIVER


  def test_bdjiebang(self):
    driver = self.driver
    sleep(2)
    driver.find_element_by_xpath("//*[@resource-id='cn.xinzhili.core:id/tl_home_tabs']/android.widget.LinearLayout[4]").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@text='我的医生']").click()
    sleep(14)
    if "解约医生" not in driver.page_source:  #判断当前绑定的是智能医生时就直接绑定医生，否则就先解绑再绑定
        driver.find_element_by_id("cn.xinzhili.core:id/iv_title_left").click()
        sleep(2)
        driver.find_element_by_id("cn.xinzhili.core:id/rl_user_scan").click()
        sleep(2)
        if "允许" in driver.page_source:
            driver.find_element_by_xpath("//*[@text='允许']").click()
            sleep(2)
        driver.find_element_by_id("cn.xinzhili.core:id/iv_input_doctor_id").click()
        sleep(2)
        id=["1","0","0","4","6","2"]
        for i in range (0,6):
            for ids in id:
               driver.find_element_by_xpath("//*[@class='android.widget.EditText'][@index='{0}']".format(i)).send_keys(ids)
               i = i + 1
               sleep(2)
            break
        driver.find_element_by_xpath("//*[@text='确认关联']").click()
        sleep(2)
        self.assertIn("电饭锅+上级医生",driver.page_source)
        driver.find_element_by_xpath("//*[@text='电饭锅']").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='选中']").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='免费试用']").click()
        sleep(2)
        driver.find_element_by_id("cn.xinzhili.core:id/tv_pay_confirm").click()
        sleep(5)
        driver.find_element_by_xpath("//*[@text='我的医生']").click()
        sleep(5)
        self.assertIn("电饭锅", driver.page_source)
        sleep(2)
    else:
        driver.find_element_by_xpath("//*[@text='解约医生 ']").click()
        sleep(1)
        driver.find_element_by_xpath("//*[@text='直接解约']").click()
        sleep(1)
        driver.find_element_by_id("cn.xinzhili.core:id/rl_user_scan").click()
        sleep(2)
        driver.find_element_by_id("cn.xinzhili.core:id/iv_input_doctor_id").click()
        sleep(2)
        id = [1, 0, 0, 4, 6, 2]
        for i in range (0,6):
            for ids in id:
               driver.find_element_by_xpath("//*[@class='android.widget.EditText'][@index='{0}']".format(i)).send_keys(ids)
               i = i + 1
               sleep(2)
            break
        driver.find_element_by_xpath("//*[@text='确认关联']").click()
        sleep(2)
        self.assertIn("电饭锅+上级医生", driver.page_source)
        driver.find_element_by_xpath("//*[@text='电饭锅']").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='选中']").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@text='免费试用']").click()
        sleep(2)
        driver.find_element_by_id("cn.xinzhili.core:id/tv_pay_confirm").click()
        sleep(5)
        driver.find_element_by_xpath("//*[@text='我的医生']").click()
        sleep(5)
        self.assertIn("电饭锅", driver.page_source)
        sleep(2)

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

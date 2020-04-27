from util.driver import Driver
#判断一个页面是否存在某一个元素，存在就true，不存在就false
class iselement(object):
    def __init__(self):
        self.driver = Driver.DRIVER

    def findelementxpath(self,value):
        try:
          self.driver.find_element_by_xpath(value)
          return True
        except Exception as error:
          return  False

    def findelementid(self, value):
        try:
            self.driver.find_element_by_id(value)
            return True
        except Exception as error:
            return False
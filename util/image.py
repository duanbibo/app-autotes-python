import os
from util.driver import Driver
from PIL import ImageChops

from PIL import Image
#一个图片对比的类，实现截图后保存与用例中的截图做对比
class Appium_Extend(object):
    def __init__(self):
        self.driver = Driver.DRIVER

    def get_screenshot_by_element(self,linshi,filepath,element):
        # 先截取整个屏幕，存储至临时文件夹下
        self.driver.get_screenshot_as_file(linshi)

        # 获取元素bounds
        location = element.location
        size = element.size
        box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])

        # 截取图片
        image = Image.open(linshi)
        newImage = image.crop(box)
        newImage.save(filepath)

        return self

    def same_as(self,one,two):
        image1 = Image.open(one)
        image2 = Image.open(two)
        try:
           diff = ImageChops.difference(image1, image2)
           if diff.getbbox() is None:
               return True
           else:
               return False
        except Exception as error:
           print("操作失败")


from util.driver import Driver
#写一个滑动屏幕的类，里面具体实现了上滑，下滑，左滑，右滑的方法
class huadong(object):
    def __init__(self):
        self.driver= Driver.DRIVER

    #获得机器屏幕大小x, y
    def getSize(self):
        dr = self.driver
        size=dr.get_window_size()
        x = size['width']
        y = size['height']
        return (x, y)


    # 屏幕向上滑动
    def swipeUp(self,t):
        dr = self.driver
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.35)  # 终点y坐标
        dr.swipe(x1, y1, x1, y2, t)


    # 屏幕向下滑动
    def swipeDown(self,t):
        dr = self.driver
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.5)  # 起始y坐标
        y2 = int(l[1] * 0.8)  # 终点y坐标
        dr.swipe(x1, y1, x1, y2, t)


    # 屏幕向左滑动
    def swipLeft(self,t):
        dr = self.driver
        l = self.getSize()
        x1 = int(l[0] * 0.8)
        y1 = int(l[1] * 0.2)
        x2 = int(l[0] * 0.05)
        dr.swipe(x1, y1, x2, y1, t)


    # 屏幕向右滑动
    def swipRight(self,t):
        dr = self.driver
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        dr.swipe(x1, y1, x2, y1, t)
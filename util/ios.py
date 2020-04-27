#封装ios的关键参数，用来给driver实例化时调用

class Ios(object):
    desired_caps = {}
    desired_caps['platformName'] = 'ios'
    desired_caps['automationName'] = "XCuiTest"
    desired_caps['deviceName'] = 'iPhone'
    desired_caps['udid'] = "078b1851c39613ee28ae0f430b901d9efd58e742"
    desired_caps['platformVersion'] = "13.1.3"
    desired_caps['bundleId'] = 'cn.xinzhili.patient.appstore'

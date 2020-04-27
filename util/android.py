#封装安卓的关键参数，用来给driver实例化时调用
class Android(object):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = "8.1"
    desired_caps['deviceName'] = 'device'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = "true"
    desired_caps['udid'] = '55bd495'
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['autoGrantPermissions'] = True
    desired_caps['appPackage'] = 'cn.xinzhili.core'
    desired_caps['appActivity'] = 'cn.xinzhili.core.ui.launch.MainActivity'
    desired_caps['noReset'] = False


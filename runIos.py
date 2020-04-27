# coding=UTF-8
from appium import webdriver
import unittest
import HTMLTestRunner
from util.driver import Driver
import smtplib
from email.mime.text import MIMEText  # MIMRText()定义邮件正文
from email.mime.multipart import MIMEMultipart
from util.ios import Ios
from util.appiumserver import start_appium, stop_appium
#ios的执行文件
start_appium() #启动appium服务
Driver.DRIVER = webdriver.Remote('http://localhost:4723/wd/hub', Ios.desired_caps)  #实例化一个driver
Driver.DRIVER.implicitly_wait(5)  # 设置隐式等待5s

# 设置用例路径
case_path = "/Users/yangxiaochen/PycharmProjects/app-autotest/IosCase"
discover = unittest.defaultTestLoader.discover(case_path, pattern="ttest_*.py", top_level_dir=None)

# 执行用例生成报告
runner = unittest.TextTestRunner()
reportpath = "/Users/yangxiaochen/PycharmProjects/app-autotest/result.html"

##定义报告
fp = open(reportpath, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'ios自动化测试报告', description=u'用例执行情况：')
runner.run(discover)
fp.close()


def send_mail():
    # 发送邮件的服务器
    smtpserver = 'smtp.qq.com'

    # 发送邮件用户和密码
    user = "645879744@qq.com"
    password = 'uvwrtjqfbsdibfci'

    # 发送者
    sender = "645879744@qq.com"

    # 接收者
    receiver = ["yangxiaochen@xinzhili.cn", "duanbibo@xinzhili.cn", "yinjie@xinzhili.cn"]

    # 邮件主题
    subject = "接口自动化测试"

    # 发送附件
    sendfile = open("/Users/yangxiaochen/PycharmProjects/interface/result.html", "r", encoding="utf-8").read()

    att = MIMEText(sendfile, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = "attachment;filename = 'result.html'"

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()


# send_mail()
# 测试结束，退出
Driver.DRIVER.quit()
stop_appium() #停止appium服务


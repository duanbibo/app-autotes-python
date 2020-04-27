import os
import time
#停止和启动本地的appium服务
def stop_appium(post_num=4723):
        '''关闭appium服务'''
        p = os.popen(f'lsof -i tcp:{post_num}')
        p0 = p.read()
        if p0.strip() != '':
            p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
            os.popen(f'kill {p1}')  # 结束进程
            print("appium end")

def start_appium(post_num=4723):
        '''开启appium服务'''
        stop_appium(post_num)  # 先判断端口是否被占用，如果被占用则关闭该端口号
        # 根据系统，启动对应的服务
        cmd_dict = {
            'MAC': f'appium -a 127.0.0.1 -p {post_num} --log appium.log --local-timezone  & '
        }
        os.system(cmd_dict['MAC'])
        time.sleep(3)  # 等待启动完成
        print("appium start")
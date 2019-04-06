#!/usr/bin/python
# -*- coding:utf-8 -*-
import subprocess,time,sys
import itchat

TIME = 3                        #程序状态检测间隔（单位：秒）

class call_WeChat():
    def __init__(self,sleep_time):
        self.sleep_time = sleep_time
        self.p = None             #self.p为subprocess.Popen()的返回值，初始化为None

        self.run()                           #启动程序

        try:
            while 1:
                time.sleep(sleep_time)  #休息TIME，判断程序状态
                self.poll = self.p.poll()    #判断程序进程是否存在，None：表示程序正在运行 其他值：表示程序已退出
                if self.poll is None:
                    pass
                else:
                    print("未检测到程序运行状态，呼叫微信")
                    UserName = str(itchat.search_friends(name='DJ')[0]['UserName'])
                    itchat.send('Master, it is done now :)', toUserName=UserName)
                    break
        except KeyboardInterrupt as e:
            print("检测到CTRL+C，准备退出程序!")
#            self.p.kill()                   #检测到CTRL+C时，kill掉CMD中启动的exe或者jar程序

    def run(self):
        self.p = subprocess.Popen(['python', 'loop.py'])

itchat.auto_login()
app = call_WeChat(TIME)

#!/usr/bin/python
# -*- coding:utf-8 -*-
import subprocess,time,sys

TIME = 1                        #程序状态检测间隔（单位：秒）

for idx in range(8):
    time.sleep(TIME)
    print(idx)

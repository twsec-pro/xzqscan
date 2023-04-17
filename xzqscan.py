#coding=utf-8
#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Author: twsec
Date: 2022-04-06 15:25:00
LastEditors: twsec
LastEditTime: 2022-04-15 22:21:22
Description: 主文件
'''


import sys
import requests
from lib.core.Spider import SpiderMain
import time
sys.path.append(r'D:\code\git\xzqscan\script')
from script import sqlcheck
from script import sqlcheck2 
from script import sqlcheck3
from script import wafscan
from script import bool
from script import ttime


def main(url):
    root = url
    threadNum = 10
    #spider
    wgd = SpiderMain(root,threadNum)
    wgd.craw()




if __name__ == '__main__':
    print("1.自动爬取链接并检测\n2.单个链接检测\n3.WAF探测\n4.盲注\n")
    key=input("选择要进行的功能：")
    if(key==1):

        url=input('输入要爬取的链接：')
    
        main(url)
        print("链接已经爬取完成！")
        print("开始调用sql注入检测模块进行检测：")
        for url in open('url.txt'):
            url = url.replace('\n','')
            print(url)
            
            try:
                keys=sqlcheck.sqlcheck(url)
                if(keys==1):
                    print("模块1检测到数据库报错信息，可能存在注入！")

                
                if(keys==0):
                    print("模块1未检测到数据库报错信息，可能不存在注入！")
                    
            except:
                ##    #print("no")
                pass
            try:
                sqlcheck2.sql(url)
            except:
                ##    #print("no")
                pass 
            try:
                sqlcheck3.sqlmapapi(url)  
            except:
                ##    #print("no")
                pass     
    if(key==2):
        
            #print("输入要检测的url：")
        url=input("输入要检测的url：")
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        r=requests.get(url,headers)

        status=r.status_code
        if status == 200:
            try:
                keys=sqlcheck.sqlcheck(url)
                if(keys==1):
                    print("模块1检测到数据库报错信息，可能存在注入！")

                
                if(keys==0):
                    print("模块1未检测到数据库报错信息，可能不存在注入！")
                    
            except:
                ##    #print("no")
                pass
            try:
                sqlcheck2.sql(url)
            except:
                ##    #print("no")
                pass 
            try:
                sqlcheck3.sqlmapapi(url)  
            except:
                ##    #print("no")
                pass      
        else:
            print("当前链接不可访问，请检查！")
    if(key==3):
        url=input("输入要检测的url：")
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        r=requests.get(url,headers)

        status=r.status_code
        if status == 200:
            try:
                wafscan.scan_waf(url)
            except:
                ##    #print("no")
                pass     
        else:
            print("当前链接不可访问，请检查！")
    if(key==4):
        print("1.基于bool的盲注\n2.基于时间的的盲注\n")
        key2=input("请选择要使用的功能：")
        if(key2==1):
            url=input("输入要检测的url：")
            headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
            r=requests.get(url,headers)

            status=r.status_code
            if status == 200:
                try:
                    bool.StartSqli(url)
                except:
                ##    #print("no")
                    pass     
            else:
                print("当前链接不可访问，请检查！")
        if(key2==2):
            url=input("输入要检测的url：")
            headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
            r=requests.get(url,headers)

            status=r.status_code
            if status == 200:
                try:
                    ttime.StartSqli(url)
                except:
                ##    #print("no")
                    pass     
            else:
                print("当前链接不可访问，请检查！")

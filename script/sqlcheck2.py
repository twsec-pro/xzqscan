#coding=utf-8
#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Author: twsec
Date: 2022-04-10 10:43:56
LastEditors: twsec
LastEditTime: 2022-04-15 20:56:56
Description: 模块2
'''
import os
import sys
import requests
import time
import requests,json

def sql(url):



    url=url

    if url !=None:

        

        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        r=requests.get(url,headers)

        status=r.status_code
        if status == 200:
            url1=url+'%20and%201=1'
            url2=url+'%20and%201=2'
            url3=url+'%27%20and%20%271%27=%271'
            url4=url+'%27%20and%20%271%27=%272'
            url5=url+'%22%20and%20%221%22=%221'
            url6=url+'%22%20and%20%221%22=%222'
            url7=url+'%29%20and%20%281%29=%281%29'
            url8=url+'%29%20and%20%281%29=%282%29'
        ##print(url1)
        ##print(url2)
            key=0
            
            zhusx=requests.get(url,headers).content

            zhus=requests.get(url1,headers).content

            zhuss=requests.get(url2,headers).content
            if zhusx == zhus and zhusx !=zhuss:
                key=1
                #print('模块2检测存在SQL注入漏洞！注入类型为')
            #else:
                #pass
            zhusx=requests.get(url,headers).content

            zhus=requests.get(url3,headers).content

            zhuss=requests.get(url4,headers).content
            if zhusx == zhus and zhusx !=zhuss:
                key=2
            #else:
                #pass
            zhusx=requests.get(url,headers).content

            zhus=requests.get(url5,headers).content

            zhuss=requests.get(url6,headers).content
            if zhusx == zhus and zhusx !=zhuss:
                key=3
            #else:
                #pass
            zhusx=requests.get(url,headers).content

            zhus=requests.get(url7,headers).content

            zhuss=requests.get(url8,headers).content
            if zhusx == zhus and zhusx !=zhuss:
                key=4
            #else:
                #pass
            if(key==1):
                print("模块2检测可能存在sql注入漏洞，类型为数字型注入!\n")
            if(key==2):
                print("模块2检测可能存在sql注入漏洞，类型为字符型单引号闭合注入!\n")
            if(key==3):
                print("模块2检测可能存在sql注入漏洞，类型为字符型双引号闭合注入!\n")
            if(key==4):
                print("模块2检测可能存在sql注入漏洞，类型为字符型括号闭合注入!\n")
            if(key==0):
                print("模块2检测可能不存在sql注入漏洞！\n")
        else:
            print("当前链接不可访问，请检查！")
    else:
        print("url为空，请检查！")
#url="http://rhiq8003.ia.aqlab.cn/index.php?id=1"
#sql(url)



#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Author: twsec
Date: 2022-04-09 21:55:31
LastEditors: twsec
LastEditTime: 2022-04-10 13:29:32
Description: 模块3
'''
import time
import requests,json


# 首先：进入sqlmap目录，启动sqlmapapi，命令：python sqlmapapi.py -s


def sqlmapapi(url):

    data = {
        "url": url
    }
    headers = {
        "Content-Type": "application/json"
    }

    # 创建新任务，记录任务ID
    task_new_url = 'http://101.43.242.147:8775/task/new'
    resp = requests.get(task_new_url)
    task_id = resp.json()['taskid']
    # print(task_id)

    if 'success' in resp.content.decode('utf-8'):
        #print('sqlmapapi task create success!')
        # 设置任务ID的配置信息（扫描信息）
        task_set_url = "http://101.43.242.147:8775/option/" + task_id + "/set"
        task_set_resp = requests.post(task_set_url, data=json.dumps(data), headers=headers)
        # print(task_set_resp.json())

        if 'success' in task_set_resp.content.decode('utf-8'):
            #print('sqlmapapi task set success!')
            # 启动对应ID的扫描任务
            task_start_url = "http://101.43.242.147:8775/scan/" + task_id + "/start"
            task_start_resp = requests.post(task_start_url, data=json.dumps(data), headers=headers)
            # print(task_start_resp.json())
            if 'success' in task_start_resp.content.decode('utf-8'):
                #print('sqlmapapi task start success!')
                while 1:
                    # 获取对应ID的扫描状态
                    task_status_url = "http://101.43.242.147:8775/scan/" + task_id + "/status"
                    task_status_resp = requests.get(task_status_url)
                    # print(task_status_resp.json())
                    if 'running' in task_status_resp.content.decode('utf-8'):
                        #print('suqmapapi task scan running!-->' + url)
                        pass
                    else:
                        # print('sqlmapapi task scan end!')
                        #扫描结果查看
                        task_data_url = "http://101.43.242.147:8775/scan/" + task_id + "/data"
                        task_data_resp = requests.get(task_data_url).content.decode('utf-8')
                        datas=requests.get(url='http://101.43.242.147:8775/scan/{}/data'.format(id))
                        #print(task_data_resp)
                        #dat=datas.json()['data']
                        #print('[*]data:',dat)
                        #dat=task_data_resp.json()['data']
                        #print(dat)
                        #print(task_data_resp)
                        with open(r'result.txt','a+') as f:
                            f.write(url + '\n')
                            f.write(task_data_resp + '\n')
                            f.write('==========python sqlmapapi by Serena==========' + '\n')
                        #如果结束删除ID
                        task_delete_url = "http://101.43.242.147:8775/task/" + task_id + "/delete"
                        task_delete_resp = requests.get(task_delete_url)
                        if 'success' in task_delete_resp.content.decode('utf-8'):
                            print('sqlmapapi检测结果已保存文件result.txt中!')
                        break
                    #time.sleep(3)


#if __name__ == '__main__':
#    for url in open('url.txt'):
#        url = url.replace('\n','')
        # print(url)
#       sqlmapapi(url)
#url="http://4842eeb2d36a600767924436d9d9a4a3.n2.vsgo.cloud:19810/sqlilabs/Less-8/?id=1"
#sqlmapapi(url)

#coding=utf-8
#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Author: twsec
Date: 2022-04-06 15:25:00
LastEditors: twsec
LastEditTime: 2022-04-15 22:57:15
Description: 爬虫
'''


from lib.core import Download,UrlManager
import threading
from urlparse import urljoin
from bs4 import BeautifulSoup
from script import sqlcheck

class SpiderMain(object):
    def __init__(self,root,threadNum):
        self.urls = UrlManager.UrlManager()
        self.download = Download.Downloader()
        self.root = root
        self.threadNum = threadNum

    def _judge(self, domain, url):
        if (url.find(domain) != -1):
            return True
        else:
            return False

    def _parse(self,page_url,content):
        if content is None:
            return
        soup = BeautifulSoup(content, 'html.parser')
        _news = self._get_new_urls(page_url,soup)
        return _news

    def _get_new_urls(self, page_url,soup):
        new_urls = set()
        links = soup.find_all('a')
        for link in links:
            new_url = link.get('href')
            new_full_url = urljoin(page_url, new_url)
            if(self._judge(self.root,new_full_url)):
                new_urls.add(new_url)
        return new_urls

    def craw(self):
        self.urls.add_new_url(self.root)
        while self.urls.has_new_url():
            _content = []
            th = []
            for i in list(range(self.threadNum)):
                #print(i)
                if self.urls.has_new_url() is False:
                    break
                new_url = self.urls.get_new_url()
                f = open("url.txt", "a")
                f.write(new_url)
                f.write('\n')
                f.close()
                ##sql check
                ##try:
                ##    if(sqlcheck.sqlcheck(new_url)):
                ##        print("url:%s sqlcheck is valueable"%new_url)
                    
                ##except:
                ##    #print("no")
                ##    pass
                print("craw:" + new_url)
                t = threading.Thread(target=self.download.download,args=(new_url,_content))
                t.start()
                th.append(t)
            for t in th:
                t.join()
            for _str in _content:
                if _str is None:
                    continue
                new_urls = self._parse(new_url,_str["html"])
                self.urls.add_new_urls(new_urls)
                
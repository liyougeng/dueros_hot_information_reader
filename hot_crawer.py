#!/usr/bin/env python
#coding:utf-8
"""
    This is a python script for 互联网热门咨询抓取简单脚本.
    Author: 
    File:   hot_crawer.py
    Tab/Space: YES
    TabSize:4
"""
import os
import sys
import json
import glob
import urllib2
from xml.etree import ElementTree as etree

def tianya_hot():
    pass

# ref: https://docs.rsshub.app/shopping.html#%E4%BC%97%E7%AD%B9%E9%A1%B9%E7%9B%AE-2
# https://rss.mifaw.com/

def baidu_hot():
    headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36",
               "referer": "https://docs.rsshub.app/social-media.html",
               "cookie": "__cfduid=dbcda5f20b2737243bc9c61cac9f9ec241566993006; _ga=GA1.2.796475881.1566993008; _gid=GA1.2.291098990.1566993008" }
    url = 'http://top.baidu.com/buzz?b=1&fr=topcategory_c12'
    url = 'https://rsshub.app/douban/movie/playing'
    url = 'https://rsshub.app/weibo/search/hot'
    url = 'https://rsshub.app/zhihu/daily'
    url = 'https://rsshub.app/zhihu/hotlist'
    request = urllib2.Request(url,headers=headers)
    try:
        response = urllib2.urlopen(request)
    except Exception as e:
        raise e
    data = response.read()
    # print(data)# .decode('gb2312')
    reddit_root = etree.fromstring(data)
    item = reddit_root.findall('channel/item')
    # print item
    reddit_feed=[]
    for entry in item:   
        #get description, url, and thumbnail
        desc = entry.findtext('title')  
        reddit_feed.append([desc])
        print(desc)
    # print(reddit_feed)

def get_web_data(url):
    '''  x  '''
    try:
        response = urllib2.urlopen(url)
    except Exception as e:
        raise e
    return response.read()

def sina_hot():
    data = get_web_data('http://sinanews.sina.cn/interface/type_of_search.d.html?callback=initFeed&keyword=%E6%98%8E%E6%98%9F&page=1&type=siftWb&size=20&newpage=0&chwm=&imei=&token=&did=&from=&oldchwm=')
    o = json.loads(data[len('initFeed('):-1])
    print(json.dumps(o))

def main():
    print("work.")

if __name__ == "__main__":
    main()
    baidu_hot()
    # sina_hot()

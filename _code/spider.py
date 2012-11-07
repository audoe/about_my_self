#!/usr/bin/env python
#coding:utf8

import re
import urllib2
import redis
import optparse
from urlparse import urlparse

from lxml.html import fromstring
global redis_server
redis_server = redis.Redis()

def push_redis(key, url):
    redis_server.sadd('list', url)

def pop_redis(key):
    return redis_server.spop('list')

def split_url(url):
    '''
    分拆url
    return {
    'head':
    'host':带端口
    'path':
    'param':参数
    'dept':path深度 
    }
    '''
    o = urlparse(url)
    return {'head':o.scheme,
            'host':o.netloc,
            'path':o.path,
            'dept':len(o.path.split('/'))-1}


def get_page(base_url, dir, key):
    '''
    url:要抓去的网页地址
    dir:网页保存的地址
    key：关键字
    result:返回的结果{'code':,'next':,'error':}
    '''
    print base_url
    try:
        response = urllib2.urlopen(base_url)
    except:
        return {'code':403, 'next':[], 'error':''}
    if response.getcode() >=200 and response.getcode() <=300:
        redis_server.sadd('history', base_url)

    page = response.read()
    html = fromstring(page)
    urls = html.xpath('//@href')
    next = []
    for url in urls:
        result = split_url(base_url)
        if url.startswith('http'):
            #合格的url，同一个host、deep合适
            next.append(url)
        if url.startswith('/'):
            next.append('%s://%s%s' % (result['head'], result['host'], url))
        if not url.startswith('javascript'):
            pass

    #编码处理 
    #values = html.xpath('//test()')
    #return result    
    print response.getcode()
    return {'code':response.getcode(), 'next':next, 'error':''}

def worker(logger, loglevel, deep, dir, redis_key, key, re_rule):
    '''
    '''
    save_dir = dir
    while True:
        print len(url_not_list)
        try:
            url = pop_redis(redis_key)
        except:
            return 

        #退出工作线程
        if url == '':
            break
        result = get_page(url, save_dir, key)
        for url in result['next']:
            split_result = split_url(url)
            if re_rule.findall(split_result['host']) and split_result['dept'] <=deep:
                push_redis('key',url)

if __name__ == '__main__':
    
    global url_not_list
    url_not_list = []
    parser = optparse.OptionParser()
    parser.add_option('-s', '--start', dest='start', help='the url where to start', metavar='START')
    parser.add_option('-d', '--dept', dest='dept', help='the level of url', metavar='DEPT')
    parser.add_option('-a', '--host', dest='host', help='the host of website', metavar="HOST")
    parser.add_option('-k', '--key', dest='key', help='the webpage you want to get', metavar='KEY')
    (options, args) = parser.parse_args()
    dir = './'
    import pdb;pdb.set_trace()
    result = get_page(options.start, dir, options.key)
    re_rule = re.compile(options.host)
    for url in result['next']:
        split_result = split_url(url)
        if re_rule.findall(split_result['host']) and split_result['dept'] <= int(options.dept):
            push_redis('key',url)
    
    worker('logger', 'logleval', int(options.dept), dir, 'redis_key', 'key', re_rule)
    



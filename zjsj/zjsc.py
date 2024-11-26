#!/usr/bin/python3
# -- coding: utf-8 --
import os
from datetime import date
from json import dumps
from requests import get, post
# -- 获取token --
# -- crontab 5 0,23 * * * python3 zjsc.py--
os.getenv('ZJSC_TOKEN')
os.environ.get('ZJSC_TOKEN')
g_token=os.environ['ZJSC_TOKEN']

def qiandao(token):
    url='https://pro.zjypwy.com/shop-api/zj-api-shop/p/score/updateUserScore'
    headers={
	'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.54(0x1800362c) NetType/4G Language/zh_CN miniProgram/wx880c4e504e1164de'
    }
    headers['Authorization']=token
    data = get(url, headers=headers)
    print(data.text);

if __name__ == "__main__":
    if g_token == "":
        exit(0)
    tokens = g_token.split("&")
    for s in tokens:
        qiandao(s)

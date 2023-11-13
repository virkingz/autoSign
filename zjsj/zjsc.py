#!/usr/bin/python3
# -- coding: utf-8 --
import os
from datetime import date
from json import dumps
from requests import get, post
# -- 获取token --
# -- crontab 5 0 * * * python3 zjsc.py--
os.getenv('ZJSC_TOKEN')
os.environ.get('ZJSC_TOKEN')
g_token=os.environ['ZJSC_TOKEN']

def qiandao(token):
    url='https://pro.zjypwy.com/shop-api/zj-api-shop/p/score/updateUserScore'
    headers={
	'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36'
    }
    headers['Authorization']=token
    data = get(url, headers=headers)
    print(data);

if __name__ == "__main__":
    if g_token == "":
        exit(0)
    tokens = g_token.split("&")
    for s in tokens:
        qiandao(s)

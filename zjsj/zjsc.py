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
    headers[Authorization]=token
    data = get(url, headers=headers).json()
    print(data);

if __name__ == "__main__":
    if g_token == "":
        exit(0)
    tokens = g_token.split("&")
    for s in tokens:
        qiandao(s)

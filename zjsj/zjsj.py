#!/usr/bin/python3
# -- coding: utf-8 --
import os
from datetime import date
from json import dumps
from requests import get, post
# -- 获取token --
# -- crontab 5 0,23 * * * --
os.getenv('ZJSJ_TOKEN')
os.environ.get('ZJSJ_TOKEN')
g_token=os.environ['ZJSJ_TOKEN']

def qiandao(token):
    tokens=token.split("@")
    param={'site':'api','r':'checkin/checkin','tenant_code':'zjsjadmin','orgcode':'zjsjadmin'}
    param['token']=tokens[0]
    param['member_id']=tokens[1]
    url='https://vip-php-platform.myscrm.cn/index.php'
    data = post(url, params=param).json()
    print(data);

if __name__ == "__main__":
    if g_token == "":
        exit(0)
    tokens = g_token.split("&")
    for s in tokens:
        qiandao(s)

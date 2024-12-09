#!/usr/bin/python3
# -- coding: utf-8 --
import os
from datetime import date
from json import dumps
from requests import get, post
# -- 获取token --
# -- crontab 5 0,23 * * * python3 zjsc.py--
os.getenv('GQBT_TOKEN')
os.environ.get('GQBT_TOKEN')
g_token=os.environ['GQBT_TOKEN']

def qiandao(token):
    tokens=token.split("@")
    headers={
	    'User-Agent':'GHA-APP-AppStore/3.1.4 (iPhone; iOS 16.6; Scale/2.00)',
      'systemVersion': '16.6',
      'version': '3.1.4',
      'os': 'ios',
      'deviceToken': 'cbf3c6b20cc975eb69516e1989b7ae5cca6fa1f20e5f2a9ce06e38ee1360a09d'
    }
    headers['X-Access-Token']=tokens[0]
    headers['customerCode']=tokens[1]
    url='https://gha.ghac.cn:8805/task/app/api/sign/save'
    data = get(url, headers=headers)
    print(data.text);

if __name__ == "__main__":
    if g_token == "":
        exit(0)
    tokens = g_token.split("&")
    for s in tokens:
        qiandao(s)

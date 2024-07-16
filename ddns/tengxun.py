#!/usr/bin/python3
# -- coding: utf-8 --
import os
import requests
import subprocess
# -- crontab 5 0,23 * * * python3 zjsj.py --
os.getenv('DDNS_DOMAIN_LIST')
os.environ.get('DDNS_DOMAIN_LIST')
s_domain_names=os.environ['DDNS_DOMAIN_LIST'].split("@")
os.getenv('DDNS_PARAMS')
os.environ.get('DDNS_PARAMS')
s_ddns_param=os.environ['DDNS_PARAMS']

class DnsPodAPI:
    """
    使用DNSPod API更新域名解析记录。
    """
    def __init__(self, api_id, api_token, domain, value):
        self.api_id = api_id
        self.api_token = api_token
        self.api_domin = domain
        self.records_id = 0
        self.domin_id = 0
        self.domain = domain
        self.value = value

    def is_domain_accessible(self, domain):
        try:
            response = subprocess.run(['ping', '-c', '1', domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return response.returncode == 0
        except OSError:
            return False  # 如果出现异常，返回 False

    def check_domin_list(self):
        for domain in s_domain_names:
            if self.is_domain_accessible(domain):
                self.api_domin = domain
            else:
                print(f"The domain {domain} is not accessible.")

    def get_domin_list(self, domain):
        try:
            url = "https://dnsapi.cn/Record.List"
            param = {}
            param['login_token'] = f'{self.api_id},{self.api_token}'
            param['domain'] = domain
            param['format'] = "json"
            data = requests.post(url, data=param).json()
            self.domin_id = data['domain']['id']
            records = data['records']
            for record in records:
                if record['name'] == self.value:
                    self.record_id = record['id']
                    break
            print(f'{self.domin_id}:{self.record_id}')
            return True
        except:
            return False

    def update_domain(self, data):
        try:
            url = "https://dnsapi.cn/Record.Modify"
            data['login_token'] = f'{self.api_id},{self.api_token}'
            data['record_id'] = data['id']
            response = requests.post(url, data=data).json()
            print("update succeed!")
        except:
            print("update Error")

    def check_need_update(self):
        self.check_domin_list()
        self.get_domin_list(self.domain)
        try:
            url = "https://dnsapi.cn/Record.Info"
            param = {}
            param['login_token'] = f'{self.api_id},{self.api_token}'
            param['domain_id'] = self.domin_id
            param['record_id'] = self.record_id
            param['format'] = "json"
            data = requests.post(url, data=param).json()
            record = data['record']
            value = record['value'].rstrip('.')
            if self.api_domin == value:
                print("Dont need update!")
            else:
                record['value']=self.api_domin
                self.update_domain(record)
        except:
            print("Error!!!")
if __name__ == "__main__":
    if s_ddns_param == "":
        exit(0)
    api = DnsPodAPI(s_ddns_param[0], s_ddns_param[1], s_ddns_param[2], s_ddns_param[3])
    api.check_need_update()

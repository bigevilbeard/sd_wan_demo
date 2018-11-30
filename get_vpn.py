#! /usr/bin/env python
from env_lab import sdwan_always
import requests
import urllib3
from requests.auth import HTTPBasicAuth
from viptela.viptela import Viptela
from tabulate import tabulate

# Silence the insecure warning due to SSL Certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    vmanage = Viptela(user=sdwan_always['username'],user_pass=sdwan_always['password'],
        vmanage_server=sdwan_always['host'],vmanage_server_port=sdwan_always['port'])
    devices = vmanage.get_ipsec_inbound('4.4.4.63')

    headers = ["Host Name", "Remote TLOC", "Local TLOC", "Remote TLOC Color", "Local TLOC Color", "Encryption"]
    table = list()

    for item in devices.data:
        tr = [item['vdevice-host-name'], item['remote-tloc-address'], item['local-tloc-address'], item['remote-tloc-color'], item['local-tloc-color'],item['negotiated-encryption-algo']]
        table.append(tr)

    print(tabulate(table, headers, tablefmt="fancy_grid"))
    # print(devices.data)



if __name__ == "__main__":
    main()

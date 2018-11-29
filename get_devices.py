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
    devices = vmanage.get_all_devices()

    headers = ["Host Name", "Device IP", "Site ID", "Host ID", "Host Type"]
    table = list()

    for item in devices.data:
        tr = [item['host-name'], item['deviceId'], item['host-name'], item['uuid'], item['device-model']]
        table.append(tr)

    print(tabulate(table, headers, tablefmt="fancy_grid"))
    # print(devices.data)
    # print(tabulate(devices.data))


if __name__ == "__main__":
    main()

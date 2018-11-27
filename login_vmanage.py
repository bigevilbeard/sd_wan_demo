#! /usr/bin/env python
from env_lab import sdwan
import requests
import json
import urllib3
from requests.auth import HTTPBasicAuth


# Silence the insecure warning due to SSL Certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
              'content-type': "application/json",
              'x-auth-token': ""
          }


def sdwan_login(host, port, username, password):
    """
    Login to vmanage
    """
    url = "https://{}:{}/j_security_check".format(host,port)

    # Make Login request and return the response body

    sess = requests.session()
    response = sess.post(url=url, data = {'j_username' : username, 'j_password' : password}, verify=False)

    # print the token
    print(response.text)
    print(response.status_code)
    # url = "https://%s:8443/dataservice/%s"%(self.vmanage_ip, mount_point)
    url = "https://{}:{}/dataservice/device".format(host,port)
    print (url)
    response = sess.get(url, verify=False)
    data = response.content
    return data

def main():
    sdwan_login(sdwan['host'],sdwan['port'],sdwan['username'],sdwan['password'])

if __name__ == "__main__":
    main()

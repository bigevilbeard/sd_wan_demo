# sd_wan_demo

All code has been tested on Cisco Devnet Always On SDWAN sandbox [HERE](https://devnetsandbox.cisco.com/RM/Diagram/Index/4fb544ad-c88c-4227-8b09-5d35aa26a63b?diagramType=Topology) and the Reservable SDWAN sandbox [HERE](https://devnetsandbox.cisco.com/RM/Diagram/Index/8a5390bf-3017-4dc2-a77b-23b6cf8b2267?diagramType=Topology) Please see the sandbox pages for credentials and reservations. This demo example is based on Python 3.6 and was tested successfully under that version.

```
python3 -m venv venv
source venv/bin/activate
python -V
Python 3.6.5
```

## Returns All Inventory Data
This section of the code will retrieve the inventory data of the vMange and return summary data of all devices in the network. The data includes SystemIP, Hostname, Version of code, UUID and interfaces and statistics. The second part of the demo presents the detailed tunnel statistics on an individual vEdge.

## Function Descriptions
This python script implements four basic functions that are described below:

`initalize_connection` - Initializes a connection to the vManage server
`get_inventory` - Get an inventory dictionary that correlates the system-ip with the hostname
`get_statistic` - Return the interface statistics for each interface in each device
`get_tunnel_statistic` - For a given vEdge, return the statistics on all the tunnels that are defined on that device

# Requirements and Prerequisites
`package_config.ini`

The code uses a file called the `package_config.ini` to house the information about the vManage and the credentials that the application uses. In the repository, there is a package_config.ini.sample that you should rename to package_config.ini. Then modify the package_config.ini to reflect the following information:

`serveraddress` - Represents the ip address of the vManage server
`username` - username of the login credentials on the vManage server
`password` - password of the login credentials on the vManage server
`systemip` - systemip of a device that will be queried for detailed tunnel information
python


There are two main requirements for external libraries (install both of these):
1. `get_devices.py` and `get_vpn.py` use the Python library for use with Viptela vManage API
2. `viptelaquery.py` uses `requests` and `configparser`

```
requests
configparser
```
```
## Installation
pip install https://github.com/bobthebutcher/viptela/archive/master.zip
pip install -r requirements
```

![sdwan](./demo.gif)

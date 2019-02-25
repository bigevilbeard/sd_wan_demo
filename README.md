[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/bigevilbeard/sd_wan_demo)
# SD-WAN Demo Code

All code has been tested on the Cisco DevNet Always On SD-WAN sandbox [HERE](https://devnetsandbox.cisco.com/RM/Diagram/Index/4fb544ad-c88c-4227-8b09-5d35aa26a63b?diagramType=Topology) and the Reservable SD-WAN sandbox [HERE](https://devnetsandbox.cisco.com/RM/Diagram/Index/8a5390bf-3017-4dc2-a77b-23b6cf8b2267?diagramType=Topology). Please see the sandbox pages for credentials and reservations. This demo example is based on Python 3.6 and was tested successfully under that version.

The Cisco SD-WAN software provides a REST API, which is a programmatic interface for controlling, configuring, and monitoring the Cisco SD-WAN devices in an overlay network. You access the REST API through the vManage web server. The API is documented on the vManage host and can be found by going to `https://{vmanage-ip-address/apidocs`. Additional API documentation can be found in the [Cisco SD-WAN Product Documentation](https://sdwan-docs.cisco.com/Product_Documentation/Command_Reference/vManage_REST_APIs).

## The requirements

```
python3 -m venv venv
source venv/bin/activate
python -V
Python 3.6.5
```
```
pip install -r requirements
git clone https://github.com/bigevilbeard/sd_wan_demo
```


## Bulk API Operations

RESTful bulk API calls allow you to issue a single RESTful API command to collect information about multiple vEdge routers in the overlay network. The information is returned in batches.

You can perform two types of bulk API operations:

`State`— These operations return status information about the Cisco SD-WAN devices, such as the number and state of OMP and BFD sessions

`Statistics` — These operations return statistics from the Cisco SD-WAN devices, such as the number of transmitted and received data packets


## Returns All Inventory Data

This section of the code will retrieve the inventory data of the vMange and return summary data of all devices in the network. The data includes SystemIP, Hostname, Version of code, UUID and interfaces and statistics. The second part of the demo presents the detailed tunnel statistics on an individual vEdge.

## Function Descriptions
These python scripts implement  basic functions that are described below:

- `get_devices.py` - Collects all device information from the SD-WAN vManage
-  `get_vpn.py` - - Collects all VPN information from the SD-WAN vManage

## Output example

![sdwan](./demo.gif)

## About me

Network Automation Developer Advocate for Cisco DevNet.
I'm like Hugh Hefner... minus the mansion, the exotic cars, the girls, the magazine and the money. So basically, I have a robe.

Find me here: [LinkedIn](https://www.linkedin.com/in/stuarteclark/) / [Twitter](https://twitter.com/bigevilbeard)

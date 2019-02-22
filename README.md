# SDWAN Demo Code Use for CLEUR 2019

All code has been tested on Cisco Devnet Always On SDWAN sandbox [HERE](https://devnetsandbox.cisco.com/RM/Diagram/Index/4fb544ad-c88c-4227-8b09-5d35aa26a63b?diagramType=Topology) and the Reservable SDWAN sandbox [HERE](https://devnetsandbox.cisco.com/RM/Diagram/Index/8a5390bf-3017-4dc2-a77b-23b6cf8b2267?diagramType=Topology) Please see the sandbox pages for credentials and reservations. This demo example is based on Python 3.6 and was tested successfully under that version.

```
python3 -m venv venv
source venv/bin/activate
python -V
Python 3.6.5
```

The requirements

`get_devices.py` and `get_vpn.py` use the Python library for use with Viptela vManage API


## Installation
```
pip install -r requirements
```
## Bulk API Operations

RESTful bulk API calls allow you to issue a single RESTful API command to collect information about multiple vEdge routers in the overlay network. The information is returned in batches.

You can perform two types of bulk API operations:

`State`— These operations return status information about the sdwan devices, such as the number and state of OMP and BFD sessions

`Statistics` — These operations return statistics from the sdwan devices, such as the number of transmitted and received data packets


## Returns All Inventory Data
This section of the code will retrieve the inventory data of the vMange and return summary data of all devices in the network. The data includes SystemIP, Hostname, Version of code, UUID and interfaces and statistics. The second part of the demo presents the detailed tunnel statistics on an individual vEdge.

## Function Descriptions
This python script implements four basic functions that are described below:

`initalize_connection` - Initializes a connection to the vManage server
`get_inventory` - Get an inventory dictionary that correlates the system-ip with the hostname
`get_statistic` - Return the interface statistics for each interface in each device
`get_tunnel_statistic` - For a given vEdge, return the statistics on all the tunnels that are defined on that device



![sdwan](./demo.gif)

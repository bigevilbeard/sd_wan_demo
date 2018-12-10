import requests
import urllib3
import configparser



def initalize_connection(ipaddress,username,password):

    """
    This function will initialize a connection to the Viptela vManage platform.

    :param ipaddress: This is the IP Address and Port number of vManage (i.e., "192.168.0.1:8443")
    :param username:  This is the username for vManage
    :param password:  This is a password for vManage
    :return: A session object which can be used to make subsequent calls for other queries
    """

    # Disable warnings like unsigned certificates, etc.
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url="https://"+ipaddress+"/j_security_check"

    payload = "j_username="+username+"&j_password="+password
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        }

    sess=requests.session()

    # Handle exceptions if we cannot connect to the vManage
    try:
        response = sess.request("POST", url, data=payload, headers=headers,verify=False,timeout=10)
    except requests.exceptions.ConnectionError:
        print ("Unable to Connect to "+ipaddress)
        return False

    return sess

def get_inventory(serveraddress,session):

    """
    This function retrieves the complete hostname data for everything in vManage
    :param serveraddress: This is the IP Address and Port number of vManage (i.e., "192.168.0.1:8443")
    :param session: session object that was returned from the prior initialize_connection function
    :return: inventory data in a dictionary format
    """
    print("Retrieving the inventory data from the vManage at "+serveraddress+"\n")

    url = "https://" + serveraddress + "/dataservice/device"
    response = session.request("GET", url, verify=False,timeout=10)
    json_string = response.json()
    #print(json_string)
    #for item in json_string['data']:
    #   print(item)

    # Initialize the inventory data dictionary
    inv={}

    # Store each item in the dictionary with the key of the "system-ip"
    for item in json_string['data']:
    #   print (item['local-system-ip']+"   "+item['host-name'])
        inv[item['system-ip']]=item['host-name']

    return(inv)


def get_statistic(serveraddress,session):
    """

    :param serveraddress: This is the IP Address and Port number of vManage (i.e., "192.168.0.1:8443")
    :param session: session object that was returned from the prior initialize_connection function
    :return: nothing
    """
    url = "https://"+serveraddress+"/dataservice/device"
    response = session.request("GET", url,verify=False,timeout=10)
    json_string=response.json()
    #print(json_string)
    #for item in json_string['data']:
    #   print(item)


    for item in json_string['data']:
        system_ip=item['system-ip']
        print('{0:15}  {1:20}  {2}     {3:36}  '.format("System IP", "Hostname", "Version","UUID"))
        print('{0:15}  {1:20}  {2}     {3:36}  '.format("---------", "--------", "-------","------------------------------------"))
        print ('{0:15}  {1:20}  {2}      {3:36}  '.format(item['system-ip'],item['host-name'],item['version'],item['uuid']))

        #print ("Retrieving Statistics for "+system_ip)
        url = "https://"+serveraddress+"/dataservice/device/interface/stats?deviceId="+system_ip
        response = session.request("GET", url,verify=False)
        json_string=response.json()

        # If there is an error, with the query then let's print out the error code
        if 'error' in json_string:
            print ("An Error Occured processing the data")
            print (json_string['error']['details'])
        else:
            #print(json_string)
            print ("\n")
            print('      {0:9}     {1:10}   {2:10}      {3:10}'.format("ifName","vpn-id","tx-packets","rx-packets"))
            print('      {0:9}     {1:10}   {2:10}      {3:10}'.format("------","------","----------","----------"))
            #for stats in json_string['data']:
            #    print(stats)

            # Reset the rx and tx total statistics for each interface
            rx=0
            tx=0

            # Process though each interface and print out the data
            for stats in json_string['data']:
                # We only want to print the ipv4 interfaces
                if stats['af-type']!='ipv6':
                    print('      {0:9}     {1:10}   {2:10d}      {3:10d}'.format(stats['ifname'],stats['vpn-id'],int(stats['tx-packets']),int(stats['rx-packets'])))
                rx=rx+int(stats['rx-packets'])
                tx=tx+int(stats['tx-packets'])
            print('                                 {0}      {1}'.format("----------","----------"))
            print('      {0:9}     {1:10}   {2:10d}      {3:10d}'.format(" ","Total",tx,rx))
        print ("\n")


def get_tunnel_statistic(serveraddress,session,systemip):

    """
    This function will return the details for all the tunnels for a particular endpoint
    :param serveraddress: This is the IP Address and Port number of vManage (i.e., "192.168.0.1:8443")
    :param session: session object that was returned from the prior initialize_connection function
    :param systemip: systemip of a device that we want to receive detailed statistics on
    :return: nothing
    """
    print ("Returning the tunnel statistics for device: "+systemip+"\n")

    url = "https://"+serveraddress+"/dataservice/device/tunnel/statistics?deviceId="+systemip

    response = session.request("GET", url,verify=False,timeout=10)
    json_string=response.json()
    #print (json_string)
    #for item in json_string['data']:
    #    print(item)

    # If there is an error, with the query then let's print out the error code
    if 'error' in json_string:
        print("An Error Occured processing the data")
        print(json_string['error']['details'])
    else:
        print('     {0:10}               {1:15} {2:10} {3:10}  {4:10}   {5:10}'.format("Tunnel",
                                                                           "Color",
                                                                           "RX Pkts",
                                                                           "TX Pkts", "RX Bytes",
                                                                           "TX Bytes"))

        print('     {0:10}               {1:15} {2:10} {3:10}  {4:10}   {5:10}'.format("------",
                                                                           "-----",
                                                                           "-------",
                                                                           "-------", "--------",
                                                                           "--------"))

        # Reset the rx and tx total statistics
        rx=0
        tx=0

        # Process through each Tunnel on the device
        for stats in json_string['data']:
            rx=rx+int(stats['rx_octets'])
            tx=tx+int(stats['tx_octets'])
            print('{0:10}->{1:12}   {2:15} {3:10d} {4:10d}   {5:10d}   {6:10d}'.format(stats['vdevice-host-name'],inventory[stats['system-ip']],stats['local-color'],int(stats['rx_pkts']),int(stats['tx_pkts']),int(stats['rx_octets'])*8,int(stats['tx_octets'])*8))

        print('                                                                    ---------    ---------')
        print('                                               Totals:             {0:10d}   {1:10d}'.format(rx*8,tx*8))



print ("Viptela vManage Engine Starting...\n")

# Open up the configuration file and get all application defaults
try:
    config = configparser.ConfigParser()
    config.read('package_config.ini')

    serveraddress = config.get("application","serveraddress")
    username = config.get("application","username")
    password = config.get("application","password")
    systemip = config.get("application","systemip")
except configparser.Error:
    print ("Cannot Parse package_config.ini")
    exit(-1)

print ("Viptela Configuration:")
print ("vManage Server Address: "+serveraddress)
print ("vManage Username: "+username)

session=initalize_connection(serveraddress,username,password)
if session != False:
    inventory=get_inventory(serveraddress,session)
    get_statistic(serveraddress,session)
    get_tunnel_statistic(serveraddress,session,systemip)

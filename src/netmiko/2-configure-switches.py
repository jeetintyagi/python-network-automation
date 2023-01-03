import netmiko

# List of dictionaries, where each dictionary represents a switch
switches = [
    {
        "host": "172.23.253.31",
        "username": "david",
        "password": "cisco",
        "device_type": "cisco_ios",
    },
    {
        "host": "172.23.253.32",
        "username": "david",
        "password": "cisco",
        "device_type": "cisco_ios",
    },
    {
        "host": "172.23.253.33",
        "username": "david",
        "password": "cisco",
        "device_type": "cisco_ios",
    },
]

# Iterate over the list of switches
for switch in switches:

    # Create a ConnectHandler object
    net_connect = netmiko.ConnectHandler(**switch)

    print('Creating VLANS on switch with management IP = ' + switch['host'])
    # iteratively create VLANs and name them

    for n in range(2, 20, 2):  # {initial=2; final=18; step/increment=2}
        # configuring VLAN name as vlan_{n} where 'n' is vlan number{2,4,6,...,18}
        configuringVlan = ["vlan " + str(n), "name " + "vlan_{n}"]
        net_connect.send_config_set(configuringVlan)

    # Disconnect from the switch
    net_connect.disconnect()

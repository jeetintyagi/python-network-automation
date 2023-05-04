import netmiko

# List of dictionaries, where each dictionary represents a router
routers = [
    {
        "host": "192.168.244.244",
        "username": "david",
        "password": "cisco",
        "device_type": "cisco_ios",
    },
    {
        "host": "192.168.244.245",
        "username": "david",
        "password": "cisco",
        "device_type": "cisco_ios",
    },
    {
        "host": "192.168.244.246",
        "username": "david",
        "password": "cisco",
        "device_type": "cisco_ios",
    },
]

# Iterate over the list of routers
for router in routers:

    # Create a ConnectHandler object
    net_connect = netmiko.ConnectHandler(**router)

    # set of commands
    commands = ['show running-config',
                'show ip route', 'show ip interface brief']

    # iterating over the list of commands and writing the output in the 'output variable'
    output = ''
    for command in commands:
        output = net_connect.send_command(command)
        print(f'\nOutput for the command : {command}\n')
        print(output)


# Disconnect from the router
net_connect.disconnect()

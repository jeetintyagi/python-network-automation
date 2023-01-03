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

    # Send the command to retrieve the configuration
    config = net_connect.send_command("show running-config")

    print("Backing up running-config of " + switch["host"])

    # Save the running-config to a file
    with open(f"{switch['host']}.txt", "w") as f:
        f.write(config)

    # Disconnect from the switch
    net_connect.disconnect()

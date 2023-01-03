"""
(1) Import the necessary libraries, such as netmiko and time.
(2) Define a list of dictionaries, where each dictionary represents 
a switch and contains the necessary information to connect to it, 
such as the hostname or IP address, username, password, and device type.
(3) Iterate over the list of dictionaries and create a "netmiko.ConnectHandler()" 
object for each switch.
(4) Connect to the switch using ".connect()" method.
(5) Send the appropriate commands to retrieve the configuration of the 
switch using the ".send_command()" method. This may vary depending on the 
type of switch and the command-line interface(CLI) used.
(6) Save the configuration to a text file, using the management IP of the 
switch as the file name.
(7) Disconnect from the switch using the ".disconnect()" method.

"""
import netmiko

# List of dictionaries, where each dictionary represents a switch
switches = [
    {
        "host": "192.168.1.1",
        "username": "admin",
        "password": "password",
        "device_type": "cisco_ios",
    },
    {
        "host": "192.168.1.2",
        "username": "admin",
        "password": "password",
        "device_type": "cisco_ios",
    },
]

# Iterate over the list of switches
for switch in switches:
    # Create a ConnectHandler object
    net_connect = netmiko.ConnectHandler(**switch)

    # Connect to the switch
    net_connect.connect()

    # Send the command to retrieve the configuration
    config = net_connect.send_command("show running-config")

    # Save the configuration to a file
    with open(f"{switch['host']}.txt", "w") as f:
        f.write(config)

    # Disconnect from the switch
    net_connect.disconnect()

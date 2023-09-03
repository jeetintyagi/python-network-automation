from netmiko import ConnectHandler
from getpass import getpass

# cisco ios information
cisco1 = {
    "device_type": "cisco_ios",
    "host": "cisco1.lasthop.io",
    "username": "pyclass",
    "password": getpass(),
    # path of the file in which the output will be saved
    "ssh_config_file": "~/.ssh/ssh_config",
}

# Create a ConnectHandler object
#  & retrive users session info into a "ssh_config" file
with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command("show users")

print(output)

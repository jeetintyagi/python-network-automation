# importing libraries
import telnetlib
import time

# List of dictionaries, where each dictionary represents a switch
# user "ram" is given level 15 privelege -> the user will directly
# enter in privlege mode upon successful telnet authentication
switches = [
    {
        "host": "192.168.1.2",
        "username": "ram",
        "password": "cisco",
    },
    {
        "host": "192.168.1.3",
        "username": "ram",
        "password": "cisco",
    },
]

# Iterate over the list of switches
for switch in switches:
    # Connect to the switch
    tn = telnetlib.Telnet(switch["host"])

    # Wait for the login prompt
    time.sleep(1)

    # Enter the username and password
    tn.read_until(b"Username: ")
    tn.write(switch["username"].encode("ascii") + b"\n")
    tn.read_until(b"Password: ")
    tn.write(switch["password"].encode("ascii") + b"\n")

    # Send the command to retrieve the configuration
    tn.write(b"terminal length 0\n")
    tn.write(b"show running-config\n")

    # Read the output and save it to a file
    config = tn.read_all().decode("ascii")
    # fileName = running-config_192.168.1.2.txt
    fileName = "running-config_" + {switch['host']} + ".txt"
    with open(f"{fileName}", "w") as f:
        f.write(config)

    # Disconnect from the switch
    tn.write(b"exit\n")
    tn.close()

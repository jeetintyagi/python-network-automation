import getpass
import telnetlib
import os

# asking for username and password from the user beforehand
user = input("Enter your telnet username: ")
password = getpass.getpass()

# creating a directory "Switch_running-configs" using "os" library
# inbuilt feature & using exception handling to catch the error if occurs
dirName = './Switch_running-configs'

try:
    os.mkdir(dirName)
except OSError as error:
    print(error)

# all management IPs of switch are stored in the file "ip-addresses.txt"
# using file-handling to open the file in python and striping IPs line by line
# and telnet each switch and configuring VlANs on each of them using loops in python
file = open('ip-addresses.txt')

for ipAddress in file:

    # .strip() returns a copy of the string without leading/trailing whitespace
    ipAddress = ipAddress.strip()
    print('Backing up running-config of switch ' + ipAddress)

    # telnet the host(switch) and writing username and password into CLI
    tn = telnetlib.Telnet(ipAddress)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')

    # executing configuration to show the running-config in one go
    # & not the default terminal length(24) lines
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b'terminal length 0\n')
    tn.write(b'show running-config\n')
    tn.write(b'exit\n')

    # creating and opening a file in write mode inside the
    # Switch_running-configs directory and writing the switch
    # running-config in the file after decoding the running-config
    # prompted on the CLI
    fileName = 'switch_running-config_' + ipAddress
    filePath = dirName + "/" + fileName
    readoutput = tn.read_until(b'telnet')
    saveoutput = open(filePath, 'w+')
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write('\n')
    saveoutput.close()

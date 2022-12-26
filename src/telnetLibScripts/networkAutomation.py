# importing libraries
import getpass
import telnetlib

# hardcoding host ip to HOST variable & telnet authentication
HOST = "192.168.1.21"
user = input("Enter your telnet username: ")
password = getpass.getpass()

# telnet the host(switch) and asking password from the user
tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# executing configuring on switch -
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"interface e0/1\n")
tn.write(b"switchport access vlan 10\n")
tn.write(b"switchport mode access\n")
tn.write(b"interface e0/2\n")
tn.write(b"switchport access vlan 20\n")
tn.write(b"switchport mode access\n")

# writing the configuration terminating telnet session with the switch
tn.write(b"end\n")
tn.write(b"write\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

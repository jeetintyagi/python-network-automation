# importing libraries
import getpass
import telnetlib

# hardcoding host ip to HOST variable & telnet authentication
HOST = "172.22.23.20"
user = input("Enter your telnet username: ")
password = getpass.getpass()

# telnet the host(router) and asking password from the user
tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# executing configuration on router -
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"interface f0/0\n")
tn.write(b"ip ospf 100 area 0\n")

tn.write(b"interface l0\n")
tn.write(b"ip ospf 100 area 0\n")

tn.write(b"router ospf 100\n")
tn.write(b"router-id 1.1.1.1\n")


# writing the configuration terminating telnet session with the switch
tn.write(b"end\n")
tn.write(b"write\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

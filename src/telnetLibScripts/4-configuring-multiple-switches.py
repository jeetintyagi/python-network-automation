# importing libraries
import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()
# all management IPs of switch are stored in the file "ip-address.txt"
# using file-handling to open the file in python and striping IPs line by line
# and telnet each switch and configuring VlANs on each of them using loops in python
file = open('ip-addresses.txt')

for ipAddress in file:
    # .strip() returns a copy of the string with leading and trailing whitespace removed
    ipAddressFinal = ipAddress.strip()

    # telnet the host(switch) and asking for username & password
    tn = telnetlib.Telnet(ipAddressFinal)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    # executing configuring on switch -
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")
    
    for n in range(2, 20, 2):  # {initial=2; final=20; step/increment=2}
        tn.write(b"vlan "+str(n).encode("ascii") + b"\n")
        # configuring VLAN name as VLAN{n} where 'n' is vlan number{2,4,6,...,20}
        tn.write(b"name tech"+str(n).encode("ascii") + b"\n")
        tn.write(b"exit\n")

    # writing the configuration terminating telnet session with the switch
    tn.write(b"end\n")
    tn.write(b"write\n")
    tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

# importing libraries
import getpass
import telnetlib

# hardcoding host ip to HOST variable & telnet authentication
HOST = "172.30.195.21"
user = input("Enter your telnet username: ")
password = getpass.getpass()

# telnet the host(switch) and asking password from the user
tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# executing configuration on switch -
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

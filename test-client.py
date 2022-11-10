from struct import *
from socket import *
from time import *

#Adress to connect to the server
ADDRESS = "lagrange.ccom.uprrp.edu"
PORT = 4205
serverAddrPort = (ADDRESS,PORT)
bufferSize = 4096

s = socket(AF_INET,SOCK_STREAM)
s.connect(serverAddrPort)
s.settimeout(1)

#s.bind(serverAddrPort)
msg = "Hola"
s.send(msg.encode())
recvMsg = s.recv(bufferSize)
print(recvMsg)

print("\n\nPlease choose one operation:\n\t1.Sum\n\t2.Substraction\n\t3.Muliplication\n\t4.Division\n\t5.Factorial\n\t6.Summatory")
inp = int(input("\nOperation >>> "))

inp2send = pack("i",inp)

msg = s.recv(bufferSize)

print(str(msg))

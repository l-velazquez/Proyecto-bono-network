from struct import *
from socket import *
from time import *

#Adress to connect to the server
ADDRESS = "lagrange.ccom.uprrp.edu"
PORT = 4205
serverAddrPort = (ADDRESS,PORT)
bufferSize = 1024

s = socket(AF_INET,SOCK_STREAM)
s.connect(serverAddrPort)
s.settimeout(1)

#s.bind(serverAddrPort)

#Print to terminal for the client
print("\n\nPlease choose one operation:\n\t1.Sum\n\t2.Substraction\n\t3.Muliplication\n\t4.Division\n\t5.Factorial\n\t6.Summatory")
inp = int(input("\nOperation >>> "))

if(inp == (1 or 2 or 3 or 4)):
    print("Please add two inputs:")
    inp1 = int(input("Input 1 >>>"))
    inp2 = int(input("Input 2 >>>"))
    inp2send = (inp,inp1,inp2)
else:
    print("Input number")
    inp1 = int(input("Input >>>"))
    inp2send = inp + inp1

print(inp2send)
packedObj1 = pack("i", inp)
packedObj2 = pack("i", inp1)
packedObj3 = pack("i", inp2)

print("sending:",packedObj1)
s.send(packedObj1)
#s.send(packedObj2)
#s.send(packedObj3)
#unpackedObj = unpack("iii",packedObj)
#print(unpackedObj)

#1
msg = s.recv(bufferSize)
print(msg)
unpackedObj = unpack("cccccccc", msg)
print(unpackedObj)
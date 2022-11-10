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

#Print to terminal for the client
print("\n\nPlease choose one operation:\n\t1.Sum\n\t2.Substraction\n\t3.Muliplication\n\t4.Division\n\t5.Factorial\n\t6.Summatory")
inp = int(input("\nOperation >>> "))

if(inp < 5):
    print("Please add two inputs:")
    inp1 = pack("i",int(input("Input 1 >>>")))
    inp2 = pack("i",int(input("Input 2 >>>")))
    inp0 = pack("B", inp)
    inp2send = (inp0+inp1+inp2)
    #print(unpack("iii",inp2send))
else:
    print("Input number")
    inp1 = pack("i", int(input("Input >>>")))
    inp0 = pack("B",inp)
    inp2send = (inp0+inp1)
    #print(unpack("ii",inp2send))

print("sending ",inp2send)


s.send(inp2send)
#s.send(packedObj2)
#s.send(packedObj3)
#unpackedObj = unpack("iii",packedObj)
#print(unpackedObj)
message = s.recv(bufferSize)

print(str(message))
print(len(message))
if len(message)<2:
    result = unpack("b",message)
    #print(result)
#result1 = unpack("i", message[1:5])
else:
    result = unpack("bi",message)


if result[0]==3:
    print("Invalid command")
#print(result1)
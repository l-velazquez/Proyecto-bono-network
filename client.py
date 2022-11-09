from struct import *
from time import *

ADDRESS = "136.145.181.51"
PORT = 4205
bufferSize = 1024


print("Please choose one operation:\n\t1. Sum\n\t2.Substraction\n\t3.Muliplication\n\t4.Division\n\t5.Factorial\n\tSummatory")
inp = input("\nOperation >>> ")

print()

if(inp == 1 or inp == 2 or inp == 3 or inp ==4):
    print("Please add two inputs:")
    inp1 = input("Input 1 >>>")
    inp2 = input("Input 2 >>>")
else:
    print("Input number")
    inp1 = input("Input >>>")

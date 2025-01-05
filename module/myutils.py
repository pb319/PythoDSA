# It's a demonstration of "User Defined Modules"
import math
from traceback import print_tb


def strFinder(input_str:str)->str:
    return f"Hi {input_str}, Welcome!!"

def primeCheck(num:int):
    i = 2
    isPrime = False
    for i in range(math.floor(math.sqrt(num))):
        if i%num == 0:
            isPrime = True
            break

    if (isPrime):
        print("It is not a Prime")
    else:
        print("It is a prime")

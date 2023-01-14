#rjs
#Personal project for COMP 1113 - Applied Mathematics
#Converting bases

#****************************#
# Do not add commas to split list
#
# b_d (binary to decimal)
#****************************#

import math


def outputVal(base, desiredBase, value):
    if base ==2 and desiredBase == 10:
        return b_d(value)

def b_d(value):  #binary to decimal
    if "." in value:
        valuelst = value.split(".")
        integers = valuelst[0]
        decimals = valuelst[1]
        decimal_sum = 0
        for x in range(len(decimals)):
            if decimals[x] == "1":
                decimal_sum += 2**(-abs(x+1))
        bin_bd = int(integers, 2) + decimal_sum
        return bin_bd
    else:
       bin_bd = int(value, 2)
       return bin_bd
       

#input
while True:
    while True:
        try:
            baseVal = int(input('Enter the base value (From 2 to 16): '))
            if baseVal < 2 or baseVal > 16:
                raise ValueError #this will send it to the print message and back to the input option
            break
        except ValueError:
            print("Invalid. The number must be in the range of 2-16.")
    while True:    
        try:   
            toBase = int(input('Enter the desired base (From 2 to 16): '))
            if toBase < 2 or toBase > 16:
                raise ValueError #this will send it to the print message and back to the input option
            break
        except ValueError:
            print("Invalid. The number must be in the range of 2-16.")
    while True:    
        try:
            initVal = str(input('Enter your digits: '))   
            if any(c.isalpha() for c in initVal) == True:
                raise ValueError #this will send it to the print message and back to the input option
            break
        except ValueError:
            print("Invalid. The input should be digits.") 
        

# output
    print('Your converted value is:', outputVal(baseVal, toBase, initVal))





    
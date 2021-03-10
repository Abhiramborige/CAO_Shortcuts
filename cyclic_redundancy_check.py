# returns the xor of two binary representations in string
def xor(a, b):
    result=""
    for i in range(len(b)):
        result=result+str(int(a[i])^int(b[i]))
    return result

# returns the remainder when divisor divides dividend
# we use modulo-2 division, where instead of subtraction, we do xor
def mod2div(dividend, divisor):
    dividend=dividend
    pick=len(divisor)
    tmp=dividend[0:pick]
    # iteration till division lasts, till pick equal to length of dividend
    while(True):
        if tmp[0]=="1":
            tmp=xor(divisor, tmp)
        else:
            tmp=xor("0"*pick, tmp)
        # get the next bit before the getting next bit of quotient
        # we have to leave the last bit from left hand, as it is always 0
        tmp=tmp[1::]+dividend[pick]
        pick+=1
        # going out of loop after the last drop of dividend bit
        if(pick>=len(dividend)):
            if tmp[0]=="1":
                tmp=xor(divisor, tmp)
            else:
                tmp=xor("0"*pick, tmp)
            tmp=tmp[1::]
            break
	# here the tmp is checkword
    return tmp

# encodes the data by adding the remainder to the data
def encodeData(data, divisor, real_data):
    remainder=mod2div(data, divisor)
    codeword=real_data+remainder
    print("CRC bits: ", remainder)
    print("Transmitted Data:", codeword)
    return codeword

# decodes the data by dividing received data with divisor
# and checks for the remainder for error detection
def decodeData(received_Data, divisor):
    remainder=mod2div(received_Data, divisor)
    print("Remainder: ", remainder)
    remainder=int(remainder,2)
    if remainder!=0:
        print("Since remainder is not equal to 0, the message received is in-correct!!!")
    else:
        print("Since remainder is 0, the message received is correct!!!")

# main function
len_data=int(input("Enter the length of the data: "))
data=input("Enter the data: ")
real_data=data
len_Divisor=int(input("Enter the length of the Generator (Divisor): "))
divisor=input("Enter the Generator(Divisor): ")
print("Number of 0's to be appended: ", (len_Divisor - 1))
data=data+"0"*(len_Divisor-1)
print("Message after appending 0's: ", data)
encodeData(data, divisor, real_data)
received_Data=input("Enter the Received Data: ")
decodeData(received_Data, divisor)

'''
----------OUTPUT----------
Enter the length of the data: 10
Enter the data: 1101011011
Enter the length of the Generator (Divisor): 5
Enter the Generator(Divisor): 10011
Number of 0's to be appended:  4
Message after appending 0's:  11010110110000
CRC bits:  1110
Transmitted Data: 11010110111110
Enter the Received Data: 11110110111110
Remainder:  1110
Since remainder is not equal to 0, the message received is in-correct!!!
>>>
'''

'''
Took help from:
1. https://www.geeksforgeeks.org/modulo-2-binary-division/
2. https://www.geeksforgeeks.org/cyclic-redundancy-check-python/
Thanks for the help !
'''

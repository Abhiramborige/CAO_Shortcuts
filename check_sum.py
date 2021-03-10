# return the complement of any binary representation
def complement_of_msg(msg):
    complement=""
    for i in range(0,len(msg)):
        if(msg[i]=='0'):
            complement+="1"
        else:
            complement+="0"
    return complement

# calculate the sum of binary arguments
def SumOfBinary(*args):
    sum=int(args[0],2)
    for i in range(1,len(args)):
        msg=args[i]
        sum=sum+int(msg,2)
    sum=bin(sum)[2::]
    print("Sum: ",sum)
    return sum

# encode the data to be sent
def encodeData(Sum):
    CheckSum=complement_of_msg(Sum)
    print("Checksum: ",CheckSum)
    return CheckSum

# decode the data received
def decodeData(Sum):
    received_Data=Sum.split(' ')
    args=(i for i in received_Data)
    decode_data=SumOfBinary(*args)
    flag=True
    print("Complement: ",complement_of_msg(decode_data))
    for i in range(len(decode_data)):
        if(decode_data[i]=="0"):
            flag=False
            break
    if flag==True:
        print("The data received is correct!!!")
    else:
        print("The data received is in-correct!!!")
    return decode_data

# main function
n=int(input("Enter the number of parts of message: "))
arr=[]
for i in range(n):
    data=input(f"Enter the {i+1}th data: ")
    arr.append(data)

# creating a generator
args=(i for i in arr)
SenderData=encodeData(SumOfBinary(*args))
transmit_data=""
for string in arr:
    transmit_data=transmit_data+string+" "
transmit_data+=SenderData

print("Data to be Transmitted: ",transmit_data)
received_Data=input("Enter the Received Data: ")
receiverData=decodeData(received_Data)

'''
----------OUTPUT----------
Enter the number of parts of message: 4
Enter the 1th data: 10010
Enter the 2th data: 00111
Enter the 3th data: 10010
Enter the 4th data: 01110
Sum:  111001
Checksum:  000110
Data to be Transmitted:  10010 00111 10010 01110 000110
Enter the Received Data: 10010 00111 10010 1110 110
Sum:  111111
Complement:  000000
The data received is correct!!!
>>> 
'''

'''
Took help from:
1. https://www.geeksforgeeks.org/error-detection-code-checksum/
2. https://stackoverflow.com/questions/54508025/passing-multiple-arguments-in-python-on-a-loop
Thanks for the help !
'''

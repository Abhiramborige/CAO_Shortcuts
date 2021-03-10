
# function to get the sequesnce of bits, 
# according to indices for calculating the even parity
def get_msg_for_parity(position, code_word):
    msg=""
    for i in range(len(code_word)-1,-1,-1):
        binary=bin(i+1)[2::]
        # get the kth least significant bit, k is the position
        if(len(binary)>=position):
            if(binary[::-1][position-1]=="1"):
                msg=msg+code_word[len(code_word)-i-1]
    # here msg is the collection of bits to be considered for producing parity
    return msg

# return the parity bit according to the bits in the message, 
# following the even parity
def parity_checker(msg):
    count=0
    parity_bit="0"
    for i in range(len(msg)):
        if(msg[i]=="1"):
            count+=1
    if(count%2!=0):
        parity_bit="1"
    return parity_bit

# return the number of parity bits to be included with the message
def parity_count(msg_length):
    r=1
    while(True):
        if(pow(2,r)>=msg_length+r+1):
            break
        r+=1
    return r

# function to check if number is power of 2
def is_powerof_two(n):
    if(n==0):
        return False
    while(n!=1):
        # if divisible by 2, then get quotient after dividing by 2.
            if(n%2!=0):
                return False
            n=n//2
    return True

# find all the parity bits of the message, get the code word, 
# and print the parity bits
def parity_bit_finder(msg, count):
    code_word=[]
    j=0
    for i in range(len(msg)+count-1,-1,-1):

        # placing parity where index is power of 2
        if(is_powerof_two(i+1)==True):
            code_word.append("X") # here X is parity bit
        # placing the messsage character
        else:
            code_word.append(msg[j])
            j+=1
    
    print("The code word(to be sent to receiver after finding the parity bits) is:\n",code_word)

    # filling the code word array with the parity bits
    for i in range(1,count+1):
        code_word[len(msg)+count-pow(2,i-1)]=parity_checker(get_msg_for_parity(i, code_word))
    for i in range(1,count+1):
        print("P"+str(pow(2,i-1))+" = ",code_word[len(msg)+count-pow(2,i-1)])
    print("Code Word at sender side is:\n",code_word)

msg_length=int(input("Enter the length of the data: "))
msg=input("Enter the data: ")
count=parity_count(msg_length)
print("Number of parity bits is: ",count)
print("Parity bits are: ")
parity_bit_finder(msg, count)

def get_error(msg):
    parity_bit=[]
    count=parity_count(len(msg))
    # getting the parity bit for the bits having the
    # kth bit of their binary representation as 1.
    for i in range(count,0,-1):
        parity_bit.append(parity_checker(get_msg_for_parity(i, msg)))
    error_pos=""
    for i in parity_bit:
        error_pos+=i
    print("The error is in the position ",int(error_pos,2))
    corr_msg=""
    for i in range(len(msg)):
        if(i==len(msg)-int(error_pos,2)):
            # inversion of bit
            if(msg[i]=="0"):
                corr_msg+="1"
            else:
                corr_msg+="0"
        else:
            corr_msg+=msg[i]
    print("The correct message that must be received is ",corr_msg)
            
rec_msg=input("Enter the message received: ")
get_error(rec_msg)


'''
----------OUTPUT----------
Enter the length of the data: 7
Enter the data: 1001101
Number of parity bits is:  4
Parity bits are: 
The code word(to be sent to receiver after finding the parity bits) is:
 ['1', '0', '0', 'X', '1', '1', '0', 'X', '1', 'X', 'X']
P1 =  1
P2 =  0
P4 =  0
P8 =  1
Code Word at sender side is:
 ['1', '0', '0', '1', '1', '1', '0', '0', '1', '0', '1']
Enter the message received: 10010100101
The error is in the position  7
The correct message that must be received is  10011100101
>>>
'''


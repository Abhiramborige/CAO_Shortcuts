
def deci_to_bin(n):
    return bin(n).replace("0b", "")

def shift_left(C,AC,Q):
    
    C=AC[0]
    
    temp_AC=list(AC)
    for i in range(1,len(AC)):
        temp_AC[i-1]=temp_AC[i]
    temp_AC[len(AC)-1]=Q[0]
    AC=''
    AC=AC.join(temp_AC)

    temp_Q=list(Q)
    for i in range(1,len(Q)):
        temp_Q[i-1]=temp_Q[i]
    temp_Q[len(Q)-1]='_'
    Q=''
    Q=Q.join(temp_Q)
    
    return(C,AC,Q)

def operation(C,AC,M):
    temp=C+AC
    temp=bin(int(temp,2)+int(M,2))
    temp=temp.replace("0b","")

    # discard the carry while operation is done
    if(len(temp)>len(M)):
        temp=temp[1::]
    return(temp[0],temp[1::])


# Main function
AC=''
C='0'

Q=input("Enter the dividend(Q)  :  ")
Q=deci_to_bin(int(Q))

M=input("Enter the divisor(M)   :  ")
M=deci_to_bin(int(M))

if(len(Q)>len(M)):
    for i in range(len(Q)):
        AC=AC+'0'
else:
    for i in range(len(M)):
        AC=AC+'0'
print("Initial C value is     : ",C)
print("Initial AC value is    : ",AC)
print("Initial Q value is     : ",Q)

for i in range(len(Q)-len(M)):
    M='0'+M
# adding one bit extra
M='0'+M
print("Value of M is          : ",M)

# two's complement
M_array=list(M)
for i in range(len(M)):
    if(M[i]=='0'):
        M_array[i]='1'
    if(M[i]=='1'):
        M_array[i]='0'
M_negative=''
M_negative=M_negative.join(M_array)
M_negative=bin(int(M_negative,2)+int('1',2))
M_negative=M_negative.replace("0b","")
print("Two's complement of M  : ",M_negative)
print()

print("---------------------------------------------------------------------------------------------------------------------")
print("\t C "," "*int(len(AC)/2),"AC"," "*int(len(AC)/2)," "*int(len(Q)/2),"Q"," "*int(len(Q)/2),"     Operation done")
print("---------------------------------------------------------------------------------------------------------------------")
print("\t",C,"  ",AC,"  ",Q,"   ","Initial values")
print()

      
for i in range(len(Q)):
    print("step",(i+1),":  ")
    C,AC,Q=shift_left(C,AC,Q)

    print("\t",C,"  ",AC,"  ",Q,"   ","After shift left operation")

    C,AC=operation(C,AC,M_negative)
    print("\t",C,"  ",AC,"  ",Q,"   ","AC_equals_AC_minus_M operation")
    
    if(C=='1'):
        temp_Q=list(Q)
        temp_Q[len(Q)-1]='0'
        Q=''
        Q=Q.join(temp_Q)
        
        C,AC=operation(C,AC,M)
        print("\t",C,"  ",AC,"  ",Q,"   ","AC_equals_AC_plus_M operation")
        
    else:
        temp_Q=list(Q)
        temp_Q[len(Q)-1]='1'
        Q=''
        Q=Q.join(temp_Q)
    print()
    
print('\nFinal values')    
print("\t",C,"  ",AC,"  ",Q)
print()
print("Remainder=(C,AC)       : ",int(C+AC,2))
print("Quotient=(Q)           : ",int(Q,2))

'''
----------OUTPUT----------
Enter the dividend(Q)  :  479
Enter the divisor(M)   :  62
Initial C value is     :  0
Initial AC value is    :  000000000
Initial Q value is     :  111011111
Value of M is          :  0000111110
Two's complement of M  :  1111000010

---------------------------------------------------------------------------------------------------------------------
	 C       AC           Q           Operation done
---------------------------------------------------------------------------------------------------------------------
	 0    000000000    111011111     Initial values

step 1 :  
	 0    000000001    11011111_     After shift left operation
	 1    111000011    11011111_     AC_equals_AC_minus_M operation
	 0    000000001    110111110     AC_equals_AC_plus_M operation

step 2 :  
	 0    000000011    10111110_     After shift left operation
	 1    111000101    10111110_     AC_equals_AC_minus_M operation
	 0    000000011    101111100     AC_equals_AC_plus_M operation

step 3 :  
	 0    000000111    01111100_     After shift left operation
	 1    111001001    01111100_     AC_equals_AC_minus_M operation
	 0    000000111    011111000     AC_equals_AC_plus_M operation

step 4 :  
	 0    000001110    11111000_     After shift left operation
	 1    111010000    11111000_     AC_equals_AC_minus_M operation
	 0    000001110    111110000     AC_equals_AC_plus_M operation

step 5 :  
	 0    000011101    11110000_     After shift left operation
	 1    111011111    11110000_     AC_equals_AC_minus_M operation
	 0    000011101    111100000     AC_equals_AC_plus_M operation

step 6 :  
	 0    000111011    11100000_     After shift left operation
	 1    111111101    11100000_     AC_equals_AC_minus_M operation
	 0    000111011    111000000     AC_equals_AC_plus_M operation

step 7 :  
	 0    001110111    11000000_     After shift left operation
	 0    000111001    11000000_     AC_equals_AC_minus_M operation

step 8 :  
	 0    001110011    10000001_     After shift left operation
	 0    000110101    10000001_     AC_equals_AC_minus_M operation

step 9 :  
	 0    001101011    00000011_     After shift left operation
	 0    000101101    00000011_     AC_equals_AC_minus_M operation


Final values
	 0    000101101    000000111

Remainder=(C,AC)       :  45
Quotient=(Q)           :  7
>>> 
'''

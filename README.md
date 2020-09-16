## Restoring Division.
### Sample input and output:

#####Enter the dividend(Q)  :  479
#####Enter the divisor(M)   :  62
#####Initial C value is     :  0
#####Initial AC value is    :  000000000
#####Initial Q value is     :  111011111
#####Value of M is          :  0000111110
#####Two's complement of M  :  1111000010
#####
#####---------------------------------------------------------------------------------------------------------------------
#####	 C       AC           Q           Operation done
#####---------------------------------------------------------------------------------------------------------------------
#####	 0    000000000    111011111     Initial values
#####
#####step 1 :  
#####	 0    000000001    11011111_     After shift left operation
#####	 1    111000011    11011111_     AC_equals_AC_minus_M operation
#####	 0    000000001    110111110     AC_equals_AC_plus_M operation
#####
#####step 2 :  
#####	 0    000000011    10111110_     After shift left operation
#####	 1    111000101    10111110_     AC_equals_AC_minus_M operation
#####	 0    000000011    101111100     AC_equals_AC_plus_M operation
#####
#####step 3 :  
#####	 0    000000111    01111100_     After shift left operation
#####	 1    111001001    01111100_     AC_equals_AC_minus_M operation
#####	 0    000000111    011111000     AC_equals_AC_plus_M operation
#####
#####step 4 :  
#####	 0    000001110    11111000_     After shift left operation
#####	 1    111010000    11111000_     AC_equals_AC_minus_M operation
#####	 0    000001110    111110000     AC_equals_AC_plus_M operation
#####
#####step 5 :  
#####	 0    000011101    11110000_     After shift left operation
#####	 1    111011111    11110000_     AC_equals_AC_minus_M operation
#####	 0    000011101    111100000     AC_equals_AC_plus_M operation
#####
#####step 6 :  
#####	 0    000111011    11100000_     After shift left operation
#####	 1    111111101    11100000_     AC_equals_AC_minus_M operation
#####	 0    000111011    111000000     AC_equals_AC_plus_M operation
#####
#####step 7 :  
#####	 0    001110111    11000000_     After shift left operation
#####	 0    000111001    11000000_     AC_equals_AC_minus_M operation
#####
#####step 8 :  
#####	 0    001110011    10000001_     After shift left operation
#####	 0    000110101    10000001_     AC_equals_AC_minus_M operation
#####
#####step 9 :  
#####	 0    001101011    00000011_     After shift left operation
#####	 0    000101101    00000011_     AC_equals_AC_minus_M operation
#####
#####
#####Final values
#####	 0    000101101    000000111
#####
#####Remainder=(C,AC)       :  45
#####Quotient=(Q)           :  7
#####>>> 

## Non-Restoring Division.
### Sample input and output:
---------------------------------------------------------------------------------------------------------------------
Enter the dividend(Q)  : 479
Enter the divisor(M)   : 62
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

step 2 :  
	 1    110000111    10111110_     After shift left operation
	 1    111000101    10111110_     AC_equals_AC_plus_M operation

step 3 :  
	 1    110001011    01111100_     After shift left operation
	 1    111001001    01111100_     AC_equals_AC_plus_M operation

step 4 :  
	 1    110010010    11111000_     After shift left operation
	 1    111010000    11111000_     AC_equals_AC_plus_M operation

step 5 :  
	 1    110100001    11110000_     After shift left operation
	 1    111011111    11110000_     AC_equals_AC_plus_M operation

step 6 :  
	 1    110111111    11100000_     After shift left operation
	 1    111111101    11100000_     AC_equals_AC_plus_M operation

step 7 :  
	 1    111111011    11000000_     After shift left operation
	 0    000111001    11000000_     AC_equals_AC_plus_M operation

step 8 :  
	 0    001110011    10000001_     After shift left operation
	 0    000110101    10000001_     AC_equals_AC_minus_M operation

step 9 :  
	 0    001101011    00000011_     After shift left operation
	 0    000101101    00000011_     AC_equals_AC_minus_M operation

Final step: 
No final step as AC is positive.

Final values
	 0    000101101    000000111

Remainder=(C,AC)       :  45
Quotient=(Q)           :  7
>>> 



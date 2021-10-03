/* Booth’s algorithm is a multiplication algorithm that multiplies two signed binary numbers in 2’s complement notation. 
Booth used desk calculators that were faster at shifting than adding and created the algorithm to increase their speed. Booth’s algorithm is of interest in the study of computer architecture. Here’s the implementation of the algorithm. 
Examples: 
 

Input : 0110, 0010
Output :  qn      q[n+1]                  AC      QR     sc(step count)
                          initial         0000   0010        4
          0       0       rightShift      0000   0001        3
          1       0       A = A - BR      1010
                          rightShift      1101   0000        2
          0       1       A = A + BR      0011
                          rightShift      0001   1000        1
          0       0       rightShift      0000   1100        0

Result=1100 */

/*  Algorithm : 
 

Put multiplicand in BR and multiplier in QR 
and then the algorithm works as per the following conditions : 
1. If Qn and Qn+1 are same i.e. 00 or 11 perform arithmetic shift by 1 bit. 
2. If Qn Qn+1 = 10 do A= A + BR and perform arithmetic shift by 1 bit. 
3. If Qn Qn+1 = 01 do A= A – BR and perform arithmetic shift by 1 bit.  
*/

// Java code to implement booth's algorithm
class Booth
{
 
    // function to perform adding in the accumulator
    static void add(int ac[], int x[], int qrn)
    {
        int i, c = 0;
 
        for (i = 0; i < qrn; i++)
        {
 
            // updating accumulator with A = A + BR
            ac[i] = ac[i] + x[i] + c;
 
            if (ac[i] > 1)
            {
                ac[i] = ac[i] % 2;
                c = 1;
            }
            else
            {
                c = 0;
            }
        }
    }
 
    // function to find the number's complement
    static void complement(int a[], int n)
    {
        int i;
        int[] x = new int[8];
        x[0] = 1;
 
        for (i = 0; i < n; i++)
        {
            a[i] = (a[i] + 1) % 2;
        }
        add(a, x, n);
    }
 
    // function ro perform right shift
    static void rightShift(int ac[], int qr[],
                            int qn, int qrn)
    {
        int temp, i;
        temp = ac[0];
        qn = qr[0];
 
        System.out.print("\t\trightShift\t");
 
        for (i = 0; i < qrn - 1; i++)
        {
            ac[i] = ac[i + 1];
            qr[i] = qr[i + 1];
        }
        qr[qrn - 1] = temp;
    }
 
    // function to display operations
    static void display(int ac[], int qr[], int qrn)
    {
        int i;
 
        // accumulator content
        for (i = qrn - 1; i >= 0; i--)
        {
            System.out.print(ac[i]);
        }
        System.out.print("\t");
 
        // multiplier content
        for (i = qrn - 1; i >= 0; i--)
        {
            System.out.print(qr[i]);
        }
    }
 
    // Function to implement booth's algo
    static void boothAlgorithm(int br[], int qr[], int mt[],
                                            int qrn, int sc)
    {
 
        int qn = 0;
        int[] ac = new int[10];
        int temp = 0;
        System.out.print("qn\tq[n+1]\t\tBR\t\tAC\tQR\t\tsc\n");
        System.out.print("\t\t\tinitial\t\t");
 
        display(ac, qr, qrn);
        System.out.print("\t\t" + sc + "\n");
 
        while (sc != 0)
        {
            System.out.print(qr[0] + "\t" + qn);
 
            // SECOND CONDITION
            if ((qn + qr[0]) == 1)
            {
                if (temp == 0)
                {
 
                    // subtract BR from accumulator
                    add(ac, mt, qrn);
                    System.out.print("\t\tA = A - BR\t");
 
                    for (int i = qrn - 1; i >= 0; i--)
                    {
                        System.out.print(ac[i]);
                    }
                    temp = 1;
                }
                 
                // THIRD CONDITION
                else if (temp == 1)
                {
                    // add BR to accumulator
                    add(ac, br, qrn);
                    System.out.print("\t\tA = A + BR\t");
 
                    for (int i = qrn - 1; i >= 0; i--)
                    {
                        System.out.print(ac[i]);
                    }
                    temp = 0;
                }
                System.out.print("\n\t");
                rightShift(ac, qr, qn, qrn);
            }
             
            // FIRST CONDITION
            else if (qn - qr[0] == 0)
            {
                rightShift(ac, qr, qn, qrn);
            }
 
            display(ac, qr, qrn);
 
            System.out.print("\t");
 
            // decrement counter
            sc--;
            System.out.print("\t" + sc + "\n");
        }
    }
 
    static void reverse(int a[])
    {
        int i, k, n = a.length;
        int t;
        for (i = 0; i < n / 2; i++)
        {
            t = a[i];
            a[i] = a[n - i - 1];
            a[n - i - 1] = t;
        }
    }
     
    // Driver code
    public static void main(String[] args)
    {
        int[] mt = new int[10];
        int sc;
        int brn, qrn;
 
        // Number of multiplicand bit
        brn = 4;
 
        // multiplicand
        int br[] = {0, 1, 1, 0};
 
        // copy multiplier to temp array mt[]
        for (int i = brn - 1; i >= 0; i--)
        {
            mt[i] = br[i];
        }
 
        reverse(br);
 
        complement(mt, brn);
 
        // No. of multiplier bit
        qrn = 4;
 
        // sequence counter
        sc = qrn;
 
        // multiplier
        int qr[] = {1, 0, 1, 0};
        reverse(qr);
 
        boothAlgorithm(br, qr, mt, qrn, sc);
 
        System.out.print("\n"
                + "Result = ");
 
        for (int i = qrn - 1; i >= 0; i--)
        {
            System.out.print(qr[i]);
        }
    }
}
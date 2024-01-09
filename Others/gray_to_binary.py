def binary_to_gray (n):
    """
    This program first reads the binary numbner as input. 
    It then calls the 'binary_to_gray' function to convert the binary number to gray code.
    Finally, it prints out the gray code in binary format using the 'bin' function.   
    """

    return n ^ (n >>1)

binary_num = int(input("Enter a binary number: "), 2)
gray_num = binary_to_gray(binary_num)

int("The gray code is:", bin(gray_num)[2:])

"""
Digital electronics Assignment
UMaT
"""
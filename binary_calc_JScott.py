# COMP 255 Lab 1: binary_calc.py
# Student: Josiah Scott
# Date: 9/14/2023
#
# Description: Performs addition, subtraction, multiplication, 
#              of two binary numbers.
#
# Starter code by T. Wilson, 9/6/23

# NOTE 1: Binary numbers are represented as strings in this module.
#         For example, '110' is 6 in binary.
#
# NOTE 2: This module only works with binary representing integer values.


class BinaryNum:
    """Class for representing binary numbers as strings."""

    def __init__(self, binary_str):
        if (self.valid_binary(binary_str)):
            self.binary = binary_str
        else:
            raise Exception("Invalid binary")


    def valid_binary(self, binary_str):
        """Returns True if binary_str is valid binary; 
           otherwise, returns False."""
        num_ones = binary_str.count("1")
        num_zeros = binary_str.count("0")
        return len(binary_str) == num_ones + num_zeros


    def get_decimal_value(self):
        """Returns the decimal value of self.binary."""
        decimal_value = 0
        digit = 0
            # received help from tutor to complete following code Cal Tipton
            # Iterate through the binary string from left to right
        for digit in self.binary:
            if digit == '1':
                decimal_value = decimal_value * 2 + 1
            elif digit == '0':
                decimal_value = decimal_value * 2 

            # Return the decimal value
        return decimal_value
            

    def __add__(self, b):
        """Parameters: b is a binary number (string).
           Returns: self.binary + b.binary"""

        max_len = max(len(self.binary), len(b.binary))
        self_binary = self.binary.zfill(max_len)
        b_binary = b.binary.zfill(max_len)

        result_binary = []
        carry = 0  # Initialize carry as an integer

        for i in range(max_len - 1, -1, -1):
            bit1 = int(self_binary[i])  # Convert bit1 to an integer
            bit2 = int(b_binary[i])  # Convert bit2 to an integer

            # Calculate the sum of bits without using int()
            bit_sum = bit1 + bit2 + carry

            # Determine the current bit in the result
            if bit_sum == 0:
                result_bit = '0'
                carry = 0
            elif bit_sum == 1:
                result_bit = '1'
                carry = 0
            elif bit_sum == 2:
                result_bit = '0'
                carry = 1
            elif bit_sum == 3:
                result_bit = '1'
                carry = 1

            # Insert the result bit at the beginning of the result list
            result_binary.insert(0, result_bit)

        # If there's still a carry left, add it to the result
        if carry == 1:
            result_binary.insert(0, '1')

        # Convert the result to a binary string
        result = ''.join(result_binary)

        return BinaryNum(result)

    def get_twos_complement(self):
        """Returns the two's complement of self.binary."""

        # Initialize an empty string to store the result
        twos_complement = ""

        # First, invert all the bits
        for position in self.binary:
            if position == '1':
                twos_complement += '0'  # Replace '1' with '0'
            elif position == '0':
                twos_complement += '1'  # Replace '0' with '1'

        # Then, add 1 to the binary number
        twos_complement = BinaryNum(twos_complement) + BinaryNum('1')

        return twos_complement                

    def __sub__(self, b):
        """Parameters: b is a binary number (string).
           Returns: self.binary - b.binary"""

        # Calculate the two's complement of b using the function you created
        twos_complement_b = b.get_twos_complement()

        # Use the __add__ function to subtract b (represented as its two's complement)
        result = self + twos_complement_b

        return result

    def shift(self, val):
        """Perform an arithmetic shift on self.binary
           Parameter: val is an integer indicating the shift amount;
                      shift left if val is positive; otherwise,
                      shift right"""
        
        # Student: Add your function implementation below.
        if val > 0:  # Left shift (shift left if val is positive)
            for i in range(val):
                # Shift left by adding '0' to the right
                self.binary += '0'
        elif val < 0:  # Right shift (shift right if val is negative)
            for i in range(-val):
                # Shift right by removing the rightmost bit and prepending '0' to the left
                self.binary = '0' + self.binary


    def __mul__(self, b):
        """Parameters: b is a binary number (string).
           Returns: self.binary * b.binary"""

        result = BinaryNum('0')  # Initialize the result to zero

        # Iterate through the bits of b from right to left
        for i in range(len(b.binary) - 1, -1, -1):
            if b.binary[i] == '1':
                # If the current bit of b is 1, add self to the result
                result += self

            # Shift self left for the next iteration
            self.shift(1)

        return result
            
        


    def __str__(self):
        return self.binary


def calc(expr):
    """Parse the binary math expression in the string expr, perform 
       the correct binary calculation, and return the result."""

    (num1, op, num2) = expr.split()
    if (op == '+'):
        return BinaryNum(num1) + BinaryNum(num2)
    elif (op == '-'):
        return BinaryNum(num1) - BinaryNum(num2)
    elif (op == '*'):
        return BinaryNum(num1) * BinaryNum(num2)
    else:
        raise Exception("Operator not defined")


def binary_calc():
    """Run the binary calculator."""

    while (True):
        expr = input("calc: ")
        if (expr == ""):
            return
        else:
           print(calc(expr))
        
from binary_calc_JScott import binary_calc
binary_calc()

#I affirm that my work upholds the highest standards of honesty and academic integrity at Wittenberg,
# and that I have neither given nor received any unauthorized assistance.
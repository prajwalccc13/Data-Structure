"""

Use a stack data structure to convert integer values to binary.

Example : 242
                rem
242/2 = 121 -> 0
121//2 = 60  ->1    # gives only integer "/ gives floating number i.e 60.50"
.
.
.
bottom to top
int('11110010', 2) -> int to binary
"""

from stack import Stack

def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        rem = dec_num % 2
        s.push(rem)
        dec_num = dec_num//2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

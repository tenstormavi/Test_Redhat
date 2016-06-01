#!/usr/bin/env python3
value = input("Enter the UTF-16 value: ")
result = ''.join('{:02X}'.format(n) for n in chr(int(value, 16)).encode())
print (("The Converted UTF-8 value is: %s") % result)

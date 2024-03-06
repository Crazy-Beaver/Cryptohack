from Crypto.Util.number import *
input_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
bytes = bytes_to_long(bytes.fromhex(input_hex))
print(bytes)
outcomes = []
for i in range (0,255):
    x = str(i)
    bytevalue = bytes_to_long(x.encode())
    a = bytes ^ bytevalue
    print(a)
    a = long2str(a)
    print(a)
print(outcomes)
#coto kurva?
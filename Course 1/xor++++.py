#POMOOOOOOOOOOOOOOOOOC!
from Crypto.Util.number import *
from pwn import xor
input_string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
input_string_bytes = bytes.fromhex(input_string)
input_cipher = "myXORkey"
print(xor(input_string_bytes,input_cipher.encode()))
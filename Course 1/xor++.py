from Crypto.Util.number import *
input_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
bytes_hex = [o for o in bytes.fromhex(input_hex)]
print(bytes_hex)
outcomes = ""
for i in range (256):
    for j in bytes_hex:
        outcomes = outcomes+(chr(j^i))
    print(i, outcomes)
    outcomes = ""
#coto kurva?
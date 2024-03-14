import math

p = 29
ints = [14, 6, 11]
for i in ints:
    for j in range (0, 10):
        x = (i+(j*p))
        print(x)
        odmocnina = math.sqrt(x)
        print(odmocnina)
    print("")
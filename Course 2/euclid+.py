def nsd(a,b):
    x = 0
    y = 0
    if (a==0) and (b==0):
        return ("NSD není definovaný")
    elif (a==0):
        return b #("NSD je",b)
    elif (b==0):
        return a #("NSD je",a)
    elif (a == b):
        return a #("NSD je",a)
    else:
        while a != b:
            if a > b:
                a -= b
                x += 1
            elif a < b:
                b -= a
                y -= 1
            print(a,b)
            print(x,y)
        return a #("NSD je",a)

p = 26513
q = 32321
#p * u + q * v = nsd(p,q)
print(nsd(p,q)) # = 1 - prvocisla
#26513 * u = 1 - 32321*v
u = 18
v = -10
print((p*u)+(q*v))
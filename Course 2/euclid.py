def nsd(a,b):
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
            elif a < b:
                b -= a
        return a #("NSD je",a)

a = int(input())
b = int(input())
print(nsd(a,b))
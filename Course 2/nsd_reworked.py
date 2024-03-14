def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_euclidean(b % a, a)
        return (gcd, y - (b // a) * x, x)

p = 26513
q = 32321

gcd, x, y = extended_euclidean(p, q)
print("x =", x)
print("y =", y)